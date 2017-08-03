import requests
from bs4 import BeautifulSoup

#Get the website data
r = requests.get('http://www.thepowerof10.info/athletes/profile.aspx?athleteid=2585')

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

# Go through the rows and save the first and second entries in each into lists
event = []
pb = []
year2017 = []
year2016 = []
rows = table.find_all('tr')
for i in rows:
   	event.append(i.find('td').string.encode('utf-8'))
   	if i.find('td').next_sibling.string is not None:
   		pb.append(i.find('td').next_sibling.string.encode('utf-8'))
   	else:
   		pb.append(None)
   	if i.find('td').next_sibling.next_sibling.string is not None:
 		year2017.append(i.find('td').next_sibling.next_sibling.string.encode('utf-8'))
 	else:
   		year2017.append(None)
 	if i.find('td').next_sibling.next_sibling.next_sibling.string is not None:
		year2016.append(i.find('td').next_sibling.next_sibling.next_sibling.string.encode('utf-8'))
	else:
   		year2016.append(None)

# for i in rows:
# 	for child in list(i.descendants)[1]:
# 		if child is not None:
# 			print child.string.encode('utf-8')
# 		else:
# 			print None
#	print "END"

# for i in rows:
# 	for sibling in list(i.find('td').next_siblings)[1]:
# 		if sibling.string is not None:
# 			print sibling.string.encode('utf-8')
# 		else:
# 			print "None"


print event
print pb
print year2017
print year2016



