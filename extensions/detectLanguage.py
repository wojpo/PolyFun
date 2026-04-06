import hikari
import httpx
import lightbulb
from googletrans import Translator
from googletrans.constants import LANGUAGES
from extensions import active_guesses

loader = lightbulb.Loader()

@loader.command()
class DetectLanguage(
    lightbulb.SlashCommand,
    name='detect_lang',
    description='Detect the language of a sentence',
):
    sentence = lightbulb.string('sentence', 'Enter a sentence to detect its language', max_length=1000)
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        if ctx.channel_id in active_guesses:
            await ctx.respond('A game is running in this channel. Dont cheat :<', flags=hikari.MessageFlag.EPHEMERAL)
        else:
            try:
                async with Translator() as translator:
                    result = await translator.detect(self.sentence)
                    await ctx.respond(f'Detected language: {LANGUAGES[result.lang]}', flags=hikari.MessageFlag.EPHEMERAL,)
            except (httpx.ReadTimeout, httpx.ConnectTimeout) as e:
                await ctx.respond(
            f"Detection timed out",
                    flags=hikari.MessageFlag.EPHEMERAL,)