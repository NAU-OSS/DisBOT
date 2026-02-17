# Command file for "example"

# Imports
    # discord
import discord
from discord.ext import commands

    # (what is it/for what?)


# Class to define the example
class Example(commands.Cog):
    # initialize own self
    def __init__(self, bot):
        # set bot
        self.bot = bot

    # define command (example)
    @commands.command()
    async def example(self, ctx):
        # send an example message
        await ctx.send("This is an example!")


# add command to cog
async def setup(bot):
    # set command
    command = Example(bot)

    # add the command to cog
    await bot.add_cog(command)
