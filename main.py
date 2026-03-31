import hikari
import lightbulb
import asyncio
import os
from googletrans import Translator


try:
    bot = hikari.GatewayBot(os.environ['DISCORD_BOT_TOKEN'], logs='DEBUG')
except KeyError:
    raise KeyError('You need to set up your DISCORD_BOT_TOKEN environment variable')

async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    """If a non-bot user mentions your bot, respond with 'Pong!'."""

    # Do not respond to bots nor webhooks pinging us, only user accounts
    if not event.is_human:
        return

    me = bot.get_me()

    if me.id in event.message.user_mentions_ids:
        await event.message.respond("Pong!")








# async def translate_text():
#     async with Translator() as translator:
#         result = await translator.translate('truth is my light.', dest='ja')
#         print(result.text)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
#
# asyncio.run(translate_text())