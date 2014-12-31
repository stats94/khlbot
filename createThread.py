import khlv2, time 

def threadText():
	matches = khlv2.getFixtures()
	teams = khlv2.getTeams(matches)
	times = khlv2.getTimes(matches)

	if matches == -1:
		return ""

	j = 0

	text = '|HOME|TIME|AWAY'
	text = text + '\n|-|:-:|--:'
	for i in range(0,len(teams),2):
		text = text + "\n|{0}|{1}|{2}".format(teams[i],times[j],teams[i+1])
		j += 1

	return text

def threadTitle():
	date = time.strftime("%B") + " " + time.strftime("%d")+ ", " + time.strftime("%Y")

	return "Games Thread - " + date

def editThread(originalText,liveScores):
	ls = '\n\n **LIVE SCORES**'

	table = originalText.split(ls,1)[0]

	text = table + ls

	text = text + '\n\n|HOME|SCORE|AWAY|PERIOD'
	text = text + '\n|-|:-:|--:|:-:'

	for i in range(0,len(liveScores),6):
		text = text + '\n|{0}|{1}-{2}|{3}'.format(liveScores[i],liveScores[i+1],liveScores[i+4],liveScores[i+3])

		if 'break' in liveScores[i+2]:
			text = text + '|*{0}*'.format(liveScores[i+2])
		elif 'End' in liveScores[i+2]:
			text = text + '|**END**'
		elif 'overtime' in liveScores[i+2]:
			text = text + '|*OT*'
		elif 'shootouts' in liveScores[i+2]:
			text = text + '|*SO*'
		else:
			text = text + '|*{0}*'.format(liveScores[i+2].split()[0])

	text = text + '\n\n ^^Last ^^Updated ^^' + time.strftime('%H') + ":" + time.strftime('%M') + ' ^^UTC+1 ^^|| ^^Created ^^By ^^/u/stats94'
						
	return text
