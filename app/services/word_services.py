from app.extensions import db
from app.models import Word, Verb, Noun, WordTranslation, Translation, WordExample, Example

class WordService:
    def add_new_word(self, title, category, extra_data='none', example_data='none', translations='none'):
        """
        Add a word with optional category-specific info, examples, and translations.
        """
        word = Word(title=title, category=category)
        if category == "verb" and extra_data:
            verb = Verb(
                conj_present=extra_data.get("conj_present"),
                nominal_form=extra_data.get("nominal_form"),
                conj_past=extra_data.get("conj_past"),
                perfekt=extra_data.get("perfekt"),
                auxiliary=extra_data.get("auxiliary"),
                transitive=extra_data.get("transitive", False),
                intransitive=extra_data.get("intransitive", False),
                word=word
            )
        elif category == "noun" and extra_data:
            noun = Noun(
                plural_form=extra_data.get("plural_form"),
                word=word
            )

            # Add translations
        if translations:
            for lang, text in translations.items():
                t = Translation(language=lang, text=text)
                db.session.add(t)
                db.session.flush()  # ensure id
                wt = WordTranslation(word=word, translation=t)
                db.session.add(wt)

            # Add example
        if example_data:
            ex = Example(title=example_data.get("title"))
            db.session.add(ex)
            db.session.flush()
            we = WordExample(word=word, example=ex)
            db.session.add(we)

        db.session.add(word)
        db.session.commit()
        return word

    def get_words_by_category(self, category):
        return Word.query.filter_by(category=category).all()

    def search_words(self, entry_letters):
        return Word.query.filter(Word.title.like(f"{entry_letters}%")).all()