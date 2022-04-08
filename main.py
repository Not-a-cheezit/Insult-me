import os
import discord
import csv
import random

client = discord.Client()
@client.event
async def on_ready():
  print(f"{client.user}logged in now")
@client.event
async def on_message(message):
  if message.content.startswith("$invite"):
    await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=961021837511389224&permissions=3072&scope=bot")
  print(message.content); 

@client.event
async def on_message(message):
    if message.content.startswith("$help"):
      await message.channel.send("to invite this bot to your server, use $invite.To join the offical discord server for this bot, use $server. for an insult use $insult. to send this message again use $help") 
      print(message.content) 
@client.event
async def on_message(message):
    if message.content.startswith("$server"):
      await message.channel.send("https://discord.gg/f38GdJEMKu") 
      print(message.content)
my_secret = os.environ['TOKEN']
client.run(my_secret)

