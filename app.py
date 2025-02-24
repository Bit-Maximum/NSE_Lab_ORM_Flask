from flask import Flask


app = Flask(__name__, static_folder="statics")

if __name__ == "__main__":
    app.run(debug=True)

from structures.views import index
