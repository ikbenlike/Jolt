import asyncio
import discord

"""
Math commands for the Jolt discord bot
"""

async def isodd(bot, message):
    num = message.content.split(" ")[1]
    if str(int(num) % 2 == 0):
        print("yes")
        await bot.send_message(message.channel, str(num) + " isn't odd")
    else:
        await bot.send_message(message.channel, str(num) + " is odd")
