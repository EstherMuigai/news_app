from flask import render_template
from ..requests import get_articles,get_sources
from . import main

# Views
@main.route('/')
def index():
    articles = get_articles('kenya')
    sources = get_sources()
    return render_template('index.html', articles = articles, sources = sources)

