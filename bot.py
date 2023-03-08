import hikari
import lightbulb
import os

# Access the value of your secret through an environment variable
my_secret = os.environ.get('BOT_TOKEN')

# bot = hikari.GatewayBot(token='<TOKEN>')
bot = lightbulb.BotApp(
    token = my_secret,
    default_enabled_guilds=(997729114968555540, 486517628404498432)) # register commands only to specified guild (discord server)

# token taken from https://discord.com/developers/applications/997331587966447678/bot

@bot.listen(hikari.StartedEvent) # triggers when bot is started
async def bot_started(event): # function header
    print('Bot has started')

#----------------------------
# Slash Commands
#----------------------------
# order in which these appear above funciton header is important
# @bot.command
# @lightbulb.command('ping','Says pong!')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx): # ctx short for context
#     await ctx.respond('Pong!')

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




bot.run()



