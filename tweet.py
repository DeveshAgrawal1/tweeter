import urllib
from BeautifulSoup import BeautifulSoup
import requests
import tweepy
from tweepy import OAuthHandler

def findquote():
    url='http://www.brainyquote.com/quotes_of_the_day.html'
    response = requests.get(url)
    source=response.text.encode('ascii', 'ignore')
    soup=BeautifulSoup(source)
    for quote in soup.find('span',{'class':'bqQuoteLink'}):
        string_quote=quote.string
        #print string_quote
        return string_quote

def usetwitter():
    consumer_key = 'your consumer key here'
    consumer_secret = 'your consumer secret key here'
    access_token = 'your access token here'
    access_secret = 'your access secret key here'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    tweet=findquote()
    status=api.update_status(tweet)

usetwitter()