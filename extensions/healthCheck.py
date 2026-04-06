import hikari
import lightbulb

loader = lightbulb.Loader()

@loader.command()
class HealthCheck(
    lightbulb.SlashCommand,
    name='health_check',
    description='Checks if bot is currently running',
):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond('Bot is running properly ;3', flags=hikari.MessageFlag.EPHEMERAL)