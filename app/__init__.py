from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/test', methods=['GET'])
    def test_api():
        return jsonify({
    "id": 1,
    "category": "verb",
    "title": "verstehen",
    "translation": "to understand",
    "usage": [
        "<also: trans., acc.> etwas begreifen, nachvollziehen, interpretieren, erfassen",
        "<sich+A> sich miteinander gut verstehen, harmonieren",
        "<also: mit dat.> klarkommen mit, sich verständigen, sich auskennen"
    ],
    "examples": [
        "Ich verstehe, was du meinst.",
        "Er hat endlich verstanden, wie die Maschine funktioniert."
    ],
    "usageRate": 0.8,
    "photos": ["/img/verstehen.jpg"],
    "nominal": "das Verstehen"

        })

    return app