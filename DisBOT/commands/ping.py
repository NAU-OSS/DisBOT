# Command file for "ping"


# Imports
    # discord
import discord
from discord.ext import commands

    # own helper functs
from utils.helpers import get_timestamp


# Class to define the ping command
class Ping(commands.Cog):
    # initialize own self
    def __init__(self, bot):
        # set bot
        self.bot = bot

    # define command (ping)
    @commands.command()
    async def ping(self, ctx):
        # get the current time
        curr_time = get_timestamp()

        # and then reply with the ping message and currenttime
        await ctx.send(f"Ping - Time: {curr_time}")


# add command to cog
async def setup(bot):
    # set command
    command = Ping(bot)

    # add the command to cog
    await bot.add_cog(command)
