import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "Hi":
        await client.send_message(message.channel, "hello, type help")
    if message.content == "help":
        await client.send_message(message.channel, "mafia\nmaniac")
    if message.content == "mafia":
        await client.send_message(message.channel, random.choice(["I think who votes against me", "I will agree with the most players", "Anna", "Phantom"]))

client.run("NDY3NzMyMTgzODQ3NjY1NjY0.DjTyFQ.gjcMyAuCvvmXj7WctLtn3ex7v1c") #Replace token with your bots token
