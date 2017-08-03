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
for i in rows:
	links.append(i.find('a'))

# del links[0]
# links2 = []
# for i in range(0, len(links)):
# 	if links[i] != 0:
# 		links2.append(links[i])

# for i in links2:
# 	print i


# if tr is not None:
# 	for i in tr.siblings:
# 		print i.find('a')
# print tr.next_sibling.find('a')
# print tr.next_sibling.next_sibling.find('a')

#table = soup.find("table")
# rows = table.find_all('tr')
# for i in rows:
# 	print i.find('td')


# th = table.find('tr', {"class":"bestperformancesheader"}).next_sibling

# for link in soup.find_all('a'):
# 	new = link.encode('utf-8')
# 	if "athleteid" in new:
# 		print link
