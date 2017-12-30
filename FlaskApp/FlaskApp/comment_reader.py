# Python module to open a read only PRAW Reddit instance
# and return that user's comments

import praw
import json
import pandas as pd
import nltk


from prawcore.exceptions import NotFound
from collections import Counter
from string import punctuation
from nltk.corpus import stopwords

COMMENT_LIMIT = 100

def init_reddit():
    ''' Initialize a reddit session through PRAW - Python Reddit API wrapper
    :return praw.Reddit connect to Reddit API with praw 
    '''
    reddit = praw.Reddit('reddit_comment_bot', user_agent='web:comment_visualizer:v0.1 (by /u/g4mecrazy)')
    return reddit


def get_redditor(redditor_name, reddit):
    ''' Query the Reddit API to find user if exists
    :param redditor_name: Expects string of reddit username
    :param reddit: Reference to the reddit script instance 
    :return praw.Reddit.redditor instance for that user if it exists. Other throws an exception.
    '''
    return reddit.redditor(redditor_name)


def get_comments_from_redditor(redditor, reddit):
    ''' Returns list of comments from PRAW Redditor Object
    :param redditor_name: Expects string of reddit username
    :param reddit: Reference to the reddit script instance 
    :return list of comments
    '''
    comments = []
    try:
        for comment in redditor.comments.new(limit=COMMENT_LIMIT):
            comments.append(comment.body)
    except prawcore.exceptions.NotFound:
        raise NameError
    return comments

def extract_top_comments_to_list(comments):
    ''' Convert full list of comments to dictionary of common words and sizes,
        returning the top 20 keywords, utilizes nltk's English stopwords as words to ignore
    :param comments: list of user comments
    :return list of top words
    '''
    stopwords = set(nltk.corpus.stopwords.words('english'))
    without_stp  = Counter()
    for comment in comments:
        words = comment.split()
        without_stp.update(w.lower().rstrip(punctuation) for w in words if w not in stopwords)
    top_words = []
    for word, count in without_stp.most_common(25):
        top_words.append(word)
    return top_words

def main():
    pass

if __name__ == '__main__':
    main()
