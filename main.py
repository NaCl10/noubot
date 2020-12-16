#!/usr/bin/python3

import configparser
from random import randint
from os import path
import re
from discord.ext import commands
import discord

client = commands.Bot(command_prefix = '%')

# Read config
config = configparser.ConfigParser()
if path.isfile('config.ini'):
    config.read('config.ini')
else:
    config['config'] = {'status': "echo 'R'; while true; do echo 'E'; done (also listening to %%help)",
            'token': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    config.read('config.ini')

# Login actions
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(config['config']['status']))


# Help command (We have to do this remove_command because there's a default help command, it's just garbage)
client.remove_command('help')
@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title='Help',
            color=discord.Color(0x000000))
    embed.add_field(name='%gokart', value='A fun little command. Give it a try!')
    await ctx.send(embed=embed)

# %gokart command. Will return 'Your gokart goes <random number between 1000000000 and 10000000000000> Kilometers per hour!'
@client.command(pass_context = True)
async def gokart(ctx):
    await ctx.send(f'Your gokart goes {randint(1000000000, 10000000000000)} Kilometers per hour!')

# Whenever someone says 'no u' the bot will say it back
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search(r"(no|none|not).*\n*(u|you|thee)", message.content, re.M|re.I|re.U): #Yes, this is a regular expression. Yes, it's hard to read (It's a regex, of course it is). If you want a good explanation of what on earth is going on, I suggest you go to https://regex101.com/ and punch it in.
        await message.channel.send('no u')

    # This has to be here, otherwise allll the other @client.commands won't work
    await client.process_commands(message)

client.run(config['config']['token'])
