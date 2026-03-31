import hikari
import lightbulb
import asyncio
from dotenv import load_dotenv
import os
from googletrans import Translator
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







# async def translate_text():
#     async with Translator() as translator:
#         result = await translator.translate('truth is my light.', dest='ja')
#         print(result.text)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
#
# asyncio.run(translate_text())