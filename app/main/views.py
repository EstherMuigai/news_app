from flask import render_template
from ..requests import get_articles,get_sources
from . import main
from .forms import SearchForm

# Views
@main.route('/',methods = ['GET','POST'])
def index():
    articles = get_articles('kenya')
    headlines = get_articles('headlines')
    technology = get_articles('technology')
    sports = get_articles('sports')
    politics = get_articles('politics')
    entertainment = get_articles('entertainment')
    sources = get_sources()
    form = SearchForm()
    search_item = form.search.data
    if form.validate_on_submit():
        new_search(search_item)
    return render_template('index.html',search_form = form, articles = articles, sources = sources, headlines = headlines, technology = technology, sports = sports, politics = politics, entertainment =entertainment )

@main.route('/searchnews')
def new_search(search_item):
    news = []
    news = get_articles(search_item)
    return render_template('searchnews.html', news = news)