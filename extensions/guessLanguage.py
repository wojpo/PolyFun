import lightbulb
import hikari

loader = lightbulb.Loader()

@loader.command()
class GuessLanguage(
    lightbulb.SlashCommand,
    name='guess_lang',
    description='Give it a sentence a',
):
    sentence = lightbulb.string('sentence', 'Give it a sentence which it will translate', default='hello world')
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond(
            "Fetching... this may take a while ⏳",
            flags=hikari.MessageFlag.EPHEMERAL,
        )