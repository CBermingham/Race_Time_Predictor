import requests
from bs4 import BeautifulSoup

#Get the website data
r = requests.get('http://www.thepowerof10.info/athletes/profile.aspx?athleteid=6313')

#Call the html data from the website a name
test_data = r.text

# Parse the data
soup = BeautifulSoup(test_data, 'html.parser')

#print soup.prettify()

print soup.title
