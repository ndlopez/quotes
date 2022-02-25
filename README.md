# CLI app to Scrape quotes from goodreads.com

Using `Scrapy`'s module on python3, scrape quotes from famous authors and display them on the CLI.<br>
This project could have probably be done by using Shell and Python alone. But I wanted to learn about Scrapy, sometimes it's helpful.

! I know there is a CLI available for Unix/Linux users (called [`fortune`](https://en.wikipedia.org/wiki/Fortune_(Unix))), however on MacOS no such thing* (I don't use homebrew or any package manager). Therefore I created my own.

On *Goodreads.com* there are lots of quotes arranged in pages and can be filtered by author. The HTML page has the class **quoteText** for the quot and a span tag **authorOrTitle** for the author.

Scrapy requires a URI to make a request an scrap data, this is defined at the beginning of the code,<br>
    
    tag_list=["friends","life","funny","science","computers"]
    for j in tag_list:
        https://www.goodreads.com/quotes/tag/tag_list[j]
        
Here, Scrapy will search quotes from the Friends, Life, Funny, Science, and Computers tag of the source(GoodReads.com)

## Installation:
! Python3 with Scrapy and JSON modules should be already installed.

1. Run:

    $ scrapy crawl quotes -o output_json_file

The generated JSON file has some unpleasant characters from the webpage, such as *single quots, return chars, &ldquo;*, to clean them I used [sed](https://www.gnu.org/software/sed/).

2. Open $HOME/.profile with VIM and add the following line at the very end of the file:

    ruby quotes/read_json.rb

To display(read) one randomly selected quote from the cleaned JSON file, Ruby is the perfect choice, Python would perform equally.

3. Every time a new Terminal is open it will display a "randomly" selected quote, e.g.:

> Well, Mr. Frankel, who started this program, began to suffer from the computer disease that anybody who works with computers now knows about. It’s a very serious disease and it interferes completely with the work. The trouble with computers is you *play* with them. They are so wonderful. You have these switches - if it’s an even number you do this, if it’s an odd number you do that - and pretty soon you can do more and more elaborate things if you are clever enough, on one machine.<br>
> Richard P. Feynman<br>
> 95/195 -- computers

### About *output_json_file*:

The file format is:

    <quote>,<author>,<topic>

I also added some quotes from the following book:<br>
"Astroparticle Physics" by Claus Grupen<br>
and some dialogues/quotes from The Simpsons (No copyright infringement intended)

---

*Languages*: Python3, Ruby, and Shell<br>
*Environment*: MacBookPro/MacOS 15.5<br>
*Editors*: VIM and Python 3.8's IDLE
