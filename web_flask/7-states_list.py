#!/usr/bin/python3
"""a script that starts a flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """lists all of the states objects present in DBstorage
    """
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda a: a.name)  # sort by A-Z
    return render_template("7-states_list.html", states=all_states)


@app.teardown_appcontext
def close():
    """close SQLAlchemy sesion"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
