import sys
import time
from selenium import webdriver
from tripadvisor.utils.extractors import extract_content, extract_list
from tripadvisor.utils.selectors import *

class CrawlerTripadvisor(object):

    def __init__(self, url):
        self.HOME = "https://www.tripadvisor.com.br"
        self.current_page = 1

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.filename = "results.csv"

        print("\n{}\n".format(url))

    def parse(self):

        time.sleep(2)

        print("\nPage ==> {}\n".format(self.current_page))

        f = open(self.filename, "ab")

        for raw in extract_list(self.driver.page_source.encode("utf-8"), selector_raw):
            title = extract_content(raw, selector_title)
            link = self.HOME + extract_content(raw, selector_link)
            image = extract_content(raw, selector_image)
            string = "{};{};{}\n".format(title, link, image)
            f.write(string.encode())

        f.close()
        self.current_page += 1

        if self.current_page > 1:
            try:
                next_page = self.driver.find_element_by_xpath(selector_page.replace("|V|", str(self.current_page)))
                next_page.click()
                time.sleep(2)
                self.parse()
            except:
                print("\nFim da paginacao\n")

        self.driver.quit()

if len(sys.argv) < 2:
    print("\nERRO: URL is required\n")
else:
    url = sys.argv[1].strip()
    crawler = CrawlerTripadvisor(url)
    crawler.parse()