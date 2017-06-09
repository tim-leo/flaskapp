#!flask/scripts/python

from app import app
from flask import Flask

app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
