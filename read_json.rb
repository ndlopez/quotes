#!/usr/bin/ruby
#reading a json file with ruby
#
require 'rubygems'
require 'json'

#get json string
str = File.read "data/goodreads_quotes.json"
obj = JSON.parse(str)

#rand Output
tot=obj["quotes"].length
i=rand 0..tot
#Output data
#puts obj.keys
puts obj["quotes"][i]["quote"]
puts obj["quotes"][i]["author"]
print i,"/",tot," -- ", obj["quotes"][i]["tags"], "\n"
