import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    '''def start_request(self):
        urls=['https://www.goodreads.com/quotes/tag/science','https://www.goodreads.com/quotes/tag/science?page=2']
        for myurl in urls:
            yield scrapy.Request(url=myurl,callback=self.parse)'''
    start_urls=['https://www.goodreads.com/quotes/tag/science',
                'https://www.goodreads.com/quotes/tag/science?page=2',]


    def parse(self,response):
        '''page=response.url.split("/")[-2]
        filename='quotes-%s.html' %page
        with open(filename,'wb') as file:
            file.write(response.body)
        self.log('Saved file %s' % filename)'''
        for quot in response.css('div.quoteText'):
            yield{
                'text':quot.css('quoteText::text').get(),
                'author':quot.css('span.authorOrTitle::text').get(),
                }
