import hikari
import lightbulb
import datetime
from typing import Optional

plugin = lightbulb.Plugin('announcement')

def load(bot):
    bot.add_plugin(plugin)

# 4 options can be passed into command.

@plugin.command
@lightbulb.option(
    "ping", "Role to ping with announcement.", type=hikari.Role, required=False
)
@lightbulb.option(
    "image", "Announcement attachment.", type=hikari.Attachment, required=False
)
@lightbulb.option(
    "channel", "Channel to post announcement to.", type=hikari.TextableChannel
)
@lightbulb.option("message", "The message to announce.", type=str)
@lightbulb.command("announce", "Make an announcement!", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def announce(
    ctx: lightbulb.SlashContext,
    message: str,
    channel: hikari.GuildTextChannel,
    image: Optional[hikari.Attachment] = None,
    ping: Optional[hikari.Role] = None,
) -> None:
    embed = hikari.Embed(
        title="Announcement!",
        description=message,
    )
    embed.set_image(image)
    await ctx.app.rest.create_message(
        channel=channel.id,
        content=ping.mention if ping else hikari.UNDEFINED,
        embed=embed,
        role_mentions=True,
    )
    await ctx.respond(
        f"Announcement posted to <#{channel.id}>!", flags=hikari.MessageFlag.EPHEMERAL
    )