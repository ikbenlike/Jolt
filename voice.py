"""
simple Discord bot using discord.py by ikbenlike
"""

import asyncio
import discord


async def connect(bot, channel_name):
    vChannel = discord.utils.find(lambda m: m.name == (
        " ".join(connectChannel)), client.get_all_channels())
    vClient = await client.join_voice_channel(vChannel)
    player = vClient.create_ffmpeg_player("sounds/empty.wav")
    player.start()
    return vClient

async def disconnect(vClient):
    vClient.disconnect()
