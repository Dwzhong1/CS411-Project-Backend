from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'David'}
    return render_template('index.html',title='Home', user=user)


