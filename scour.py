import urllib2
import re
import time
import socket
import elementtree.ElementTree

#
#

rssOut = open('/home/nix/Desktop/Scour/rss', 'r+')

print 'Starting Search'
url = "http://query.yahooapis.com/v1/public/yql?q=select%20abstract%2C%20clickurl%2C%20title%2C%20date%20from%20search.web(50)%20where%20query%3D%20%22comment1%20OR%20comment2%20OR%20comment3%20OR%20comment4%20OR%20comment5%20OR%20comment6%20OR%20comment7%20OR%20comment8%20OR%20comment9%20OR%20comment0%22%20%7C%20sort(field%3D%22date%22%2C%20descending%3D%22true%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

spamList = []

request = urllib2.Request(url)

page = urllib2.urlopen(request)

rawXML = page.read()

#decided to turn raw XML into RSS manually
#minidom was slow & ET gives IOERROR36

#removes yahoo yql & adds RSS metadata 
rawXMLa = rawXML[:rawXML.find("<query")]
rawXMLb = "<rss version='2.0'>"
rawXMLc = rawXML[(rawXML.find("<results")):(rawXML.find("/results>"))+9:1]

xml1 = rawXMLa+rawXMLb+rawXMLc+'</rss>'

xml1a = xml1[:xml1.find("s>")+2]
xml1b = xml1[xml1.find("<result "):]

rssMetaData = '<title>Scour</title> <description>This is an example of an RSS feed from Scour. Feeds can deliver lists of spam, malicious URLs, and distribution URLs.</description> <link>http://developer.yahoo.com/hacku/gt.html</link> <lastBuildDate>time.localtime</lastBuildDate> <pubDate>time.gmtime</pubDate>'

xml2 = xml1a+rssMetaData+xml1b

#finds & replaces all Yahoo tags with corresponding RSS tags

xml2 = xml2.replace("results","channel")
xml2 = xml2.replace("result","item")
xml2 = xml2.replace("clickurl","link")
xml2 = xml2.replace("abstract","description")

#removes default XML namespace
xml2 = xml2.replace('xmlns="http://www.inktomi.com/"',"")

rssOut.write(xml2)

rssOut.flush()
rssOut.close()
