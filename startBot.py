import praw
import time
import createThread
import datetime

def sleepCalc():
	t = datetime.datetime.today()
	future = datetime.datetime(t.year,t.month,t.day,2,0)
	if t.hour >= 2:
		future += datetime.timedelta(days=1)
	time.sleep((future-t).seconds)

if __name__=="__main__":

	r = praw.Reddit(user_agent='/r/KontinentalHL bot to create the daily game threads by /u/stats94. Version 0.1')

	r.login()

	print('logged in')

	while True:
		r.submit('khlbottest', createThread.threadTitle(), text=createThread.threadText())

		sleepCalc()
