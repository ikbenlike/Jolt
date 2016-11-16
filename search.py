"""
simple Discord bot using discord.py by ikbenlike
"""

import asyncio
import urllib

async def google(bot, message):
    """
    search on google
    """
    await bot.send_message(message.channel, "https://google.com/#q=" +
                           urllib.parse.quote((" ".join(message.content.split(" ")[1:]))))

async def lmgtfy(bot, message):
    """
    search on lmgtfy (google)
    """
    await bot.send_message(message.channel, "http://lmgtfy.com/?q=" +
                           urllib.parse.quote((" ".join(message.content.split(" ")[1:]))))

async def bing(bot, message):
    """
    search on bing
    """
    if message.content.split(" ")[1] == "-i":
        await bot.send_message(message.channel, "https://bing.com/images/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-v":
        await bot.send_message(message.channel, "https://bing.com/videos/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-n":
        await bot.send_message(message.channel, "https://bing.com/news/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-m":
        await bot.send_message(message.channel, "https://bing.com/maps/default.aspx?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-w":
        await bot.send_message(message.channel, "https://bing.com/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    else:
        await bot.send_message(message.channel, "https://bing.com/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[1:]))))

async def ddg(bot, message):
    """
    search on duckduckgo
    """
    if message.content.split(" ")[1] == "-i":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=images")
    elif message.content.split(" ")[1] == "-v":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=videos")
    elif message.content.split(" ")[1] == "-w":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=web")
    elif message.content.split(" ")[1] == "-m":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=meanings")
    elif message.content.split(" ")[1] == "-a":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=about")
    elif message.content.split(" ")[1] == "-d":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=definition")
    elif message.content.split(" ")[1] == "-l":
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))) +
                               "&ia=lyrics")
    else:
        await bot.send_message(message.channel, "https://duckduckgo.com/?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[1:]))) +
                               "&ia=web")

async def aol(bot, message):
    """
    search on America Online
    """
    if message.content.split(" ")[1] == "-i":
        await bot.send_message(message.channel, "http://search.aol.com/aol/image?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-w":
        await bot.send_message(message.channel, "http://search.aol.com/aol/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-v":
        await bot.send_message(message.channel, "http://search.aol.com/aol/video?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    elif message.content.split(" ")[1] == "-n":
        await bot.send_message(message.channel, "http://search.aol.com/aol/news?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[2:]))))
    else:
        await bot.send_message(message.channel, "http://search.aol.com/aol/search?q=" +
                               urllib.parse.quote((" ".join(message.content.split(" ")[1:]))))
