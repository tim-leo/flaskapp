#!flask/scripts/python

from app import app
from flask import Flask
from flask_wtf import FlaskForm
app.run(debug=True)
