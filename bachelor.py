import tweepy
from tweepy import API
from tweepy import Cursor
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

    
# def get_word_list(file_name):
#     """Read the specified project Gutenberg book.
#
#     Header comments, punctuation, and whitespace are stripped away. The function
#     returns a list of the words used in the book as a list. All words are
#     converted to lower case.
#     """
#
#     word_list = []
#     with open(file_name) as f:
#         for line in f:
#             processed_line = line.strip(string.punctuation)
#             final_line = processed_line.lower()
#             final_list = final_line.split(' ')
#             for list in final_list:
#                 if list != '\n' and len(list)>0:
#                     word_list.append(list.strip(string.punctuation).strip('\n'))
#
#     return word_list
#
# def histogram(word_list):
#     """Return a dictionary that counts occurrences of each character in s.
#
#     Examples:
#     >>> histogram('help')
#     {'h': 1, 'e': 1, 'l': 1, 'p': 1}
#
#     >>> histogram('banana')
#     {'b': 1, 'a': 3, 'n': 2}
#     """
#     d = dict()
#     for c in word_list:
#         d[c] = d.get(c,0)+1
#
#     return d
#
# def most_frequent(word_list):
#     """
#     a function that reads a word and returns a list of the letters based on their frequency (decreasing)
#
#     >>> most_frequent('bookkeeper')
#     ['e', 'o', 'k', 'r', 'p', 'b']
#
#     >>> most_frequent('domingo')
#     ['o', 'n', 'm', 'i', 'g', 'd']
#
#     >>> most_frequent('agressiveness')
#     ['s', 'e', 'v', 'r', 'n', 'i', 'g', 'a']
#     """
#
#     h = histogram(word_list)
#     t = []
#     for x,freq in h.items():
#         t.append((freq,x))
#
#     t.sort(reverse = True)
#
#     res = []
#     for freq,x in t:
#         res.append(x)
#
#     return res
#
# import doctest
# doctest.run_docstring_examples(most_frequent, globals(), verbose = True)

def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
        Most frequently to least frequently occurring
    """
    top_n_words = most_frequent(word_list)[:n]

    return top_n_words
import os
import requests
import sys
import time

def strip_scheme(url):
    """
    Return 'url' without scheme part (e.g. "http://")

    >>> strip_scheme("https://www.example.com")
    'www.example.com'
    >>> strip_scheme("http://www.gutenberg.org/files/2701/2701-0.txt")
    'www.gutenberg.org/files/2701/2701-0.txt'
    """
    # TODO: This ad-hoc implementation is fairly fragile
    # and doesn't support e.g. URL parameters (e.g. ?sort=reverse&lang=fr)
    # For a more robust implementation, consider using
    # https://docs.python.org/3/library/urllib.parse.html
    scheme, remainder = url.split("://")
    return remainder


class Text:
    """
    Text class holds text-based information downloaded from the web
    It uses local file caching to avoid downloading a given file multiple times,
    even across multiple runs of the programself.
    """
    def __init__(self, url, file_cache=os.path.join(sys.path[0], "cache")):
        """
        Given 'url' of a text file, create a new instance with the
        text attribute set by either downloading the URL or retrieving
        it from local text cache.

        Optional 'file_cache' argument specifies where text cache should be
        stored (default: same directory as the script in a "cache" folder)
        """
        self.url = url
        self.local_fn = os.path.join(file_cache, strip_scheme(url))

        # First see if file is already in local file cache
        if self.is_cached():
            print("INFO: {url!r} found in local file cache, reading".format(url=self.url))
            self.read_cache()

        # If not found, download (and write to local file cache)
        else:
            print("INFO: {url!r} not found in local file cache, downloading".format(url=self.url))
            self.download()
            self.write_cache()

    def lines(self):
        new_lines = []
        example = Text(url)
        for line in examples.lines():
            return new_lines.append(line)


    def __repr__(self):
        return "Text({url!r})".format(url=self.url)

    def is_cached(self):
        """Return True if file is already in local file cache"""
        return os.path.exists(self.local_fn)

    def download(self):
        """Download URL and save to .text attribute"""
        self.text = requests.get(self.url).text     # TODO: Exception handling
        # Wait 2 seconds to avoid stressing data source and rate-limiting
        # You don't need to do this here (only has to happen between requests),
        # but you should have it somewhere in your code
        time.sleep(2)

    def write_cache(self):
        """Save current .text attribute to text cache"""
        # Create directory if it doesn't exist
        directory = os.path.dirname(self.local_fn)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Write text to local file cache
        with open(self.local_fn, 'w') as fp:
            fp.write(self.text)

    def read_cache(self):
        """Read from text cache (file must exist) and save to .text attribute"""
        with open(self.local_fn, 'r') as fp:
            self.text = fp.read()

def run_example():
    """
    Return a dictionary with key: book title, value: Text objects for books.
    """
    import time

    urls = { "#TheBachelor": "https://twitter.com/search?q=%23TheBachelor&src=tyah"
           }

    texts = {}
    for title, url in urls.items():
        t = Text(url)
        texts[title] = t

    return texts


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    #print(get_top_n_words(get_word_list(tweet.text),100))
    from pprint import pprint   # "Pretty-print" dictionary
    tweets = run_example()
    pprint(tweets)
