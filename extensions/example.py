import lightbulb
import hikari

plugin = lightbulb.Plugin('Example') # Create instance of plugin

# create function load that takes in an instance of the bot application
# and adds the plugin previously created to the bot to use wihtin discord
def load(bot):
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.option("text", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)