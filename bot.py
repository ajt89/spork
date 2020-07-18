import os

import discord

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!spork ping"):
        await message.channel.send("pong!")


client.run(DISCORD_BOT_TOKEN)
