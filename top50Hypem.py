from bs4 import BeautifulSoup
import urllib
import Tkinter as tk
import webbrowser


track_names = []

for i in range(1,4):
	r = urllib.urlopen('http://hypem.com/popular/' + str(i)).read()
	soup = BeautifulSoup(r, "lxml")
	track_names.extend(soup.find_all("h3", class_="track_name"))

atags = []

links = []

for t in track_names:
	atags.append(t.find_all("a"))

for t in track_names:
	links.append(t.find("a", class_="track")['href'])


tracks = []
for x in atags:
	s = ""
	for y in x:
		s= s + y.get_text()
	tracks.append(s.replace("\n", ": "))

def internet(index):
	webbrowser.open_new_tab("http://www.hypem.com/" + links[index])

def clicked(event):
	widget = event.widget
	selection=widget.curselection()
	internet(selection[0])
	

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