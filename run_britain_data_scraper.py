import requests
from bs4 import BeautifulSoup

#Get the website data
r = requests.get('http://www.runbritainrankings.com/runners/profile.aspx?athleteid=17296')

#Call the html data from the website a name
test_data = r.text

# Parse the data
soup = BeautifulSoup(test_data, 'html.parser')

# Make it more readable
pretty_data = soup.prettify()

# Save the pretty html to a file (have to change it from unicode to text)
F = open('test_data_runbritain.txt','w+') 
F.write(pretty_data.encode('utf-8'))
F.close()

div = soup.find("table",{"id":"cphBody_eventrankings_gvEventRankings"})
tbody = div.find("tbody")

for row in tbody.find_all("tr"):
	if row.find("td").next_sibling.text == '2016':
		print row.find("td").text
		print row.find("td").next_sibling.next_sibling.text
#	if row.find("td").text == "2017":
#		print row.find("td").text

#row = div.find("tbody")
#print row.find("td").text
#print row.find("td").next_sibling.text
#print row.find("td").next_sibling.next_sibling.text

#table = div.next_sibling.find("table")
#print table