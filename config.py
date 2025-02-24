from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///structure.db"
db = SQLAlchemy(app)
