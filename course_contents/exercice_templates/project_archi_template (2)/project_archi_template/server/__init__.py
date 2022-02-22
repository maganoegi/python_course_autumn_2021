
"""
A way provided by the Flask documentation for clean server file separation
by functionality.

SOURCE: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
"""
import flask

app = flask.Flask(__name__)

import server.views