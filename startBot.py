import praw
import time
import createThread
import datetime
from khlv2 import checkCorrectDate, getTodaysScores

if __name__=="__main__":

	r = praw.Reddit(user_agent='/r/KontinentalHL bot to create the daily game threads by /u/stats94. Version 0.3')

	r.login()

	print('logged in')

	while True:
		try:
			submissions = list(r.get_redditor('khlbot').get_submitted())
		except:
			print("Failed to get submissions")

		if submissions[0].title != createThread.threadTitle() and checkCorrectDate:
			threadText = createThread.threadText()

			if threadText != "":
				try:
					r.submit('KontinentalHL', createThread.threadTitle(), text=threadText)
				except:
					print("Error creating Game Thread")

		for _ in range(0,180):
			scores = getTodaysScores()
		
			if scores:
				try:
					submissions[0].edit(createThread.editThread(submissions[0].selftext,scores))
				except:
					print("Error editing Game Thread")
				
			time.sleep(120)
