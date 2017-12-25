# Python module to open a read only PRAW Reddit instance
# and return that user's comments

import praw
import json
import pandas as pd


from prawcore.exceptions import NotFound

COMMENT_LIMIT = 100

def init_reddit():
    '''
    :return praw.Reddit connect to Reddit API with praw 
    '''
    reddit = praw.Reddit('reddit_comment_bot', user_agent='web:comment_visualizer:v0.1 (by /u/g4mecrazy)')
    return reddit


def get_redditor(redditor_name, reddit):
    '''
    :param redditor_name: Expects string of reddit username
    :param reddit: Reference to the reddit script instance 
    :return praw.Reddit.redditor instance for that user if it exists. Other throws an exception.
    '''
    return reddit.redditor(redditor_name)


def get_comments_from_redditor(redditor, reddit):
    '''
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


def main():
    #Creates a new Reddit instance, client_id and client_secret should be defined in your praw.ini
    # reddit = init_reddit()

    # comments = []

    # redditor_name = 'g4mecrazy' #TODO: stubbed in for testing; get from user

    # redditor = get_redditor(redditor_name, reddit)
    # for comment in redditor.comments.new(limit=COMMENT_LIMIT):
    #     comments.append(dict([('text', comment.body)]))

    # comment_json = json.dumps(comments)
    # print(comment_json)
    # return comments

if __name__ == '__main__':
    main()
