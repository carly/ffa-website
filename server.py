"""Freedom For All server"""

#imports - standard lib
import os

#imports - flask
from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

#app config
app = Flask(__name__)

app.secret_key="""FFA"""
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("home.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
	
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    print "\n\n\nYO\n\n\n"
    app.run()

