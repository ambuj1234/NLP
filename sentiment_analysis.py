# -*- coding: utf-8 -*-
"""sentiment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fEo5R5guZvmO0ql1qHPmnGDFPPR0n1yv
"""

!pip3 install tweepy

import tweepy
import time
from textblob import TextBlob
import matplotlib.pyplot as plt

# storing consumer key and token
consumer_key = 'kqEGmgAt3WNava7BNq9loZNNX'
consumer_secret_key = "dcELgyinahrFM3GE6HPk1VcTT99GAOzN6HZQGA1apJ1kj4BmjW"

# access key and access secret key store
access_token="276375321-YX0Au6SyRczoe2tiOjchRbhANOMs1bjAsMOr1nmW"
access_secret_token="xEoT9B36t9XA8pidcUrGELidVC8VBsewjRN0m8CMJAlq3"

# finding method for consumer key and consumer secret key
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)

# now using this auth with access token and secret
auth.set_access_token(access_token,access_secret_token)

# now you can connect api
api_connect=tweepy.API(auth)

# now api is connected you can search the topic
tweets=api_connect.search('virat',count=10)
tweets
pos=0
neg=0
neu=0

for tweet in tweets:
  print(tweet.text)
for tweet in tweets:
  analysis=TextBlob(tweet.text)
  #print(analysis.sentiment)
  if analysis.sentiment.polarity > 0
    print("positive")
    pos=pos+1
  elif analysis.sentiment.polarity == 0
    print("neutral")
    neu=neu+1
  else : 
    print("negative")
    neg=neg+1
    
print(pos,neg,neu)

plt.xlabel("sentiments")
plt.ylabel("count")
plt.bar(["positive","negative","neutral"],[pos,neg,neu])
plt.show()