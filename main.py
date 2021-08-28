import discord
import os

from dotenv import load_dotenv
load_dotenv()


client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('@fuck'):
        await message.channel.send("shihab er putkite gondho")


# print(f"this is the token {os.getenv('TOKEN')}")
client.run(os.getenv('TOKEN'))
