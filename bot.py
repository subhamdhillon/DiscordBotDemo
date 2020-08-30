import os
import random
import re
import discord
from dotenv import load_dotenv

import google_search
import google_api
import database_demo

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# google_api_obj = google_api.GoogleApi()

database_demo_obj = database_demo.DatabaseDemo()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    message_content = message.content.lower()

    google_regex = "^!google.*$"

    recent_regex = "^!recent.*$"    

    # print("message_content",message_content)

    greet_quotes = [
        'hi',
        'hey',
        'hello',
        'howdy'
    ]

    # response  = 'default_response'

    if message_content in greet_quotes:
        # print('a greeting message')
        response = 'Hi,I am just a bot!'
        await message.channel.send(response)

    elif (re.search(google_regex, message_content)):
        # print("google_regex")
        query = message_content[7:].strip()
        response = "blank google search query"
        # print(query)
        if(query):
            database_demo_obj.put_data(query)
            # response = str(google_api_obj.get_resp(query))
            response = str(google_search.perform_search(query))
        await message.channel.send(response)

    elif (re.search(recent_regex, message_content)):
        # print('recent_regex')
        query = message_content[7:].strip()
        # print(query)
        response = "blank recent search query"
        if(query):
            response = database_demo_obj.get_data(query)
            # database_demo_obj.put_data(query)
        # response = "recent regex"
        await message.channel.send(response)
    else:
        print('no match')

    # await message.channel.send(response)

client.run(TOKEN)