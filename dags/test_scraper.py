from unittest import TestCase
import unittest
from scraper import Scraper
from config import *


class TestScraper(TestCase):
    def test_get(self):
        scraper = Scraper(url)
        self.assertTrue(scraper.get())

    def test_contents(self):
        scraper = Scraper(url)
        scraper.get()
        result = scraper.contents(tag=tag, tag_id_or_class=tag_id_or_class, tag_id_or_class_val=tag_id_or_class_val)
        print(result)
        self.assertTrue(result[1])


if __name__ == '__main__':
    unittest.main()
