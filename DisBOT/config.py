# File containing constants and general config information.

# imports
    # reading from env file
from dotenv import load_dotenv
    # os
import os

# set command prefix
PREFIX = "!"



# load .env from root rather than current directory
dotenv_path = "../.env"
load_dotenv(dotenv_path)

# set the TOKEN for use.
TOKEN = os.getenv("DISCORD_TOKEN")
