import hikari
import lightbulb
import asyncio
from dotenv import load_dotenv
import os
from googletrans.constants import LANGUAGES
import extensions

load_dotenv()

try:
    bot = hikari.GatewayBot(os.environ['DISCORD_BOT_TOKEN'], logs='DEBUG')
except KeyError:
    raise KeyError('You need to set up your DISCORD_BOT_TOKEN environment variable')

client = lightbulb.client_from_app(bot)
@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    await client.load_extensions_from_package(extensions)
    await client.start()

bot.run()
