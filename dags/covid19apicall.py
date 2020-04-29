import requests
import logging


class Covid19APICall:
    def __init__(self, api_url):
        """
        initialize url with url for api request call
        :type api_url: string
        """
        # create and configure logger
        LOG_FORMAT = "%(name)s : %(levelname)s - %(asctime)s - %(message)s"
        logging.basicConfig(filename="Scraper.log", level=logging.INFO, format=LOG_FORMAT, filemode="w")
        logging.info("Initialization.................")
        self.logger = logging.getLogger()
        self.url = api_url
        self.request = None
        self.success = False

    def get(self):
        """
        get() the data from the url call into self.request
        and set self.success to True or False
        :return: self.success => True or False
        """
        try:
            logging.info("get() function start.................")
            self.request = requests.get(self.url)
            if self.request:
                self.success = True
            logging.info("get() function finished.................")
        except Exception as ex:
            print(ex)
            self.success = False
            logging.info("get() function error................." + ex)
        return self.success

    def content(self):
        """
        return the result of the self.request call
        :return: self.request.text => json data,self.success => True or False
        """
        logging.info("content() function finished.................")
        return self.request.text, self.success
