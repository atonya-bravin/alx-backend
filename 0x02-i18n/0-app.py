#!/usr/bin/env python3
"""
This is a flass application that renders the index.html page
"""


from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """
    function that takes action when rendering
    """
    return render_template("index.html")
