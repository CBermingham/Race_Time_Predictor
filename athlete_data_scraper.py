import requests
from bs4 import BeautifulSoup
import unicodedata

#Get the website data
r = requests.get('http://www.thepowerof10.info/athletes/profile.aspx?athleteid=6313')

#Call the html data from the website a name
test_data = r.text

# Parse the data
soup = BeautifulSoup(test_data, 'html.parser')

# Make it more readable
pretty_data = soup.prettify()

# Save the pretty html to a file (have to change it from unicode to text)
F = open('test_data.txt','w+') 
F.write(pretty_data.encode('utf-8'))
F.close()

# Identify the table of interest using the div and class
div = soup.find("div",{"id":"cphBody_divBestPerformances"})
table = div.find("table")
th = table.find('tr', {"class":"bestperformancesheader"}).next_sibling

# Go through the rows and save the first and second entries in each into lists
event = []
time = []
rows = table.find_all('tr')
for i in rows:
   	event.append(i.find('td').string.encode('utf-8'))
   	time.append(i.find('td').next_sibling.string.encode('utf-8'))





