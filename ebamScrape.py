'''
Attempting to scrape top search results from amazon and ebay to find best deal
'''

from bs4 import BeautifulSoup
import urllib
import Tkinter as tk
import webbrowser
import mechanize
import cookielib

def amazon(item):
	#create browser object
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	br.set_handle_robots(False) #no robots
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	response = br.open("http://www.amazon.com")

	br.select_form("site-search")

	control = br.form.find_control("field-keywords")
	control.value = item

	response = br.submit();

	soup = BeautifulSoup(response, "lxml")
	items = soup.find_all("li", class_="s-result-item")

	print items[0]


item = raw_input('Enter item to search: ')

amazon(item)