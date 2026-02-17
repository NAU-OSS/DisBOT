# File for general helper functions

# Imports
    # datea and time
import datetime


# Helper Functions
    # retrieve current time
def get_timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
