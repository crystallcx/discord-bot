import lightbulb
import hikari
import tweepy
import os

from tweepy.streaming import StreamListener
from tweepy import Stream
from time import gmtime, strftime
from time import sleep
import urllib3
import requests

plugin = lightbulb.Plugin('Twitter') # Create instance of plugin

# create function load that takes in an instance of the bot application
# and adds the plugin previously created to the bot to use wihtin discord
def load(bot):
    bot.add_plugin(plugin)

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])