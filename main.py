import hikari
import lightbulb
from dotenv import load_dotenv
import os
import extensions

load_dotenv()

try:
    intents = hikari.Intents.GUILD_MESSAGES | hikari.Intents.MESSAGE_CONTENT
    bot = hikari.GatewayBot(os.environ['DISCORD_BOT_TOKEN'], logs='DEBUG', intents=intents)
except KeyError:
    raise KeyError('You need to set up your DISCORD_BOT_TOKEN environment variable')

client = lightbulb.client_from_app(bot)
@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    await client.load_extensions_from_package(extensions)
    await client.start()

bot.run()
