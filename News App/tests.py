import application
import unittest


class CheckRequests(unittest.TestCase):

    def test_bbc_request_is_working(self):
        bbc = "https://www.bbc.com"
        self.assertEqual(bbc, application.bbc), "The application's bbc source is not the same as https://www.bbc.com"
        response = application.requests.get(bbc)
        self.assertEqual(200, response.status_code), "The bbc page's response is not 200"

    def test_nbc_request_is_working(self):
        nbc = "https://www.nbcnews.com/latest-stories/"
        self.assertEqual(nbc, application.nbc), "The application's nbc source is not the same as https://www.nbcnews.com/latest-stories/"
        response = application.requests.get(nbc)
        self.assertEqual(200, response.status_code), "The nbc page's response is not 200"

    def test_fox_request_is_working(self):
        fox = "https://www.foxnews.com/"
        self.assertEqual(fox, application.fox), "The application's fox source is not the same as https://www.foxnews.com/"
        response = application.requests.get(fox)
        self.assertEqual(200, response.status_code), "The fox page's response is not 200"

    def test_protv_request_is_working(self):
        protv = "https://stirileprotv.ro/"
        self.assertEqual(protv, application.protv), "The application's protv source is not the same as https://stirileprotv.ro/"
        response = application.requests.get(protv)
        self.assertEqual(200, response.status_code), "The protv page's response is not 200"

    def test_digi24_request_is_working(self):
        digi24 = "https://www.digi24.ro/"
        self.assertEqual(digi24, application.digi24), "The application's digi24 source is not the same as https://www.digi24.ro/"
        response = application.requests.get(digi24)
        self.assertEqual(200, response.status_code), "The digi24 page's response is not 200"


class CheckHeader(unittest.TestCase):

    def test_header_initialization_is_working(self):
        title = "Example title"
        link = "Example href"
        bonus_attribute = "Bonus"
        test_header = application.Header(title, link, bonus_attribute)
        assert isinstance(test_header, application.Header), "Could not instantiate Header object"
        self.assertEqual(test_header.text, title), "Wrong value for the text attribute"
        self.assertEqual(test_header[0], title), "Title not stored in list"
        self.assertEqual(test_header.href, link), "Wrong value for the href attribute"
        self.assertEqual(test_header[0], title), "Link not stored in list"
        self.assertEqual(test_header[2], bonus_attribute), "Bonus attribute not stored in a list"


class CheckNews(unittest.TestCase):

    def test_news_initialization_is_working(self):
        header1 = application.Header("Example news 1", "Example link 1")
        header2 = application.Header("Example news 2", "Example link 2")
        news_object = application.News()
        news_object += header1
        news_object += header2
        assert isinstance(news_object, application.News), "Could not instantiate News object"
        self.assertEqual(news_object[0], header1), "Operator overloading not working as expected"

    def test_bbc_get_news_generator(self):
        bbc_generator = application.Bbc.get_news()
        test_header = next(bbc_generator)
        assert isinstance(test_header, application.Header), "BBC Generator did not return a Header"

    def test_nbc_get_news_generator(self):
        nbc_generator = application.Nbc.get_news()
        test_header = next(nbc_generator)
        assert isinstance(test_header, application.Header), "NBC Generator did not return a Header"

    def test_fox_get_news_generator(self):
        fox_generator = application.Fox.get_news()
        test_header = next(fox_generator)
        assert isinstance(test_header, application.Header), "FOX Generator did not return a Header"

    def test_protv_get_news_generator(self):
        protv_generator = application.Protv.get_news()
        test_header = next(protv_generator)
        assert isinstance(test_header, application.Header), "PROTV Generator did not return a Header"

    def test_digi24_get_news_generator(self):
        digi24_generator = application.Digi24.get_news()
        test_header = next(digi24_generator)
        assert isinstance(test_header, application.Header), "DIGI24 Generator did not return a Header"


class CheckMixin(unittest.TestCase):

    def test_get_first_x_news_method(self):
        bbc_test = application.Bbc()
        bbc_test = bbc_test.get_first_x_news(2)
        assert isinstance(bbc_test, application.Bbc), "Get_first_x_news method returned a different object"
        assert isinstance(bbc_test[0], application.Header), "The returned objects from get_first_x_news are not Headers"
        nbc_test = application.Nbc()
        nbc_test = nbc_test.get_first_x_news(2)
        assert isinstance(nbc_test, application.Nbc), "Get_first_x_news method returned a different object"
        assert isinstance(nbc_test[0], application.Header), "The returned objects from get_first_x_news are not Headers"


unittest.main()
