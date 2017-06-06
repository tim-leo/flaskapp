from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():

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
