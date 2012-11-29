import unittest
import codecs
from url_util import is_valid_url

class TestValidUrls(unittest.TestCase):

    def setUp(self):
        f = codecs.open('./urls_valid.txt', encoding='utf-8', mode='r')
        self.URLS = [line.strip() for line in f.readlines()]
        f.close()

    def test_all_valid(self):
        for url in self.URLS:
            self.assertTrue(is_valid_url(url), msg=u"Failed URL: {0}".format(url))

class TestInvalidUrls(unittest.TestCase):

    def setUp(self):
        f = codecs.open('./urls_invalid.txt', encoding='utf-8', mode='r')
        self.URLS = [line.strip() for line in f.readlines()]
        f.close()

    def test_all_invalid(self):
        for url in self.URLS:
            self.assertFalse(is_valid_url(url), \
                             msg=u"Failed URL: {0}".format(url))


if __name__ == '__main__':
    unittest.main()
