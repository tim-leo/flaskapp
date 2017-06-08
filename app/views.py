from flask import render_template
from app import app
import json


@app.route('/')
@app.route('/index')
def index():
    """Creates an array with random names."""
    user = {'nickname': 'big'}

    posts = []

    i = 1
    while i < 20:
        posts.append({
            'author': {'nickname': 'Person' + str(i)},
            'body': 'some message about weenies' + str(i)
        })
        i += 1
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/validusers')
def validusers():
    """Creates an array with random names."""

    return render_template('validusers.html', title='Users')
