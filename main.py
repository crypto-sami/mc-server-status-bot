from mcstatus import JavaServer
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.user import User
import json

def check_online():
    server = JavaServer.lookup("mc.sturk.au")
    status = server.status()
    return(f"The server has {status.players.online} player(s) online")
intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix='?', intents=intents)
TOKEN = json.loads(open("token.json", "r").read())


@bot.event
async def on_message(message):
    command = message.content.split(" ")

    if message.content == ("?online"):
        server = JavaServer.lookup("mc.sturk.au:25565")
        status=server.status()
        embedVar=discord.Embed(title="Current Online Players", url="", color=0x00ff00)
        msg = check_online()
        embedVar.add_field(name="Contents", value=f"{msg}")
        for player in status.players.sample:
            embedVar.add_field(name="Contents", value=f"The player %s is online" % player.name)
           
        
      
        await message.reply(embed=embedVar)

bot.run(TOKEN)