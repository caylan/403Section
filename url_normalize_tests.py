import unittest
from url_util import normalize_url

class TestNormalization(unittest.TestCase):

    def test_case(self):
        self.assertEquals("http://www.google.com/", \
                normalize_url("http://www.GooGLE.com/"))

    def test_empty_fragment(self):
        self.assertEquals("http://wiki.foo.com/", \
                normalize_url("http://wiki.foo.com/#"))

    def test_non_empty_fragment(self):
        self.assertEquals("http://wiki.foo.com/", \
                normalize_url("http://wiki.foo.com/#FragMentOMatic"))

    def test_preserved_path_case(self):
        self.assertEquals("http://wiki.foo.com/Test/CaSiNg/", \
                normalize_url("http://wiki.foo.com/Test/CaSiNg/"))

    def test_trailing_slash(self):
        self.assertEquals("http://aa.com/", \
                normalize_url("http://aa.com"))
    
    def test_removing_params(self):
        self.assertEquals("http://www.google.com/",
                normalize_url("http://www.google.com/?q=cow&search=something"))

if __name__ == '__main__':
    unittest.main()
