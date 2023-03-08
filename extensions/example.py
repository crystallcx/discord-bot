import lightbulb
import hikari

plugin = lightbulb.Plugin('Example') # Create instance of plugin


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event): 
    print(event.content)

@plugin.command
@lightbulb.command('ping','Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def pong(ctx):
    await ctx.respond('Pong!')

# create function load that takes in an instance of the bot application
# and adds the plugin previously created to the bot to use wihtin discord
def load(bot):
    bot.add_plugin(plugin)

