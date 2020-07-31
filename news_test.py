import json
import numpy as np
import pandas as pd
# import seaborn as sns
import requests
import nltk
# import sqlite3
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords

url = ('https://newsapi.org/v2/everything?domains=cnn.com,nytimes.com&apiKey=a01534fb6a904ee48578f4d586219db2')
response = requests.get(url)
arr = response.json()
# print(arr)
arr_dmp = json.dumps(arr, indent = 4, sort_keys=True)
# print(arr_dmp)
r = 0
for x in arr['articles']:
    r+=1
headlines = []
published_at = []
for x in range(0,r):
    headlines.append(arr['articles'][x]['title'])
    published_at.append(arr['articles'][x]['publishedAt'])
# we now have a list of the headlines
# print(headlines,published_at)

news_df = pd.DataFrame(data=headlines,columns=['Headlines'])
news_df['PublishedAt'] = published_at
# print(news_df.head())
# converted things to df
word_splits = []
full_list=[]
for x in headlines:
    # simple splitting
    tokens = word_tokenize(x)
    # removing punctuation
    tokens = [word for word in tokens if word.isalpha()]
    # removing stop words
    stop_words = stopwords.words('english')
    tokens = [w for w in tokens if not w in stop_words]
    # word_splits.append(tokens) --> removed because we're going to have one blob of text
    full_list.append(tokens)
    # tokens=[] --> removed because we're going to have one blob of text
    # words=[]
#
# news_df['WordSplits']=word_splits
# print(news_df.head())
# we just keep this df aside for later
full_list = [y for x in full_list for y in x]
# print(full_list)

'''
We're going to combine the word splits
and take a frequency measure
'''
# using full_list
# initializing dict to store frequency of each element
elements_count = {}
# iterating over the elements for frequency
for element in full_list:
   # checking whether it is in the dict or not
   if element in elements_count:
      # incerementing the count by 1
      elements_count[element] += 1
   else:
      # setting the count to 1
      elements_count[element] = 1
# printing the elements frequencies
for key, value in elements_count.items():
   print(f"{key}: {value}")
