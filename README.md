# Scrape quotes from goodreads.com

Using `Scrapy`'s module on python3, scrape quotes from famous authors and display them on the terminal.

! I know there is a CLI available for Unix/Linux users (I think is called `fortune`), however on MacOS no such thing* (I don't use homebrew or any package manager). Therefore I created my own.

Sources: 
    
    tag_list=["friends","life","funny","science","computers"]
    for j in tag_list:
        https://www.goodreads.com/quotes/tag/tag_list[j]

## How to run

    $ scrapy crawl quotes -o goodreads_quotes.json

The generated JSON file has some unpleasant characters from the webpage, to clean them I used [sed](https://www.gnu.org/software/sed/).

To display(read) one randomly selected quote from the cleaned JSON file, Ruby is the perfect choice.

### About *goodread_quotes.json*:

The file format is:

<quote>,<author>,<topic>

I also added some quotes from the following book:<br>
"Astroparticle Physics" by Claus Grupen<br>
and some dialogues from The Simpsons

## How to add to Terminal.app:

Open $HOME/.profile with VIM and add the following line:

    ruby quotes/read_json.rb

Every time a new Terminal is open it will display a "randomly" selected quote, e.g.:

> Well, Mr. Frankel, who started this program, began to suffer from the computer disease that anybody who works with computers now knows about. It’s a very serious disease and it interferes completely with the work. The trouble with computers is you *play* with them. They are so wonderful. You have these switches - if it’s an even number you do this, if it’s an odd number you do that - and pretty soon you can do more and more elaborate things if you are clever enough, on one machine.<br>
> Richard P. Feynman<br>
> 95/195 -- computers
---

*Written in*: Python3, Ruby, and Shell<br>
*Environment*: MacOS 15.5<br>
*Editors*: VIM and Python 3.8's IDLE
