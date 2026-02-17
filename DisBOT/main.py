# File containing the main core. Used to actually start the bot.

# Imports
    # os and async
import os
import asyncio
    # discord
import discord
from discord.ext import commands

    # constants / config
from config import TOKEN, PREFIX


# set intents
intents = discord.Intents.default()
intents.message_content = True

# set bot
bot = commands.Bot(command_prefix = PREFIX, 
                   intents = intents)


# function to load all commands in
async def load_commands():
    # load all commands files in the commands folder
    for filename in os.listdir("./commands"):

        # check if its a py file and make sure its not private
        if filename.endswith(".py") and not filename.startswith("__"):

            # then load in all the files (commands)
            curr_file = filename[:-3]
            await bot.load_extension(f"commands.{curr_file}")


# on an event, that being if the bad is ready
@bot.event
async def on_ready():
    # in the terminal, note that the bot as started and its username
    print(f"Logged in as {bot.user}")


# MAIN. Starts running the actual bot.
async def main():
    async with bot:
        # load the commands
        await load_commands()
        # start the bot
        await bot.start(TOKEN)


# run main with async to allow multiple commands
if __name__ == "__main__":
    asyncio.run(main())
