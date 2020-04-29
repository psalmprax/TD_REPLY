import os
import time
from multiprocessing.dummy import Pool

import glob2
from config import *
from etl_for_s3_data import Etl
from scraper import Scraper

if __name__ == "__main__":
    scraper = Scraper(url_etl)
    scraper.get()
    result = scraper.contents()
    etl = Etl(result[0])
    start = time.time()

    links = list(x for x in result[0][4:] if x.startswith("https"))
    r = Pool(len(links[:3])).map(Etl.url_response, links[:3])

    file = [file for file in glob2.glob(os.getcwd() + '/*tsv.gz')]
    r = Pool(len(file)).map(Etl.dbingest, file)

    print(f"Time to download: {time.time() - start}")