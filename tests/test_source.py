import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        Test to determine whether the source class has been instaniated correctly
        '''

        self.assertEqual(self.new_source.id,"abc-news")
        self.assertEqual(self.new_source.name,"ABC News")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_source.url,"https://abcnews.go.com")
        self.assertEqual(self.new_source.category,"general")
        self.assertEqual(self.new_source.language,"en")
        self.assertEqual(self.new_source.country,"us")
