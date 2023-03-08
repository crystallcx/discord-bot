import os
from typing import Optional
from dotenv import load_dotenv

import hikari
import lightbulb
from hikari import Intents

# Load environment variables from .env file
load_dotenv()

# Access environment variables using os.environ.get()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

INTENTS = Intents.GUILD_MEMBERS | Intents.GUILDS

bot = lightbulb.BotApp(
    token = BOT_TOKEN,
    intents=INTENTS,
    banner=None,
    default_enabled_guilds = 997729114968555540
)

# token taken from https://discord.com/developers/applications/997331587966447678/bot

@bot.listen(hikari.StartedEvent) # triggers when bot is started
async def bot_started(event): # function header
    print('Bot has started')

#--- Automatic messages when users join and leave server
@bot.listen(hikari.MemberCreateEvent)
async def on_group_join(event):
    print(f'{event.member} has joined the toke space.')
# @bot.listen()
# def on_group_join(event: hikari.MemberCreateEvent):
#     print(f'{event.member} has joined the toke space.')

@bot.listen(hikari.MemberDeleteEvent)
async def on_group_remove(event):
    print(f'{event.member} has left the toke space.')


@bot.listen()
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
    if event.content == "!ping":
        print(event.message.content)
#----------------------------
# Slash Commands
#----------------------------
# order in which these appear above funciton header is important
"""
Using `ctx` vx `ctx: lightbulb.Context` as an argument name.
ctx: lightbulb.Context specifies the type of the argument as 
lightbulb.Context. This is a type hint that tells the Python 
interpreter that the ctx argument should be an instance of
the lightbulb.Context class. 
"""
@bot.command
@lightbulb.command('ping','Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx): # ctx short for context
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f'Pong! Latency: {bot.heartbeat_latency * 1000:.2f}ms.')
    

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass #do nothing

# subcommand of my_group
@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')


# using options
@bot.command
@lightbulb.option('num2', 'The second number', type = int)
@lightbulb.option('num1', 'The first number', type = int)
@lightbulb.command('add', "Add two numbers together")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

#----------------------------
# Plugins and Extensions
#----------------------------

# load plugin from extensions/example.py
bot.load_extensions_from('./extensions')




# if __name__ == "__main__":
bot.run()


