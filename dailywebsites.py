'''
This script webscrapes hypem.com and theberrics.com for todays most popular songs and todays new articles then displays them in a window
and allows the user to double click on the info to open it in the webbrowser
I made this so I could view all the websites I visit daily in one location at one time.
'''
from bs4 import BeautifulSoup
import urllib
import Tkinter as tk
import webbrowser
import mechanize

#gets the links and info from hypem.com
def hypem(app):
	#will store all track info from website
	track_names = []

	#gets track info from website
	for i in range(1,4):
		r = urllib.urlopen('http://hypem.com/popular/' + str(i)).read()
		soup = BeautifulSoup(r, "lxml")
		track_names.extend(soup.find_all("h3", class_="track_name"))

	#stores all <a> tags
	atags = []

	#stores links to songs
	links = []

	#get all <a> tags for names/artists
	for t in track_names:
		atags.append(t.find_all("a"))

	#get links to songs
	for t in track_names:
		links.append(t.find("a", class_="track")['href'])

	#make strings of track names/artists and put in list
	tracks = []
	for x in atags:
		s = ""
		for y in x:
			s= s + y.get_text()
		tracks.append(s.replace("\n", ": "))

	#will open tab in browser with song link
	def internet(index):
		webbrowser.open_new_tab("http://www.hypem.com/" + links[index])

	#when double clicked calls this method to get selection and open tab
	def clicked(event):
		widget = event.widget
		selection=widget.curselection()
		internet(selection[0])
	scrollbar = tk.Scrollbar(app, orient="vertical")
	lb = tk.Listbox(app, width=50, height=20, yscrollcommand=scrollbar.set)
	lb.bind("<Double-Button-1>" , clicked)
	scrollbar.config(command=lb.yview)

	scrollbar.pack(side="right", fill="y")
	lb.pack(side="left",fill="both", expand=True)
	for t in tracks:
		lb.insert("end", str(tracks.index(t)+1) + ".\t"+t)

#gets the links and info from theberrics.com
def berrics(app):
	#use mechanize to simulate browser because website guards against accessing in certain ways
	#create browser object
	br = mechanize.Browser()
	br.set_handle_robots(False) #no robots
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	#open the webpage
	response = br.open("http://www.theberrics.com/dailyops")

	#get the video names
	soup = BeautifulSoup(response, "lxml")
	video = soup.find_all("div", class_="title-details")

	#stores video names
	video_names = []

	#stores link to video
	links = []

	for v in video:
		video_names.append(v.find("h2").get_text() + " - " + v.find("h3").get_text())
		links.append(v.find("a")['href'])

	#will open tab in browser with song link
	def internet(index):
		webbrowser.open_new_tab(links[index])

	#when double clicked calls this method to get selection and open tab
	def clicked(event):
		widget = event.widget
		selection=widget.curselection()
		internet(selection[0])

	lb = tk.Listbox(app, width=50, height=20)
	lb.bind("<Double-Button-1>" , clicked)

	lb.pack(side="left",fill="both", expand=True)
	for v in video_names:
		lb.insert("end", v)


#set up window
app = tk.Tk()
app.title("Daily Websites")
hypem(app)
berrics(app)
app.mainloop()





