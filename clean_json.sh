#!/bin/bash
#Scraped data contains lots of unpleasant data
#First replace "\n" with empty space
#Next, replace "u201c" with empty space
#delete \ from file

in_file=data/goodreads_quotes.json
sed -i -e 's/\\n//g' ${in_file}
sed -i -e 's/u201c//g' ${in_file}
sed -i -e 's/u201dn  //g' ${in_file}
sed -i -e 's/\\u201d\\n  //g' ${in_file}
