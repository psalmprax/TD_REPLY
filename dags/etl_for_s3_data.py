import logging
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
from config import *
from sqlalchemy import create_engine


class Etl:
    def __init__(self, links=None):
        """
        initializing the etl pipeline
        :param links: list of url links scrape from the website
        """
        LOG_FORMAT = "%(name)s : %(levelname)s - %(asctime)s - %(message)s"
        logging.basicConfig(filename="Scraper.log", level=logging.INFO, format=LOG_FORMAT, filemode="w")
        logging.info("__init__() function .................")
        self.logger = logging.getLogger()
        self.links = links
        self.engine = create_engine('postgresql+psycopg2://sourcedb:solution@localhost:5432/postgres')
        self.connection = None
        self.cursor = None
        self.file = None
        self.url = None

    @staticmethod
    def url_response(url):
        """
        This is a static method
        :param url: url used tot download the data set from s3
        :return: true or false if the operation is completed or not
        """
        try:
            logging.info("url_response() function start.................")
            r = requests.get(url, stream=True)
            filename = url.split("/")[-1]
            print(filename)
            with open(filename, 'wb') as f:
                for ch in r:
                    f.write(ch)
                f.close()
            logging.info("url_response() function finished.................")
            return True
        except Exception as ex:
            print(ex)
            logging.info("url_response() function finished................."+ex)
            return False

    @staticmethod
    def download(file):
        """
        Parallelize download is initialized from this function
        :param file: this is the url for parallelize download
        :return: true or false if the operation is completed or not
        """
        try:
            logging.info("download() function start.................")
            with ThreadPoolExecutor(max_workers=12) as executor:
                future = executor.submit(Etl.url_response, file)
                print(future.result())
            logging.info("download() function finished................."+ex)
            return True
        except Exception as ex:
            print(ex)
            logging.info("download() function error.................")
            return False

    @staticmethod
    def dbingest(file):
        """
        This is the process parallelization of ingesting downloaded file into the database
        :param file: name of the file to load into the database
        :return: true or false if the operation is completed or not
        """
        try:
            logging.info("dbingest() function start.................")
            with ThreadPoolExecutor(max_workers=12) as executor:
                future = executor.submit(Etl.ingest, file)
                print(future.result())
            logging.info("dbingest() function finished.................")
            return True
        except Exception as ex:
            print(ex)
            logging.info((ex))
            return False

    @staticmethod
    def ingest(file):
        """
        This is the process ingesting downloaded file into the database
        :param file: name of the file to load into the database
        :return: true or false if the operation is completed or not
        """
        try:
            logging.info("dbingest() function ingest.................")
            for df in pd.read_csv(file, compression='gzip', sep='\t', error_bad_lines=False, chunksize=10000,
                                  iterator=True):
                print(df.head(5))
                df.to_sql(file.split("/")[-1].split(".")[0], Etl().engine, if_exists='append', index=True)
            logging.info("dbingest() function finished.................")
            return True
        except Exception as ex:
            print(ex)
            logging.info("dbingest() function error................."+ex)
            return False

