from bs4 import BeautifulSoup
import urllib3


def getFixtures():
	http = urllib3.PoolManager()
	filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')

	soup = BeautifulSoup(filehandle.data)

	header = soup.find_all('div','header')

	for header in soup.find_all('div','header'):
		if 'Future' in header.text:
			matches = header.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
			break

	return matches

def getResults():
	http = urllib3.PoolManager()
	filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')

	soup = BeautifulSoup(filehandle.data)

	header = soup.find_all('div','header')

	for header in soup.find_all('div','header'):
		if 'Future' in header.text:
			matches = header.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling
			break

	return matches

def getTeams(matches):
	teams = []

	for team in matches.find_all('td'):
		if team.text != '-':
			teams.append(team.text)

	return teams

def getTimes(matches):
	times = []

	for time in matches.find_all('div','right'):
		hourString = time.text[0] + time.text[1]
		minutesString = time.text[3] + time.text[4]

		hour = int(hourString)

		GMTHour = hour - 4
		ESTHour = hour - 8

		GMTString = "{0}:{1}".format(GMTHour,minutesString)
		ESTString = "{0}:{1}".format(ESTHour,minutesString)

		times.append("{0} - {1} GMT - {2} EST".format(time.text,GMTString,ESTString))

	return times
