import requests
from bs4 import BeautifulSoup
import csv
import time

# -------------------------------------------
# Get the urls of the individual athlete pages from the main page for an event
r = requests.get('http://www.thepowerof10.info/rankings/rankinglist.aspx?event=10K&agegroup=ALL&sex=W&year=2017')

athlete_data = r.text

soup = BeautifulSoup(athlete_data, 'html.parser')

## Make the data pretty and save it so you can view it if needed
# pretty_data = soup.prettify()

# F = open('athlete_data.txt','w+') 
# F.write(pretty_data.encode('utf-8'))
# F.close()

tr = soup.find('tr', {"class":"rankinglistheadings"})

links = []
rows = tr.parent.find_all('tr')
for i in rows[1:]:
	if i.find('a') is not None:
		links.append(i.find('a')['href'])

# -------------------------------------------
#Get the athlete's best times data from each page

possible_events = ['60', '100', '200', '400', '600', '800', '1000', '1200', '1500', 'Mile', '3000', '5000', '10000', '1M', '2M', '3K', '5K', '10K', '10M', 'HM', 'Mar']
headings_all = [i + "_PB" for i in possible_events] + [i+ "_2017" for i in possible_events] + [i+ "_2016" for i in possible_events]
writer = csv.writer(open("test_times_data.csv", "wb"))
writer.writerow(headings_all)
count = 0

for link in links:

	#Get the website data
	r = requests.get('http://www.thepowerof10.info' + link)

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


		

	# Make new lists with only the events in possible_events 
	headings = []
	results_pb = []
	results_2017 = []
	results_2016 = []
	for i in range(0, len(possible_events)):
		if possible_events[i] in event:
			headings.append(possible_events[i])
			results_pb.append(pb[event.index(possible_events[i])])
			results_2017.append(year2017[event.index(possible_events[i])])
			results_2016.append(year2016[event.index(possible_events[i])])
		else:
			headings.append(possible_events[i])
			results_pb.append(None)
			results_2017.append(None)
			results_2016.append(None)

	# Make into one list of events for PB, 2017 and 2016

	results_all = results_pb + results_2017 + results_2016

	# # Save data as a csv file
	writer = csv.writer(open("test_times_data.csv", "a"))
	writer.writerow(results_all)

	count += 1
	if count % 15 == 0:
		time.sleep(10)



