import discord
import asyncio
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

# قائمة الرسائل العشوائية
random_messages = [
  "Good morning, everyone! Have a fantastic day ahead!",
  "Did you know? Cats can jump up to six times their body length in one leap!",
  "Reminder: Drink water and stay hydrated throughout the day.",
  "How's everyone doing today? Let's spread some positivity!",
  "Fun fact: The Earth's oceans contain nearly 20 million tons of gold!",
  "Take a deep breath and remember to relax. You've got this!",
  "Today's challenge: Do something kind for a stranger.",
  "Just a friendly reminder to take breaks and stretch if you've been sitting for a while.",
  "In case nobody told you today: You are amazing and capable of great things!",
  "Fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    # يمكنك إضاف المزيد من الرسائل هنا
]

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('------')
    await send_message_every_minute()

async def send_message_every_minute():
    await client.wait_until_ready()
    channel = client.get_channel(1222311774255321158)
    if not channel:
        print('Invalid channel ID.')
        return

    while not client.is_closed():
        # اختيار رسالة عشوائية من القائمة
        random_message = random.choice(random_messages)
        await channel.send(random_message)
        await asyncio.sleep(3600)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(os.environ['token'])
