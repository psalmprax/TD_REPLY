from multiprocessing.dummy import Pool
from unittest import TestCase
import unittest
from etl_for_s3_data import Etl
from scraper import Scraper
from config import *
import glob2
import os


class TestEtl(TestCase):
    def test_url_response(self):
        scraper = Scraper(url_etl)
        scraper.get()
        result = scraper.contents()
        links = list(x for x in result[0][4:] if x.startswith("https"))
        print(links[:3])
        r = Pool(len(links[:3])).map(Etl.url_response, links[:3])
        self.assertTrue(set(r).pop())

    def test_download(self):
        scraper = Scraper(url_etl)
        scraper.get()
        result = scraper.contents()
        links = list(x for x in result[0][4:] if x.startswith("https"))
        print(links[:3])
        r = Pool(len(links[:3])).map(Etl.download, links[:3])
        self.assertTrue(set(r).pop())

    def test_dbingest(self):
        scraper = Scraper(url_etl)
        scraper.get()
        result = scraper.contents()
        links = list(x for x in result[0][4:] if x.startswith("https"))
        print(links[:3])
        r = Pool(len(links[:3])).map(Etl.url_response, links[:3])
        files = [file for file in glob2.glob(os.getcwd() + '/*tsv.gz')]
        r = Pool(len(files)).map(Etl.dbingest, files)
        self.assertTrue(set(r).pop())

    def test_ingest(self):
        scraper = Scraper(url_etl)
        scraper.get()
        result = scraper.contents()
        links = list(x for x in result[0][4:] if x.startswith("https"))
        print(links[:3])
        r = Pool(len(links[:3])).map(Etl.url_response, links[:3])
        files = [file for file in glob2.glob(os.getcwd() + '/*tsv.gz')]
        r = Pool(len(files)).map(Etl.ingest, files)
        self.assertTrue(set(r).pop())


if __name__ == '__main__':
    unittest.main()
