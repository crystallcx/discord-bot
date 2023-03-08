discord bot:
https://discord.com/developers/applications/

## Setup:
- `python3 -m venv env`  # create virtual environment env so modules are not installed across enitre system

## Requirements:
- python3.10
- hikari: `python3 -m pip install -U hikari`
- hikari-lightbulb: `pip install hikari-lightbulb`


## To run:
- `. env/bin/activate`  # activate virtual environment or source env/bin/activate
- `python3 bot.py` #start bot




Referred to videos in the following series:
https://www.youtube.com/watch?v=RejwzqK6dJI



#
#
#

# Discord Features
## Intents
Intents are a feature in the Discord API that allow bots to specify which events they want to receive from the Discord server. By enabling or disabling certain intents, a bot can customize the set of events it receives, which can help reduce the amount of unnecessary data the bot receives and improve its performance.

To enable or disable intents in your Discord bot, you can use the Intents class in the discord module. For example, to enable the members intent, you can do:
```
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
```