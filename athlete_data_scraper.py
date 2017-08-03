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

#table = soup.table
#print table.string

#print soup.find_all('a')

#table = soup.find_all("PB")
#print table

#table = soup.find('table', {'class': "athleteprofilesubheader"})
#print table.string

table = soup.find(lambda tag: tag.name=='td' and tag.has_attr('id') and tag['id']=="cphBody_divBestPerformances") 

print table
#rows = table.findAll(lambda tag: tag.name=='tr')

