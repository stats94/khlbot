from bs4 import BeautifulSoup
import urllib3
import time

def getFixtures():
	http = urllib3.PoolManager()

	try:
		filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')
	except:
		print("Failed to get fixtures")
		return -1

	soup = BeautifulSoup(filehandle.data)

	for header in soup.find_all('div','header'):
		if 'Future' in header.text:
			matches = header.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
			break

	return matches

def getResults():
	http = urllib3.PoolManager()

	try:
		filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')
	except:
		print("Failed to get results")
		return -1

	soup = BeautifulSoup(filehandle.data)

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

def getDate():
	http = urllib3.PoolManager()

	try:
		filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')
	except:
		print("Failed to get date")
		return -1

	soup = BeautifulSoup(filehandle.data)

	for header in soup.find_all('div','header'):
		if 'Future' in header.text:
			date = header.next_sibling.next_sibling.next_sibling
			break

	return date

def checkCorrectDate():
	day = time.strftime("%d")
	date = getDate()

	if day[0] == '0':
		day = day[1]

	if day in date.text:
		return True
	else:
		return False

def getTodaysScores():
	scores = []


	http = urllib3.PoolManager()

	try:
		filehandle = http.urlopen('GET','http://en.khl.ru/calendar/')
	except:
		print("Failed to get today's scores")
		return scores	

	soup = BeautifulSoup(filehandle.data)

	for match in soup.find_all('li',attrs={"title":"today"}):
		for score in match.find_all('td','num'):
			if score.text != '':
				scores.append(score.previous_sibling.previous_sibling.text)
				scores.append(score.text)

				if match.find_all('tr','blue'):
					scores.append('End')
				else:
					scores.append(match.find('span','left').text)
				
	return scores
