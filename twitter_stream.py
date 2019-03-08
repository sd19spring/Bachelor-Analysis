import tweepy
from tweepy import API
from tweepy import Cursor
#from tweepy.streaming import StreamListener
#from tweepy import Stream
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

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

# class twitter_stream():
#     """
#     attributes
#     """
#     def __init__(self):
#         self.twitter_authenticate = twitter_authenticate
#
#     def stream_tweets(self,tweet_file,list_of_hastags_keywords):
#         listener = twitter_listener(tweet_file)
#         auth = self.twitter_authenticate()
#         stream = Stream(auth,listener)
#
#         stream.filter(track = list_of_hastags_keywords)
#
# class twitter_listener(StreamListener):
#     """
#     this class writes the tweets taken from twitter to a attribute: tweet_file
#     """
#
#     def __init__(self,tweet_file):
#         self.tweet_file = tweet_file
#
#     def on_data(self,data):
#         i = 0
#         for i in range (10):
#             try:
#                 #print(data)
#                 with open(tweet_file,'w') as tf:
#                     tf.write(data)
#             except BaseException as e:
#                 print('error on_data %s' % str(e))
#             i = i+1
#         close.tweet_file
#         return True
#
#     def on_error(self,status):
#         if status == 420: ### condition so that i do not get kicked out of twitter for accessing too much data
#             False
#         print(status)

class tweet_analyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """
    def tweets_to_data_frame(self, tweets):
        pd.set_option('display.max_colwidth', -1)
        pd.options.display.max_rows = 700
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df
        #df['date'] = np.array([tweet.created_at for tweet in tweets])

def save_tweets(df):
    with open(df_file,'w') as tf:
        tf.write(str(df))


if __name__ == "__main__":
    df_file = 'BachelorABC.txt'
    list_of_hastags_keywords = ['#TheBachelor', 'colton underwood']
    #tweets = twitter_stream()
    #tweets.stream_tweets(tweet_file,list_of_hastags_keywords)

    # twitter_client = TwitterClient('BachelorABC')
    # twitter_client2 = TwitterClient('bachelorburnbk')
    # print(twitter_client.get_user_timeline_tweets(679))
    # print(twitter_client2.get_user_timeline_tweets(60))

    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets1 = api.user_timeline(screen_name = 'BachelorABC', count = 679)
    tweets2 = api.user_timeline(screen_name = 'bachelorburnbk', count = 60)
    #print(tweets1)
    #print(tweets2)

    tweet_analyzer = tweet_analyzer()
    df1 = tweet_analyzer.tweets_to_data_frame(tweets1)
    df2 = tweet_analyzer.tweets_to_data_frame(tweets2)
    #print(df1.head(10))
    #print(df2)
    save_tweets(df1)
    
