import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

import config

class twitter_stream():
    """
    attributes
    """
    def __init__(self):
        pass

    def stream_tweets(self,tweet_file,list_of_hastags_keywords):
        listener = stdoutlistener(tweet_file)
        auth = OAuthHandler(config.consumer_key,config.consumer_secret)
        auth.set_access_token(config.access_token_key,config.access_token_secret)
        stream = Stream(auth,listener)

        stream.filter(track = list_of_hastags_keywords)

class stdoutlistener(StreamListener):
    """
    this class writes the tweets taken from twitter to a attribute: tweet_file
    """

    def __init__(self,tweet_file):
        self.tweet_file = tweet_file

    def on_data(self,data):
        while True:
            try:
                print(data)
                # with open(tweet_file) as tf:
                #     tf.write('data')
            except BaseException as e:
                print('error on data %s' % str(e))

if __name__ == "__main__":
    tweet_file = 'tweet.txt'
    list_of_hastags_keywords = ['#TheBachelor', 'colton underwood']
    tweets = twitter_stream()
    tweets.stream_tweets(tweet_file,list_of_hastags_keywords)
