"""
simple Discord bot using discord.py by ikbenlike
"""

import asyncio
import time
import json
import socket
import logging
import discord

logging.basicConfig(level=logging.ERROR)


def load_config():
    """
    loads config
    """
    with open("config/config.json") as config_file:
        return json.load(config_file)

async def reload_config(config):
    """
    reloads config
    """
    await asyncio.sleep(0)  # only here to satisfy pylint
    with open("config/config.json", "w") as config_file:
        config_file.write(json.dumps(config, sort_keys=True, indent=4))
    with open("config/config.json") as config_file:
        return json.load(config_file)

async def has_permission(config, user_id):
    """
    checks if the user with user_id has enough permissions
    """
    return user_id in config["mods"] or config["owner_id"] == user_id

async def exit_bot(bot, message):
    """
    logs out of the bot
    """
    await bot.send_message(message.channel, "[exiting " + bot.user.name + "]")
    await bot.logout()

async def set_game(bot, message):
    """
    sets the game-status
    """
    game = discord.Game()
    game.name = (" ".join(message.content.split(" ")[1:]))
    await bot.change_status(game=game)
    await bot.send_message(message.channel, "game has been set to `" + game.name + "`")

async def set_prefix(bot, message, config):
    """
    sets command prefix
    """
    config["prefix"] = message.content.split(" ")[1]
    await bot.send_message(message.channel, "set prefix to " + config["prefix"])
    return await reload_config(config)

async def get_host(bot, message):
    """
    gets IP-address of a site
    """
    site = " ".join(message.content.split(" ")[1:])
    res = "\n".join([s[4][0] for s in socket.getaddrinfo(site, "443")])
    await bot.send_message(message.channel, "```" + res + "```")

async def echo(bot, message):
    msg = message.content.split(" ")
    print(msg)
    if msg[1] == "-t":
        await asyncio.sleep(float(msg[2]))
        await bot.send_message(message.channel, message.author.mention + " " +
                              (" ".join(msg[3:])))
    else:
        await bot.send_message(message.channel, message.author.mention + " " +
                          (" ".join(message.content.split(" ")[1:])))
