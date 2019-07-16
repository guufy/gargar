

import discord
import random

TOKEN = 'NDgzMjM1Njg1MzI3OTYyMTEz.DmQgMQ.OkF0FAjw6HJaakJQp3wPOpmhgO8'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == ('i hate'):
        msg = 'mondays'.format(message)
        await client.send_message(message.channel, msg)

    if random.randint(0,1000) < 1:
        msg = 'wheres my pipe'.format(message)
        await client.send_message(message.channel, msg)

    if ('shid') in message.content:
        msg = 'ofuk {0.author.mention} shidded'.format(message)
        await client.send_message(message.channel, msg)

    if ('camed') in message.content:
        msg = 'ofuk {0.author.mention} camed'.format(message)
        await client.send_message(message.channel, msg)

    if ('fard') in message.content:
        msg = 'ofuk {0.author.mention} farded'.format(message)
        await client.send_message(message.channel, msg)

    if ('pee') in message.content:
        msg = 'ofuk {0.author.mention} peed'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == ('?help'):
        msg = '?hello\nshid\ncamed\nfard\npee'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == ("?gargar"):
        await client.send_file(message.channel,"gargar/" + str(random.randint(1,174)) + ".png")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
