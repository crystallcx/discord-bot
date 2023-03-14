discord bot:
https://discord.com/developers/applications/

## Setup:
- `python3 -m venv env`  # create virtual environment env so modules are not installed across enitre system

Create `.env` file defining variables:
- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_TOKEN_SECRET

## Requirements:
- python3.10
- hikari: `python3 -m pip install -U hikari`
- tweepy
- hikari-lightbulb: `pip install hikari-lightbulb`


## To run:
- `. env/bin/activate`  # activate virtual environment or source env/bin/activate
- `python3 bot.py` #start bot


## Hikari Documentation
https://docs.hikari-py.dev/en/latest/reference/hikari/


Referred to videos in the following series:
https://www.youtube.com/watch?v=RejwzqK6dJI



#
#
#


## Troubleshooting
### Why is some information about my messages from MessageCreateEvent unavailable?
Intents are a feature in the Discord API that allow bots to specify which events they want to receive from the Discord server. By enabling or disabling certain intents, a bot can customize the set of events it receives, which can help reduce the amount of unnecessary data the bot receives and improve its performance.

You may have not enabled the Message Content Intent. This had been a thing for bots from August 31st, 2022 onward. For more info, refer to https://support-dev.discord.com/hc/en-us/articles/4404772028055

Firstly, go to your discord developer portal. In your bot application, in the bot section, tick this to be on. (check the attached screenshot: https://i.imgur.com/8Ps9Boi.png)
Secondly, in your bot's code, add the highlighted lines:
```
bot = hikari.GatewayBot( # or lightbulb.BotApp
    "your token",
    intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.MESSAGE_CONTENT # Add this line
)
```