#!/usr/bin/python3
"""a script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """a function that returns HBNB
    """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def app_name():
    """a function that returns 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays c followed by value of text
    Replace '_' with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"c {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
