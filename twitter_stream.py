import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

import config
import pandas as pd
import numpy as np

def twitter_authenticate():
        auth = OAuthHandler(config.consumer_key,config.consumer_secret)
        auth.set_access_token(config.access_token_key,config.access_token_secret)
        return auth

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = twitter_authenticate()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

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
        while True:
            try:
                #print(data)
                with open(tweet_file) as tf:
                    tf.write('data')
            except BaseException as e:
                print('error on_data %s' % str(e))
        return True

    def on_error(self,status):
        if status == 420: ### condition so that i do not get kicked out of twitter for accessing too much data
            False
        print(status)

class tweet_analyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """
    def tweets_to_data_frame(self, tweets):
        tweets = []
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
#
#         df['id'] = np.array([tweet.id for tweet in tweets])
#         df['len'] = np.array([len(tweet.text) for tweet in tweets])
#         df['date'] = np.array([tweet.created_at for tweet in tweets])
#         df['source'] = np.array([tweet.source for tweet in tweets])
#         df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
#         df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])


if __name__ == "__main__":
    tweet_file = 'tweets.txt'
    list_of_hastags_keywords = ['#TheBachelor', 'colton underwood']

    twitter_client = TwitterClient('BachelorABC')
    print(twitter_client.get_user_timeline_tweets(1))
    #tweets = twitter_stream()
    tweet_analyzer = tweet_analyzer()
    #tweets.stream_tweets(tweet_file,list_of_hastags_keywords)
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    #
    print(df.head(1))
