import discord
from discord.ext import commands

import json

with open('config.json') as config_file:
    config = json.load(config_file)


client = commands.Bot(command_prefix = config['prefix'])

#Notification for when the bot is read to use. 
@client.event
async def on_ready():
    print('Bot is ready and here to use. Logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    print('A message was sent by {0.author}: {0.content}'.format(message))

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! {round(client.latency * 1000)}ms')



client.run(config['token'])
