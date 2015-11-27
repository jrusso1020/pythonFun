'''
This script webscrapes hypem.com for todays most popular songs then displays them in a window
and allows the user to double click on the song which will open up the song in their webbrowser
Possible additions:
1. have double click start playing song automatically when double click(invisible webbrowser which starts playing song)
2. fix look of window
'''
from bs4 import BeautifulSoup
import urllib
import Tkinter as tk
import webbrowser

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
	webbrowser.open_new("http://www.hypem.com/" + links[index])

#when double clicked calls this method to get selection and open tab
def clicked(event):
	widget = event.widget
	selection=widget.curselection()
	internet(selection[0])
	
#set up window
app = tk.Tk()
app.title("Today Hypem Top 50")
scrollbar = tk.Scrollbar(app, orient="vertical")
lb = tk.Listbox(app, width=50, height=20, yscrollcommand=scrollbar.set)
lb.bind("<Double-Button-1>" , clicked)
scrollbar.config(command=lb.yview)

scrollbar.pack(side="right", fill="y")
lb.pack(side="left",fill="both", expand=True)
for t in tracks:
	lb.insert("end", str(tracks.index(t)+1) + ".\t"+t)
app.mainloop()