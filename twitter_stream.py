import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

import config
import pandas
import numpy


def twitter_authenticate():
        auth = OAuthHandler(config.consumer_key,config.consumer_secret)
        auth.set_access_token(config.access_token_key,config.access_token_secret)
        return auth

class twitter_stream():
    """
    attributes
    """
    def __init__(self):
        self.twitter_authenticate = twitter_authenticate

    def stream_tweets(self,tweet_file,list_of_hastags_keywords):
        listener = twitter_listener(tweet_file)
        auth = self.twitter_authenticate()
        stream = Stream(auth,listener)

        stream.filter(track = list_of_hastags_keywords)

class twitter_listener(StreamListener):
    """
    this class writes the tweets taken from twitter to a attribute: tweet_file
    """

    def __init__(self,tweet_file):
        self.tweet_file = tweet_file

    def on_data(self,data):
        #i = 0
        #for i in range[500]:
        while True:
            try:
                print(data)
                # with open(tweet_file) as tf:
                #     tf.write('data')
            except BaseException as e:
                print('error on_data %s' % str(e))
            #i = i+1
    def error(self,status):
        if status == 420: ### condition so that i do not get kicked out of twitter for accessing too much data
            False
        print(status)

if __name__ == "__main__":
    tweet_file = 'tweet.txt'
    list_of_hastags_keywords = ['#TheBachelor', 'colton underwood']
    tweets = twitter_stream()
    tweets.stream_tweets(tweet_file,list_of_hastags_keywords)
