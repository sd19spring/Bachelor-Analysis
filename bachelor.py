'Text Mining Twitter'
'@author: Kristin Aoki'
'Attributions: https://github.com/vprusso, https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c'

#------------------------------------------------------------------------------

import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler

import config
import pandas as pd
import numpy as np
import string

#-------------------------------------------------------------------------------

def twitter_authenticate():
    """
    Establishes authentication using consumer keys and access tokens.
    Imports consumer key and access token information from config.py
    """
    auth = OAuthHandler(config.consumer_key,config.consumer_secret)
    auth.set_access_token(config.access_token_key,config.access_token_secret)
    return auth

class TwitterClient():
    """
    Creates away to read multiple twitter user's timelines
    """
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
        #gets tweets from a users timeline and adds it to a list
        #will run for a given number of times
        return tweets

class tweet_analyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    Places tweets into a DataFrame that allow them to be read easily in a .txt file
    """
    def tweets_to_data_frame(self, tweets):
        pd.set_option('display.max_colwidth', -1)
        pd.options.display.max_rows = 700
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df

def save_tweets(df,file_name):
    """
    takes the a data frame and writes it to a given file to save in a .txt file
    """
    with open(file_name,'w') as tf:
        tf.write(str(df))

def get_word_list(file_name):
    """
    Reads a file and returns a word list
    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """

    word_list = []
    with open(file_name) as f:
        for line in f:
            processed_line = line.strip(string.punctuation)
            final_line = processed_line.lower()
            final_list = final_line.split(' ')
            for list in final_list:
                if list != '\n' and len(list)>0:
                    word_list.append(list.strip(string.punctuation).strip('\n'))

    return word_list

def histogram(word_list):
    """Return a dictionary that counts occurrences of each character in s.

    Examples:
    >>> histogram('help')
    {'h': 1, 'e': 1, 'l': 1, 'p': 1}

    >>> histogram('banana')
    {'b': 1, 'a': 3, 'n': 2}
    """
    d = dict()
    entriesToRemove = ('rt', 'a', 'the', 'is', 'of', 'on', 'this', 'are', 'and',
    'i', 'as', 'in', 'or', 'we', 'you', 'thebachelor', 'be', 'to', "b'rt", 'for',
    'at', 'it', 'not', 'their', 'me', 'b"rt', 'was', 'so', 'but',"thebachelor'\t\t\t\t\t\t\t\t",
    'into', "it's", 'that', '', 'therookie', '8|7c', 'i’m','it’s', 'there', 'b',
    'has', 'these', 'an', "don't", 'all', 'if', 'just', 'get', 'were', 'while',
    'up', 'too', 'my', 'it\\xe2\\x80\\x99s', 'amp\t', 'having', 'taking', "respe\\xe2\\x80\\xa6'\t\t\t\t\t\t\t\t",
    'don\\xe2\\x80\\x99t', 'xe2\\x80\\x9ci\\xe2\\x80\\x99m', 'when', 'how', 'however')
    #removing words that no signficance (meaning not related to The Bachelor) and words that are gibberish
    for c in word_list:
        d[c] = d.get(c,0)+1
        for k in entriesToRemove:
            d.pop(k, None)

    return d

def most_frequent(word_list):
    """
    a function that reads a word list and returns a list of the letters based on their frequency (decreasing)

    >>> most_frequent('bookkeeper')
    ['e', 'o', 'k', 'r', 'p', 'b']

    >>> most_frequent('domingo')
    ['o', 'n', 'm', 'i', 'g', 'd']

    >>> most_frequent('agressiveness')
    ['s', 'e', 'v', 'r', 'n', 'i', 'g', 'a']
    """

    h = histogram(word_list)
    t = []
    for x,freq in h.items():
        t.append((freq,x))

    t.sort(reverse = True)

    res = []
    for freq,x in t:
        res.append(x)

    return res

#import doctest
#doctest.run_docstring_examples(most_frequent, globals(), verbose = True)

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

def save_top_words(word_list):
    """
    Saving most freqent words to a .txt file
    """
    with open('BachelorMostFrequent.txt', 'a') as f:
        f.write(str(word_list)+'\n')

if __name__ == "__main__":
    df_file1 = 'BachelorABC.txt'
    df_file2 = 'bachelorburnbk.txt'
    df_file3 = '#TheBachelor.txt'

    save_top_words(get_top_n_words(get_word_list(df_file1),50))
    save_top_words(get_top_n_words(get_word_list(df_file2),50))
    save_top_words(get_top_n_words(get_word_list(df_file3),50))
