#!/usr/bin/python3

import configparser
from os import path
import re
import discord

client = discord.Client()

# Read config
config = configparser.ConfigParser()
if not path.isfile('config.ini'):
    config['config'] = {'status': "no YOU!",
            'token': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
config.read('config.ini')

# Login actions
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(config['config']['status']))

# Whenever someone says 'no u' the bot will say it back
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Yes, this is a regular expression. Yes, it's hard to read (It's a regex, of course it is). If you want a good explanation of what on earth is going on, I suggest you go to https://regex101.com/ and punch it in.
    #\u00FA is a letter u with an acute (that little mark above it)
    if re.search('(no|none|not|nee)\s{1,10}(u|you|thee|t[u\u00FA])', message.content, re.M|re.I|re.U):
        await message.channel.send('no u')

client.run(config['config']['token'])
