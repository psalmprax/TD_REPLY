import logging
import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Scraper:
    def __init__(self, url):
        """
        This is a Scraper class for web scrapping. the url argument is passed
        and the selenium package with the webdriver extension is used. This is
        the __init__ point of entry for the Scraper class
        :param url:
        """
        # create and configure logger
        LOG_FORMAT = "%(name)s : %(levelname)s - %(asctime)s - %(message)s"
        logging.basicConfig(filename="Scraper.log", level=logging.DEBUG, format=LOG_FORMAT, filemode="w")
        self.logger = logging.getLogger()
        self.url = url
        self.soup = None
        self.Options = Options()
        self.Options.headless = True
        self.browser = webdriver.Firefox(options=self.Options)
        self.content = list()
        self.source = None
        self.success = False

    def get(self):
        """
        the get(9 function get the scraped webpage and set the self.soup
        with returned BeautifulSoup Object
        :return: self.success => True or False
        """
        try:
            self.browser.get(self.url)
            time.sleep(1)
            self.source = self.browser
            self.soup = BeautifulSoup(self.source.page_source, 'html.parser')
            self.source.minimize_window()
            self.browser.stop_client()
            self.browser.close()
            self.success = True
        except Exception as ex:
            print(ex)
            self.success = False
        return self.success

    def contents(self, tag=None, tag_id_or_class=None, tag_id_or_class_val=None):
        """
        return the content of Beautiful soup in list data format
        :param tag: i.e <div>
        :param tag_id_or_class: i.e class or id
        :param tag_id_or_class_val: i.e id = "url"
        :return: self.content => list(data),self.success => True or False
        """

        try:
            for item in self.soup.findAll(tag, attrs={tag_id_or_class: tag_id_or_class_val}):
                self.content.append(item.text)

            if self.content:
                self.success = True
            if tag is None:
                self.content = self.content[-1].split("\n")

        except Exception as ex:
            print(ex)
            self.success = False
        return self.content, self.success
