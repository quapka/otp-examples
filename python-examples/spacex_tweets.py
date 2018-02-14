# builtins
import sys

# 3rd party
from bs4 import BeautifulSoup
import requests

def get_page():
    page = requests.get('https://twitter.com/spacex')
    return page

def parse_page(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_tweets(parsed_page):
    tweets = parsed_page.find_all(attrs={'class': 'tweet', 'data-name': 'SpaceX'})
    return tweets

def main():
    page = get_page()
    if page.status_code != 200:
        print('Could not fetch the tweets. Exiting..')
        sys.exit(1)

    parsed_page = parse_page(page)
    tweets = get_tweets(parsed_page)


    last_tweets = []
    for tweet in tweets[:3]:
        last_tweets.append(tweet.find(attrs={'class': 'TweetTextSize'}).text)

    print('Last three SpaceX tweets:')
    for tweet_text in last_tweets:
        print(tweet_text)


if __name__ == '__main__':
    main()
