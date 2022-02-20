from dis import dis
from urllib import response
import discord
import random

TOKEN = 'OTQ0OTU4NDI3NjE5Mjc0Nzgy.YhJLHQ.ufl7sftWXiFBsP_2DKvY-OS6lgs'

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}" .format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_msg} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':

        if user_msg.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return

        elif user_msg.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
            return

        elif user_msg.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return


client.run(TOKEN)
