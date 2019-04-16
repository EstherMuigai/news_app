from flask import render_template
from ..requests import get_articles,get_sources
from . import main
from .forms import SearchForm

# Views
@main.route('/main', methods = ['GET','POST'])
def index():
    articles = get_articles('kenya')
    headlines = get_articles('headlines')
    technology = get_articles('technology')
    sports = get_articles('sports')
    politics = get_articles('politics')
    entertainment = get_articles('entertainment')
    sources = get_sources()
    news = []
    form = SearchForm()
    search_item = form.search.data
    if form.validate_on_submit():
        news = []
        search_item = form.search.data
        news = get_articles(search_item)
    return render_template('index.html',news = news,search_form = form, articles = articles, sources = sources, headlines = headlines, technology = technology, sports = sports, politics = politics, entertainment =entertainment )