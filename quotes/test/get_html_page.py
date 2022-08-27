import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"

    def start_requests(self):
        urls=['https://www.goodreads.com/quotes/tag/science',
                'https://www.goodreads.com/quotes/tag/science?page=2',]
        for myurl in urls:
            yield scrapy.Request(url=myurl, callback=self.parse)
    def parse(self, response):
        page= response.url.split("/")[-1]
        filename= 'quotes-%s.html' % page
        with open(filename,'wb') as myfile:
            myfile.write(response.body)
        self.log('Saved file %s' % filename)
