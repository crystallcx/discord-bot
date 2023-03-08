import hikari
import lightbulb
import datetime

plugin = lightbulb.Plugin('Birthdays')

def load(bot):
    bot.add_plugin(plugin)

birthdays = {}

@plugin.command
@lightbulb.option('date','Please enter date of birth in format: DD/MM/YYYY')
@lightbulb.command('setbirthday','set your birthday', pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def setbirthday(ctx: lightbulb.Context, date: str) -> None:
    user_id = ctx.author.id
    try:
        birthday = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    except ValueError or TypeError:
        await ctx.respond("Invalid date format. Please use the format 'DD/MM/YYYY'.")
        return
    birthdays[user_id] = birthday
    await ctx.respond("Got it, I'll remember your birthday!")