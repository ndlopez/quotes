#
# outputs one single randomly-selected quote
# scraped from goodreads.com
# using scrapy library 
# JSON data was cleaned using sed
# Must find a method to use pandas and clean data
#
import json
import random

i=0
#with open('data/science_quotes.json') as json_file:
with open('data/goodreads_quotes.json') as json_file:
    data = json.load(json_file)
    #for p in data['quotes']:
        #i = i+1
        #print('id:',i)
        #print('author:' + p['author'])
        #print('quote:' + p['quote'])
        #print('')
#print('quotes')
total=len(data['quotes'])
i=random.randint(0,total)
print(json.dumps(data['quotes'][i]['quote'],indent=4,sort_keys=True))
author=json.dumps(data['quotes'][i]['author'])
print('-- ',author.strip('\"'))
tag=json.dumps(data['quotes'][i]['tags'])
print(i,'-',tag.strip('\"'))

