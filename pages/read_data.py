#
# reads a JSON file, scraped from goodreads.com
# using curl, grep, cut commands 
# It outputs one single
# randomly selected quote
# pls. add say -v Samantha when running
#
import json
import random

i=0
with open('/Users/diego/Public/science_quotes.json') as json_file:
    data = json.load(json_file)
    #for p in data['quotes']:
        #i = random.randint(0,28)
        #print('id:',i)
        #print('author:' + p['author'])
        #print('quote:' + p['quote'])
        #print('')
#print('quotes')
#print('quote_id',i)
total=len(data['quotes'])
i = random.randint(0,total)

print(json.dumps(data['quotes'][i]['quote'],indent=4,sort_keys=True))
print('-- ',json.dumps(data['quotes'][i]['author']))
