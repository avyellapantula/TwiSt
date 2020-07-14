# import numpy as np
##
import os
import tweepy as tw
import pandas as pd

consumer_key= 'Sz9l1s6CzaT7ejESFKtY2L01d'
consumer_secret= 'YFRfAp782PHEIak4ZCZTbuqFq56q4ujA7RTyw3UynYhi7roTek'
access_token= '1282323957593575426-9h80zOQhXZ9Usf4VtcIFTKbq04bLSf'
access_token_secret= 'WsjEi4IGyAZpI1by5lUqM28KTQAJFYzhEqIksFtYVptpZ'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python
# api.update_status("I'm tweeting from #PyCharm again")
# Your tweet has been posted!

# search twitter for tweets
# Define the search term and the date_since date as variables
search_words = "#news"
date_since = "2020-06-12"

# Collect tweets, using cursor
# items limits the number of tweets printed
new_search = search_words + " -filter:retweets"
# new_search

tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(15)

# for tweet in tweets:
    # print(tweet.created_at)

info_df = [[tweet.text, tweet.created_at] for tweet in tweets]
# print(info_df,'/n')
tweet_text = pd.DataFrame(data=info_df,
                    columns=['text', 'created'])
print(tweet_text)
