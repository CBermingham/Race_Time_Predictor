import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.thepowerof10.info/rankings/rankinglist.aspx?event=10K&agegroup=ALL&sex=W&year=2017')

athlete_data = r.text

soup = BeautifulSoup(athlete_data, 'html.parser')

pretty_data = soup.prettify()

F = open('athlete_data.txt','w+') 
F.write(pretty_data.encode('utf-8'))
F.close()

tr = soup.find('tr', {"class":"rankinglistheadings"})

links = []
rows = tr.parent.find_all('tr')
for i in rows[1:]:
	if i.find('a') is not None:
		links.append(i.find('a')['href'])

for i in links:
	print i

