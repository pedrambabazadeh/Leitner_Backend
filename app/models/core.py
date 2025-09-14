from datetime import datetime
from app.extensions import db

# 1. WORDS TABLE
class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(191), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # verb, noun, adjective, etc.

    __table_args__ = (db.UniqueConstraint('title', 'category', name='_title_category_uc'),)

    translations = db.relationship('WordTranslation', back_populates='word', cascade="all, delete-orphan")
    examples = db.relationship('WordExample', back_populates='word', cascade="all, delete-orphan")
    word_object_prepositions = db.relationship('WordObjectPreposition', back_populates='word', cascade="all, delete-orphan")


# 2. VERBS TABLE
class Verb(db.Model):
    __tablename__ = 'verbs'

    id = db.Column(db.Integer, db.ForeignKey('words.id'), primary_key=True)
    conj_present = db.Column(db.String(191), nullable=True)
    nominal_form = db.Column(db.String(191), nullable=True)
    conj_past = db.Column(db.String(191), nullable=True)
    perfekt = db.Column(db.String(191), nullable=True)
    auxiliary = db.Column(db.String(50), nullable=True)
    transitive = db.Column(db.Boolean, default=False)
    intransitive = db.Column(db.Boolean, default=False)

    word = db.relationship('Word', backref=db.backref('verb', uselist=False))


# 3. TRANSLATIONS TABLE
class Translation(db.Model):
    __tablename__ = 'translations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language = db.Column(db.String(10), nullable=False)
    text = db.Column(db.String(191), nullable=False)
    category = db.Column(db.String(50), nullable=True)

    words = db.relationship('WordTranslation', back_populates='translation', cascade="all, delete-orphan")

    __table_args__ = (
        db.UniqueConstraint('language', 'text', name='unique_word_meaning'),
    )


# 4. WORD_TRANSLATIONS TABLE
class WordTranslation(db.Model):
    __tablename__ = 'word_translations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    translation_id = db.Column(db.Integer, db.ForeignKey('translations.id'), nullable=False)

    word = db.relationship('Word', back_populates='translations')
    translation = db.relationship('Translation', back_populates='words')


# 5. NOUNS TABLE
class Noun(db.Model):
    __tablename__ = 'nouns'

    id = db.Column(db.Integer, db.ForeignKey('words.id'), primary_key=True)
    plural_form = db.Column(db.String(191), nullable=True)

    word = db.relationship('Word', backref=db.backref('noun', uselist=False))


# 6. PREPOSITIONS AND DIRECT OBJECTS TABLE
class PrepositionObject(db.Model):
    __tablename__ = 'prepositions_objects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(191), nullable=False)
    object = db.Column(db.String(191), nullable=True)


# 7. WORDS_OBJECT_PREPOSITIONS TABLE
class WordObjectPreposition(db.Model):
    __tablename__ = 'word_object_prepositions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    preposition_object_id = db.Column(db.Integer, db.ForeignKey('prepositions_objects.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('word_id', 'preposition_object_id', name='uq_word_preposition_object'),
    )

    word = db.relationship('Word', back_populates='word_object_prepositions')
    preposition_object = db.relationship('PrepositionObject')


# 8. EXAMPLES TABLE
class Example(db.Model):
    __tablename__ = 'examples'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)

    translations = db.relationship('ExampleTranslation', back_populates='example', cascade="all, delete-orphan")
    words = db.relationship('WordExample', back_populates='example', cascade="all, delete-orphan")


# 9. EXAMPLE_TRANSLATIONS TABLE
class ExampleTranslation(db.Model):
    __tablename__ = 'example_translations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    example_id = db.Column(db.Integer, db.ForeignKey('examples.id'), nullable=False)
    language = db.Column(db.String(10), nullable=False)
    translation = db.Column(db.String(255), nullable=False)

    example = db.relationship('Example', back_populates='translations')


# 10. WORD_EXAMPLE TABLE
class WordExample(db.Model):
    __tablename__ = 'word_examples'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    example_id = db.Column(db.Integer, db.ForeignKey('examples.id'), nullable=False)

    word = db.relationship('Word', back_populates='examples')
    example = db.relationship('Example', back_populates='words')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)