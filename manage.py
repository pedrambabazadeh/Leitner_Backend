# manage.py
# Entry for Flask CLI (flask run, flask db ...)
from app import create_app
from app.extensions import db
from app.models import *  # so Alembic sees all models

app = create_app()