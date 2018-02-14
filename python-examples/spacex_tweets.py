# builtins
import sys

# 3rd party
from bs4 import BeautifulSoup
import requests


page = requests.get('https://twitter.com/spacex')
if page.status_code != 200:
    print('Could not fetch the tweets. Exiting..')
    sys.exit(1)

soup = BeautifulSoup(page.content, 'html.parser')
tweets = soup.find_all(attrs={'class': 'tweet', 'data-name': 'SpaceX'})

last_tweets = []
for tweet in tweets[:3]:
    last_tweets.append(tweet.find(attrs={'class': 'TweetTextSize'}).text)

print('Last three SpaceX tweets')
for tweet_text in last_tweets:
    print(tweet_text)
