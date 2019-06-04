from scrapy import Selector


def extract_content(text, selector):
    value = Selector(text=text).xpath(selector).extract()
    if value:
        return value[0]
    return ""

def extract_list(text, selector):
    value = Selector(text=text).xpath(selector).extract()
    return value
