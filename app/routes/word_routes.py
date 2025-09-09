from flask import Blueprint, request, jsonify
from app.services.word_services import WordService

bp = Blueprint("words", __name__, url_prefix="/api/words")
service = WordService()

# Add a word (POST)
@bp.route("/add", methods=["POST"])
def add_word():
    data = request.json
    word = service.add_word(
        title=data["title"],
        category=data["category"],
        extra_data=data.get("extra_data"),
        example_data=data.get("example_data"),
        translations=data.get("translations")
    )
    return jsonify({"id": word.id, "title": word.title}), 201

# Get all words by category (GET)
@bp.route("/category/<category>", methods=["GET"])
def get_by_category(category):
    words = service.get_words_by_category(category)
    return jsonify([{"id": w.id, "title": w.title} for w in words])

# Search words by starting letters (GET)
@bp.route("/search", methods=["GET"])
def search_words():
    entry = request.args.get("entry")
    words = service.search_words(entry)
    return jsonify([{"id": w.id, "title": w.title} for w in words])