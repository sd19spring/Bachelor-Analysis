import tweepy
import csv
import pandas as pd
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token_key
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data after scraping Twitter
csvFile = open('ua.csv', 'a')
#Use csv Writer to place tweets into an excel document
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#TheBachelor",count=500,
                           lang="en",
                           since="2019-01-07",
                           until="2019-03-01").items(): #sets time parameters for tweets
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
###copied and pasted info placed into csv file into a .txt file so bachelor.py could read the data
