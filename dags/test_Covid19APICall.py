from unittest import TestCase
import unittest
from scraper import Scraper
from covid19apicall import Covid19APICall
from config import *


class TestCovid19APICall(TestCase):
    def test_get(self):
        scraper = Scraper(url)
        scraper.get()
        result = scraper.contents(tag=tag, tag_id_or_class=tag_id_or_class, tag_id_or_class_val=tag_id_or_class_val)
        covid19api = Covid19APICall(result[0][0])
        get_object = covid19api.get()
        self.assertTrue(get_object)

    def test_content(self):
        scraper = Scraper(url)
        scraper.get()
        result = scraper.contents(tag=tag, tag_id_or_class=tag_id_or_class, tag_id_or_class_val=tag_id_or_class_val)
        covid19api = Covid19APICall(result[0][3])
        get_object = covid19api.get()
        content = covid19api.content()
        print(content)
        self.assertTrue(content[1])


if __name__ == '__main__':
    unittest.main()