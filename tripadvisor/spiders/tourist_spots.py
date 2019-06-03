import scrapy
from tripadvisor.utils.extractors import extract_content, extract_list


class TouristSpotsSpider(scrapy.Spider):
    name = "tourist_spots"
    start_urls = ["https://www.tripadvisor.com.br/Attractions-g303631-Activities-c47-Sao_Paulo_State_of_Sao_Paulo.html"]

    def parse(self, response):

        selector_raw = "//*[@id='FILTERED_LIST']//div[@class='listing_details']"

        selector_title = "//div[@class='listing_title ']/a/text()"
        selector_image = "//a[@class='photo_link ']/img[@class='photo_image']/@src"

        for i, raw in enumerate(extract_list(response.body_as_unicode(), selector_raw)):
            title = extract_content(raw, selector_title)
            image = extract_content(raw, selector_image)

            import ipdb; ipdb.set_trace()
            print(title, image)
            print("----------------------------------------------")