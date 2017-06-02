from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'big'}
    posts = [ #fake stuff
        {
            'author': {'nickname': 'Weenie'},
            'body': 'lel i like nuts'
        },
        {
            'author': {'nickname': 'Hut jr.'},
            'body': 'pls give me more salt'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
