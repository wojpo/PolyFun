import lightbulb
import hikari
from googletrans.constants import LANGUAGES
import random
loader = lightbulb.Loader()
from googletrans import Translator

@loader.command()
class GuessLanguage(
    lightbulb.SlashCommand,
    name='guess_lang',
    description='Give it a sentence and try to guess language',
):
    sentence = lightbulb.string('sentence', 'Give it a sentence which it will translate', default='hello world')
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond(
            "Translating... this may take a while",
            flags=hikari.MessageFlag.EPHEMERAL,
        )
        async with Translator() as translator:
            if self.sentence:
                result = await translator.translate(self.sentence, dest=random.choice(list(LANGUAGES.keys())))
            else:
                result = await translator.translate('hello world', dest=random.choice(list(LANGUAGES.keys())))
        embed = hikari.Embed(title='Guess the language', description=result.text, color=hikari.Color(0xff0000))
        await ctx.respond(embed=embed)