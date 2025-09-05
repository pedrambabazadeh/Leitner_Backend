from datetime import datetime
from app.extensions import db

class Words(db.Model):
    __tablename__ = 'verbs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(191), unique=True, nullable=False, index=True)
    category = db.Column(db.String(50))

class Translations(db.Model):
    __tablename__ = 'translations'
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    language = db.Column(db.String(10), nullable=False)
    meaning = db.Column(db.String(255), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('word_id', 'meaning', name='unique_word_meaning'),
    )


