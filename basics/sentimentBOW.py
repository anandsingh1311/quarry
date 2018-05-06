import tweepy
from textblob import TextBlob

consumer_key= 'XXXXXX'
consumer_secret= 'XXXX'

access_token='XXXXX'
access_token_secret='XXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


apiClient = tweepy.API(auth)

public_tweets = apiClient.search('{Text to search for}')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
