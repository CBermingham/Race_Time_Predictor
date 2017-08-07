import requests
from bs4 import BeautifulSoup
import csv
import time

# -------------------------------------------

distance = '5K'
gender = 'M'
year = '2016'

#Get the urls of the individual athlete pages from the main page for an event
r = requests.get('http://www.runbritainrankings.com/rankings/rankinglist.aspx?event=' + distance + '&agegroup=ALL&sex=' + gender + '&year=' + year)

athlete_data = r.text

soup = BeautifulSoup(athlete_data, 'html.parser')

# Make the data pretty and save it so you can view it if needed
pretty_data = soup.prettify()

F = open('runbritain_athlete_data_' + year + '_' + gender + '_' + distance + '.txt','w+') 
F.write(pretty_data.encode('utf-8'))
F.close()

# --------------------------------------------

f = open('runbritain_athlete_data_' + year + '_' + gender + '_' + distance + '.txt', 'rU')
lines=f.readlines()
f.close()

links = []
ids = []
age_group = []
for l in lines:
	if "/runners/profile.aspx?athleteid=" in l:
		links.append(l[l.find("/runners/"):l.find("target=")-3])
		ids.append(l[l.find("athleteid=")+10:l.find("target=")-3])
		if l[l.find("</a>', '")+8:l.find("</a>', '")+11] == "', ":
			age_group.append("SEN")
		else:
			age_group.append(l[l.find("</a>', '")+8:l.find("</a>', '")+11])

possible_events = ['5K', '10K', 'HM', 'Mar']
count = 0

writer = csv.writer(open('runbritain_data_' + year + '_' + gender + '_' + distance + 'b.csv', "wb"))
writer.writerow(['athleteid'] + ['age_group'] + possible_events)

for link in links[0:10]:

	#Get the website data
	r = requests.get('http://www.runbritainrankings.com' + link)

	#Call the html data from the website a name
	test_data = r.text

	# Parse the data
	soup = BeautifulSoup(test_data, 'html.parser')

	# Make it more readable
#	pretty_data = soup.prettify()

	# Save the pretty html to a file (have to change it from unicode to text)
	# F = open('test_data_runbritain.txt','w+') 
	# F.write(pretty_data.encode('utf-8'))
	# F.close()

	div = soup.find("table",{"id":"cphBody_eventrankings_gvEventRankings"})
	if div != None:
		tbody = div.find("tbody")

		times = []
		events = []
		for row in tbody.find_all("tr"):
			if row.find("td").next_sibling.text == '2016':
				events.append(row.find("td").text)
				times.append(row.find("td").next_sibling.next_sibling.text)

		results = []
		for i in range(0, len(possible_events)):
			if possible_events[i] in events:
		 		results.append(times[events.index(possible_events[i])].encode('utf-8'))
		 	else:
				results.append(None)

		results = [ids[count]] + [age_group[count]] + results

		# # Save data as a csv file
		writer = csv.writer(open('runbritain_data_' + year + '_' + gender + '_' + distance + 'b.csv', "a"))
		writer.writerow(results)

		count += 1
		if count % 15 == 0:
			time.sleep(10)





















