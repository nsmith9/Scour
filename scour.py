import urllib2
import re
import time
import socket
import xml.dom.minidom

print 'Starting Search'
url =" http://query.yahooapis.com/v1/public/yql?q=select%20abstract%2C%20clickurl%2C%20title%20from%20search.web%20where%20query%3D%20%22comment1%20OR%20comment2%20OR%20comment3%20OR%20comment4%20OR%20comment5%20OR%20comment6%20OR%20comment7%20OR%20comment8%20OR%20comment9%20OR%20comment0%22&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

spamList = []

request = urllib2.Request(url)

page = urllib2.urlopen(request)



print page.read()

