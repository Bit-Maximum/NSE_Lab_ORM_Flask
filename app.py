from flask import Flask
from config import db

app = Flask(__name__, static_folder="statics")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///structure.db"
db.init_app(app)

from structures.views import views_bp

app.register_blueprint(views_bp)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
