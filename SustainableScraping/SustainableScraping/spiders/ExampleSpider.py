import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://google.com']

    def parse(self, response):
        for things in response.css('input.'):
            yield {
                'category': things.css('morespecificspecifier').get(),
            }