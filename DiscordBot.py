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

@client.command()
@commands.has_permissions(administrator=True)
async def assignrole(ctx, target: discord.Member, role: discord.Role):

    await target.add_roles(role)
    await ctx.send (f'Hey {ctx.author}, {target.name} has been given the role {role.name}')


client.run(config['token'])
