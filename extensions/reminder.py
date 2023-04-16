import hikari
import lightbulb
import datetime

plugin = lightbulb.Plugin('reminders')

def load(bot):
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('reminders', 'Reminder Group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def reminders(ctx):
    pass #do nothing

# subcommand of my_group
@reminders.child
@lightbulb.command('show', 'Show reminders')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')
    embed = hikari.Embed(
        title="Reminders!",
        description=message,
    )
    await ctx.app.rest.create_message(
        channel=channel.id,
        content=ping.mention if ping else hikari.UNDEFINED,
        embed=embed,
        role_mentions=True,
    )
    await ctx.respond(
        f"Announcement posted to <#{channel.id}>!", flags=hikari.MessageFlag.EPHEMERAL
    )

# subcommand of my_group
@reminders.child
@lightbulb.option('reminder', 'e.g. +$40 shoes', type = str)
@lightbulb.command('add', 'Add reminder to list')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond(ctx.options.reminder)
