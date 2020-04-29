from scraper import Scraper
from config import *

if __name__ == "__main__":
    scraper = Scraper(url)
    scraper.get()
    result = scraper.contents(tag=tag, tag_id_or_class=tag_id_or_class, tag_id_or_class_val=tag_id_or_class_val)
    print(result)
