"""
simple Discord bot using discord.py by ikbenlike
"""

import asyncio
import discord
import utils
import search
import jolt_math
import misc


BOT = discord.Client()


def get_config():
    """
    only exists to get a higher pylint score
    """
    config = utils.load_config()
    return config


@BOT.event
async def on_ready():
    """
    runs on ready
    """
    print("logged in as: " + BOT.user.name + " - " + BOT.user.id)


@BOT.event
async def on_message(message):
    """
    runs when a message is received
    """
    config = utils.load_config()
    #await BOT.change_nickname(message.server.me, None)
    if message.content.startswith(config["prefix"] + "perm"):
        await BOT.send_message(message.channel, str(await utils.has_permission(config, message.author.id)))
    elif message.content.startswith(config["prefix"] + "exit"):
        if await utils.has_permission(config, message.author.id):
            await utils.exit_bot(BOT, message)
        else:
            await BOT.send_message(message.channel, "<@" + message.author.id + "> you do not have permission to do that")
    elif message.content.startswith(config["prefix"] + "game"):
        if await utils.has_permission(config, message.author.id):
            await utils.set_game(BOT, message)
        else:
            await BOT.send_message(message.channel, "<@" + message.author.id + "> you do not have permission to do that")
    elif message.content.startswith(config["prefix"] + "prefix"):
        if await utils.has_permission(config, message.author.id):
            config = await utils.set_prefix(BOT, message, config)
        else:
            await BOT.send_message(message.channel, "<@" + message.author.id + "> you do not have permission to do that")
    elif message.content.startswith(config["prefix"] + "host"):
        await utils.get_host(BOT, message)
    elif message.content.startswith(config["prefix"] + "echo"):
        print(message.content.split(" ")[1])
        await utils.echo(BOT, message)
    elif message.content.startswith(config["prefix"] + "google"):
        await search.google(BOT, message)
    elif message.content.startswith(config["prefix"] + "lmgtfy"):
        await search.lmgtfy(BOT, message)
    elif message.content.startswith(config["prefix"] + "bing"):
        await search.bing(BOT, message)
    elif message.content.startswith(config["prefix"] + "ddg"):
        await search.ddg(BOT, message)
    elif message.content.startswith(config["prefix"] + "aol"):
        await search.aol(BOT, message)
    elif message.content.startswith(config["prefix"] + "xkcd"):
        await misc.xkcd(BOT, message)
    elif message.content.startswith(config["prefix"] + "echo"):
        await misc.echo(BOT, message)
    elif message.content.startswith(config["prefix"] + "isodd"):
        await jolt_math.isodd(BOT, message)


BOT.run(get_config()["token"])
