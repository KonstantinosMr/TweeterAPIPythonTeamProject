
import tweepy
import configparser
import pandas as pd
import re
import collections
import itertools
import os
import collections

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Tweet search
search_term = "#csharp  -filter:retweets"


tweets = tweepy.Cursor(api.search_tweets,
                   q=search_term,
                   lang="en",
                   since='2018-11-01').items(100)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
all_tweets_no_urls[:5]

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].split()

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].lower().split()
    # Create a list of lists containing lowercase words for each tweet
words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
words_in_tweet[:2]
    # List of all words across tweets
all_words_no_urls = list(itertools.chain(*words_in_tweet))
    # Create counter
counts_no_urls1 = collections.Counter(all_words_no_urls)

counts_no_urls1.most_common(1)

clean_tweets_no_urls1 = pd.DataFrame(counts_no_urls1.most_common(1),
                             columns=['Programming Languages', 'count'])

clean_tweets_no_urls1.head()
print(clean_tweets_no_urls1)
clean_tweets_no_urls1.to_excel('csharp.xlsx')

#Tweet search
search_term = "#java  -filter:retweets"


tweets = tweepy.Cursor(api.search_tweets,
                   q=search_term,
                   lang="en",
                   since='2018-11-01').items(100)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
all_tweets_no_urls[:5]

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].split()

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].lower().split()
    # Create a list of lists containing lowercase words for each tweet
words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
words_in_tweet[:2]
    # List of all words across tweets
all_words_no_urls = list(itertools.chain(*words_in_tweet))

# Create counter
counts_no_urls2 = collections.Counter(all_words_no_urls)

counts_no_urls2.most_common(1)

clean_tweets_no_urls2 = pd.DataFrame(counts_no_urls2.most_common(1),
                             columns=['Programming Languages', 'count'])

clean_tweets_no_urls2.head()
print(clean_tweets_no_urls2)

#Tweet search
search_term = "#javascript  -filter:retweets"


tweets = tweepy.Cursor(api.search_tweets,
                   q=search_term,
                   lang="en",
                   since='2018-11-01').items(100)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
all_tweets_no_urls[:5]

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].split()

    # Split the words from one tweet into unique elements
all_tweets_no_urls[0].lower().split()
    # Create a list of lists containing lowercase words for each tweet
words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
words_in_tweet[:2]
    # List of all words across tweets
all_words_no_urls = list(itertools.chain(*words_in_tweet))