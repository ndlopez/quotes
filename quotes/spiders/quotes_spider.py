# <quotes_spider.py>
# ! do NOT change the name of this file.
#
# scrape quotes from www.goodreads.com and
# store them in a JSON file.
# ! as long as the website does not change
# the HTML elements and CSS classes,
# it will run just ok. Otherwise review page.
# run like:
# $ scrapy crawl quotes -o goodreads_quotes.json 
# !! pls, change the name of output json file
# scrapy will append data to the same file.
#
import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    #change here the urls to be scraped
    start_urls=[
        'https://www.goodreads.com/quotes/tag/friends',
        'https://www.goodreads.com/quotes/tag/life',
        'https://www.goodreads.com/quotes/tag/funny',
        'https://www.goodreads.com/quotes/tag/science',
        'https://www.goodreads.com/quotes/tag/computers',
	'https://www.goodreads.com/author/quotes/466.Jon_Stewart',
]
    #start_urls0=['https://www.goodreads.com/quotes/tag/science',
    #            'https://www.goodreads.com/quotes/tag/science?page=2',]
    def parse(self,response):
        for quote in response.css('div.quoteText'):
            tags = response.url.split("/")[-1]
            yield{
                'quote':quote.css('div.quoteText::text').get(),
                'author':quote.css('span.authorOrTitle::text').get(),
                'tags':tags,
                #quote.css('div.quoteFooter div.greyText a').attrib['href'].get(),
                }
