#get the author
grep -w -A 1 "authorOrTitle" science_quotes.html | cut -f2 -d'>' > author_science.quotes
#get one quote
grep -m1 -w -A 1 "ldquo" science_quotes.html | cut -f2 -d'&' | cut -f2 -f3 -d';'
#grep all quotes
grep -w -A 1 "ldquo" science_quotes.html | cut -f2 -f3 -d';' | cut -f1 -d'&' > science_text.quotes