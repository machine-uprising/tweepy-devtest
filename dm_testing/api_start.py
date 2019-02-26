import tweepy
from tweepy import OAuthHandler


import api_keystore as keys

API_KEY = keys.API_KEYSTORE["API_KEY"]
API_SECRET = keys.API_KEYSTORE["API_SECRET"]

ACCESS_TOKEN = keys.API_KEYSTORE["ACCESS_TOKEN"]
ACCESS_SECRET = keys.API_KEYSTORE["ACCESS_SECRET"]

auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth_handler=auth)
