import scrapy

class PlacerSpider(scrapy.Spider):
    name = 'placer'

    # create the function to get the information
    def start_requests(self):
        url = 'https://permits.placer.ca.gov/CitizenAccess/Default.aspx'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            # get the Permit number
            'Permit Number' : response.css('div.rec-left h1 span#ctl00_PlaceHolderMain_lblPermitNumber::text').get(),
            'Applicant Name' :  response.css('span.contactinfo_businessname::text').get(),
            'Work Place' :  response.css('.NotBreakWord::text').get(),

        }