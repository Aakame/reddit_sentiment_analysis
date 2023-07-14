#july, 8th 2023
import datetime
import praw
import pandas as pd
import numpy as np 

user_agent= 'scraper 1.0 (by u/Aka_me-)'
subreddit_name="datascience"
#number_of_submissions=1000
hot_submissions=[]
start_date = datetime.datetime(2023, 1, 1)
file_path = 'C:\\Users\\pc\\Desktop\\scraped_data\\scraped_data.csv'



reddit = praw.Reddit(
    client_id="0XBTelwbODkrdGSDTJlTqw",
    client_secret="kXQVSVz5Ql6fFTVuEx5obdqFvYfIRg",
    user_agent=user_agent,
    
)

for submission in reddit.subreddit(subreddit_name).hot(limit=None):
    timestamp = datetime.datetime.fromtimestamp(submission.created_utc)

    # Check if the submission falls within the desired time range
    if start_date > timestamp :
        continue
    else:
        comms=[]
        for top_level_comment in submission.comments:
            comms.append(top_level_comment.body.replace("\n", ""),)
        hot_submissions.append([submission.title, submission.score, submission.id, submission.num_comments, submission.selftext.replace("\n", ""), comms])

    
hot_posts = pd.DataFrame(hot_submissions,columns=['title', 'score', 'id', 'num_comments', 'body', 'comments'])
hot_posts.to_csv(file_path, index=True, encoding="UTF-8")

