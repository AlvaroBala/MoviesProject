from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.movie import Movie

@app.route('/')
def index():
    return render_template("index.html")
