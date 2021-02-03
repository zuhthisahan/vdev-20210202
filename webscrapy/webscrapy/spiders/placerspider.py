import scrapy

class PlacerSpider(scrapy.Spider):
    name = 'placer'

    # create the function to get the information
    def start_requests(self):
        url = 'https://permits.placer.ca.gov/CitizenAccess/Default.aspx'

        yield scrapy.Request(url=url, callback=self.parse)

    