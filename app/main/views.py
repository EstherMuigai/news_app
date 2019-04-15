from flask import render_template
from ..requests import get_articles
from . import main

# Views
@main.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles = articles)
