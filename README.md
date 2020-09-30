# Scrape quotes from goodreads.com

Using `Scrapy`'s module on python3, scrape quotes from famous authors and display them on the terminal.

! I know there is a CLI available for Unix/Linux users, however on MacOS no such thing. Therefore I created my own.

Sources: 
    
    tag_list=["friends","life","funny","science","computers"]
    for j in tag_list:
        https://www.goodreads.com/quotes/tag/tag_list[j]

The generated JSON file has some unpleasant characters, probably from the webpage, to clean it I used `sed`.

To display(read) one randomly selected quote from the generated JSON file, Ruby is the perfect choice.

## How to run

    $ scrapy crawl quotes -o goodreads_quotes.json

About *goodread_quotes.json*:

I added some extra quotes from the following book:<br>
"Astroparticle Physics" by Claus Grupen<br>
and some dialogues from The Simpsons

### To add to Terminal.app:

Open $HOME/.profile with VIM or nano and add the following line:

    ruby quotes/read_json.rb

Every time a new Terminal is open it will display a "randomly" selected quote:

> Well, Mr. Frankel, who started this program, began to suffer from the computer disease that anybody who works with computers now knows about. It’s a very serious disease and it interferes completely with the work. The trouble with computers is you *play* with them. They are so wonderful. You have these switches - if it’s an even number you do this, if it’s an odd number you do that - and pretty soon you can do more and more elaborate things if you are clever enough, on one machine.<br>
> Richard P. Feynman<br>
> 95/195 -- computers
---
*Written in*: Python3, Ruby, and Shell
*Environment*: MacOS15.5/MacBookPro
*Editors*: VIM and Python3.8's IDLE
