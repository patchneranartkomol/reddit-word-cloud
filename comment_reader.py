# Python module to open a read only PRAW Reddit instance
# and return that user's comments

import praw

COMMENT_LIMIT = 100

def get_redditor(redditor_name):
    '''
    :param redditor_name: Expects string of reddit username
    :return praw.Reddit.redditor instance for that user if it exists. Other throws an exception.
    '''
    return reddit.redditor(redditor_name)




def main():
    #Creates a new Reddit instance, client_id and client_secret should be defined in your praw.ini
    reddit = praw.Reddit('reddit_comment_bot', user_agent='web:comment_bot:v0.1 (by /u/g4mecrazy)')

    comments = []

    redditor = get_redditor(redditor_name)
    for comment in redditor.comments.new(limit=COMMENT_LIMIT):
        comments.append(comment.body)

    print(comments)
    return comments

if __name__ == '__main__':
    main()