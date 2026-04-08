import asyncio
import time
import random
import hikari
import httpx
import lightbulb
from googletrans import Translator
from googletrans.constants import LANGUAGES
from extensions import active_guesses

loader = lightbulb.Loader()

@loader.listener(hikari.MessageCreateEvent)
async def on_guess_message(event: hikari.MessageCreateEvent) -> None:
    if event.is_bot:
        return

    channel_id = event.channel_id
    current_time = time.time()

    if channel_id in active_guesses and current_time < active_guesses[channel_id]['expiry']:
        expected = active_guesses[channel_id]['expected'].lower()
        guess = event.message.content.strip().lower() if event.message.content else ""

        if guess == expected or guess == expected.split('(')[0].strip():
            await event.message.add_reaction("✅")
            embed = hikari.Embed(title=f'{event.author} guessed correctly', description=f'The language was {expected}', color=0x00ff00)
            await event.message.respond(embed=embed)
            del active_guesses[channel_id]
        else:
            await event.message.add_reaction("❌")
    else:
        active_guesses.pop(channel_id, None)

@loader.command()
class GuessLanguage(
    lightbulb.SlashCommand,
    name='guess_lang',
    description='Provide a sentence and try to guess the language',
):
    sentence = lightbulb.string('sentence', 'Enter a sentence to translate', default='hello world', max_length=200)

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond(
            "Translating... this may take a while",
            flags=hikari.MessageFlag.EPHEMERAL,
        )

        lang_code = random.choice(list(LANGUAGES.keys()))
        lang_name = LANGUAGES[lang_code]
        try:
            async with Translator() as translator:
                text_to_translate = self.sentence if self.sentence else 'hello world'
                result = await translator.translate(text_to_translate, dest=lang_code)
                while result.text == text_to_translate:
                    lang_code = random.choice(list(LANGUAGES.keys()))
                    lang_name = LANGUAGES[lang_code]
                    result = await translator.translate(text_to_translate, dest=lang_code)
        except (httpx.ReadTimeout, httpx.ConnectTimeout) as e:
            await ctx.respond(
        f"Translation timed out for language `{lang_name}`. Please try again.",
                flags=hikari.MessageFlag.EPHEMERAL,
        )
            return

        embed = hikari.Embed(
            title="Guess the language!",
            description=result.text,
            color=hikari.Color(0xffaa00)
        )
        embed.set_footer(text="Type the language name (in English) in this channel to guess! You have 60 seconds btw.")

        await ctx.respond(embed=embed)

        expiry_time = time.time() + 60
        active_guesses[ctx.channel_id] = {
            'expected': lang_name,
            'expiry': expiry_time
        }

        await asyncio.sleep(60)
        if ctx.channel_id in active_guesses and active_guesses[ctx.channel_id]['expiry'] == expiry_time:
            del active_guesses[ctx.channel_id]
            no_time_embed = hikari.Embed(title="Time's up. No one guessed correctly", description=f'The language was {lang_name}', color=0xff0000)
            await ctx.respond(
                embed=no_time_embed
            )