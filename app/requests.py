import urllib.request,json
from .models import Article
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_articles():
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = base_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if title:
            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results

