import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article =("Crystal Bell","BTS And Halsey Kick Off Summer Early With 'Boy With Luv' - MTV.com", "Oh my my my oh my my my' prepare to have this song stuck in your head","http://www.mtv.com/news/3120451/bts-halsey-boy-with-luv-video/","https://mtv.mtvnimages.com/uri/mgid:ao:image:mtv.com:671751?quality=0.8&format=jpg&width=1440&height=810&.jpg","2019-04-12T10:55:00Z","Five years ago, BTS were a group of young adults in their teens and early twenties trying to make sense of the world around them. They channeled these confusing coming-of-age emotions and experiences like first love, disappointment, and heartbreak into their...","source.name: MTV News"})

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test to determine whether the article class has been instaniated correctly
        '''

        self.assertEqual(self.new_article.author,"Crystal Bell")
        self.assertEqual(self.new_article.title,"BTS And Halsey Kick Off Summer Early With 'Boy With Luv' - MTV.com")
        self.assertEqual(self.new_article.description,"Oh my my my oh my my my' prepare to have this song stuck in your head")
        self.assertEqual(self.new_article.url,"http://www.mtv.com/news/3120451/bts-halsey-boy-with-luv-video/")
        self.assertEqual(self.new_article.urlToImage,"https://mtv.mtvnimages.com/uri/mgid:ao:image:mtv.com:671751?quality=0.8&format=jpg&width=1440&height=810&.jpg")
        self.assertEqual(self.new_article.publishedAt,"2019-04-12T10:55:00Z")
        self.assertEqual(self.new_article.content,"Five years ago, BTS were a group of young adults in their teens and early twenties trying to make sense of the world around them. They channeled these confusing coming-of-age emotions and experiences like first love, disappointment, and heartbreak into their...")
        self.assertEqual(self.new_article.source.name,"source.name: MTV News"})

if __name__ == '__main__':
    unittest.main()