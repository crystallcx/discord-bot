import os
import tweepy
from hikari import *
import lightbulb

DISCORD_CHANNEL_ID = "997729115463487581"
TWITTER_USER_ID = "the_grocers"

plugin = lightbulb.Plugin('Twitter') # Create instance of plugin

# create function load that takes in an instance of the bot application
# and adds the plugin previously created to the bot to use wihtin discord
def load(bot):
    bot.add_plugin(plugin)

# Initialize the Twitter API client
auth = tweepy.OAuth1UserHandler(
    os.environ['TWITTER_CONSUMER_KEY'],
    os.environ['TWITTER_CONSUMER_SECRET'], 
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
# auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])

# Define the callback function to handle the Twitter stream
class MyStream(tweepy.Stream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_status(self, status):
        # Check if the tweet is not a retweet
        if not hasattr(status, 'retweeted_status'):
            # Create the Discord message
            message = Embed(title=status.user.name, url=f'https://twitter.com/{status.user.screen_name}/status/{status.id_str}')
            message.set_author(name='@' + status.user.screen_name, icon_url=status.user.profile_image_url)
            message.set_footer(text=status.created_at.strftime('%Y-%m-%d %H:%M:%S'))

            # Add the tweet content to the Discord message
            if status.full_text:
                message.description = status.full_text

            # Add the tweet image to the Discord message
            if status.entities.get('media'):
                message.set_image(status.entities.get('media')[0]['media_url'])

            # Post the Discord message
            bot.rest.create_message(channel_id=DISCORD_CHANNEL_ID, embed=message)
            
# Start the Twitter stream
stream = MyStream(
    os.environ['TWITTER_CONSUMER_KEY'],
      os.environ['TWITTER_CONSUMER_SECRET'],
      os.environ['TWITTER_ACCESS_TOKEN'], 
      os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
stream.filter(follow=['TWITTER_USER_ID'])