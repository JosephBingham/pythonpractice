#!/usr/bin/python
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards'
#opens page
uClient = uReq(my_url)
#reads html
page_html = uClient.read()

uClient.close()
#html parsing
page_soup = soup(page_html, "html.parser")

#gets thing in h1 tag
#print page_soup.h1


#grabs each product, gives raw html code 
containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
		#goes to div      goes to a tag
	brand = container.div.div.a.img["title"]
		#	      ^goes to div
	#getting atrs of stuff
	title = container.findAll("a", {"class":"item-title"}
	name = title[0].text
	price_contain = container.findAll("li", {"class":"price-ship"})
	price = price_contain[0].text.strip()
	print "{}, {}, {}".format(brand, name, price)
	print brand

