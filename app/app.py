# from flask import Flask
#
# app = Flask(__name__)
# app.config.from_object('config')
# # @app.route('/')
# # @app.route('/index')
# # def index():
# #     """Creates an array with random names."""
# #     user = {'nickname': 'big'}
# #
# #     posts = []
# #
# #     i = 1
# #     while i < 20:
# #         posts.append({
# #             'author': {'nickname': 'Person' + str(i)},
# #             'body': 'some message about weenies' + str(i)
# #         })
# #         i += 1
# #     return render_template('index.html', title='Home', user=user, posts=posts)
# #
# #
# # @app.route('/validusers')
# # def validusers():
# #     """Creates an array with random names."""
# #
# #     return render_template('validusers.html', title='Users')
# #
# # if __name__ == '__main__':
# #     # app.run(host='0.0.0.0', port=5000, debug=True)
# #     app.run(host='0.0.0.0')
#
# from app import views

from flask import Flask, render_template
from app import app
import json

app = Flask(__name__)
print('we got here')
@app.route('/')
@app.route('/index')
def index():
    """Creates an array with random names."""
    user = {'nickname': 'big'}
    print('we got here 2')
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
