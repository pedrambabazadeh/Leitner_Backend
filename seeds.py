# seed.py
from app import create_app
from app.extensions import db
from app.models.core import (
    Word, Verb, Translation, WordTranslation,
    Noun, PrepositionObject, WordObjectPreposition,
    Example, ExampleTranslation, WordExample
)

app = create_app()

def seed_db():
    # 1️⃣ Words
    word1 = Word(title="laufen", category="verb")
    word2 = Word(title="Katze", category="noun")
    db.session.add_all([word1, word2])
    db.session.commit()

    # 2️⃣ Verbs (depends on Words)
    verb1 = Verb(
        id=word1.id,
        conj_present="läuft",
        conj_past="lief",
        perfekt="gelaufen",
        auxiliary="sein",
        transitive=False,
        intransitive=True
    )
    db.session.add(verb1)
    db.session.commit()

    # 3️⃣ Nouns (depends on Words)
    noun1 = Noun(id=word2.id, plural_form="Katzen")
    db.session.add(noun1)
    db.session.commit()

    # 4️⃣ Translations
    trans1 = Translation(language="de", text="laufen", category="verb")
    trans2 = Translation(language="de", text="Katze", category="noun")
    db.session.add_all([trans1, trans2])
    db.session.commit()

    # 5️⃣ WordTranslations (depends on Words + Translations)
    wt1 = WordTranslation(word_id=word1.id, translation_id=trans1.id)
    wt2 = WordTranslation(word_id=word2.id, translation_id=trans2.id)
    db.session.add_all([wt1, wt2])
    db.session.commit()

    # 6️⃣ PrepositionObjects
    prep1 = PrepositionObject(title="auf", object="Tisch")
    db.session.add(prep1)
    db.session.commit()

    # 7️⃣ WordObjectPrepositions (depends on Words + PrepositionObjects)
    wop1 = WordObjectPreposition(word_id=word1.id, preposition_object_id=prep1.id)
    db.session.add(wop1)
    db.session.commit()

    # 8️⃣ Examples
    ex1 = Example(title="Ich laufe jeden Morgen.")
    db.session.add(ex1)
    db.session.commit()

    # 9️⃣ ExampleTranslations (depends on Examples)
    ex_trans1 = ExampleTranslation(example_id=ex1.id, language="de", translation="Ich laufe jeden Morgen.")
    db.session.add(ex_trans1)
    db.session.commit()

    # 🔟 WordExamples (depends on Words + Examples)
    we1 = WordExample(word_id=word1.id, example_id=ex1.id)
    db.session.add(we1)
    db.session.commit()

    print("✅ German database seeded successfully!")

if __name__ == "__main__":
    with app.app_context():
        seed_db()
        print("Database seeded successfully!")