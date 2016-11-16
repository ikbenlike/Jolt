"""
simple Discord bot using discord.py by ikbenlike
"""

import asyncio
import time
import urllib
import requests
import json

async def xkcd(bot, message):
    """
    This function sends an xkcd comic
    """
    try:
        stuff = message.content.split(" ")[1]
        res = requests.get("http://xkcd.com/" + stuff + "/info.0.json")
    except IndexError:
        res = requests.get("http://xkcd.com/info.0.json")

    if res.status_code == 200:
        await bot.send_message(message.channel, res.json()["img"] + "\nTitle: " + res.json()["title"])
    else:
        await bot.send_message(message.channel, "an error occured")

#async def set_game(bot, message):
