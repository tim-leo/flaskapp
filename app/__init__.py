from flask import Flask

app = Flask(__name__)
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

app.config.from_object('config')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from app import views
