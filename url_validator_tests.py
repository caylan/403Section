import unittest
import codecs
from url_validator import validate

class TestValidUrls(unittest.TestCase):

    def setUp(self):
        f = codecs.open('./urls_valid.txt', encoding='utf-8', mode='r')
        self.URLS = [line.strip() for line in f.readlines()]
        f.close()

    def test_all_valid(self):
        for url in self.URLS:
            self.assertTrue(validate(url), msg=u"Failed URL: {0}".format(url))

if __name__ == '__main__':
    unittest.main()
