import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

import config

class twitter_stream():
    """

    """
    def __init__(self):
        pass
    def stream_tweets(self,tweet_file,list_of_hastags_keywords):
        listener = stdlistener(tweet_file)
        auth = OAuthHandler(config.consumer_key,config.consumer_secret)
        auth.set_access_token(config.access_token_key,config.access_token_secret)
        stream = Stream(auth,listener)

    
