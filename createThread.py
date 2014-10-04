import khlv2, time 

def threadText():
	matches = khlv2.getFixtures()
	teams = khlv2.getTeams(matches)
	times = khlv2.getTimes(matches)

	j = 0

	text = '|HOME|TIME|AWAY'
	text = text + '\n|-|-|-'
	for i in range(0,len(teams),2):
		text = text + "\n|{0}|{1}|{2}".format(teams[i],times[j],teams[i+1])
		j += 1

	return text

def threadTitle():
	date = time.strftime("%B") + " " + time.strftime("%d")+ ", " + time.strftime("%Y")

	return "Games Thread - " + date
