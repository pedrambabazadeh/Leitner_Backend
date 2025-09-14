
#read after DB first api carefully to initialize routes file and reform directory etc.


from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from app.extensions import db, migrate, jwt
from app.config import Config
from .routes import word_bp
import os

#read after DB first api carefully to initialize routes file and reform directory etc.

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(word_bp)
    jwt.init_app(app)

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