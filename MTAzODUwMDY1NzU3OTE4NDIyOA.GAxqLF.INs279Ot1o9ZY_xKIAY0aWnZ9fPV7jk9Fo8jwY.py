import discord
from datetime import timedelta

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if 'yo' in message.content:
    timeout_duration = timedelta(days=1, hours=1, minutes=1, seconds=1)
    await message.author.timeout(timeout_duration)

client.run('MTAzODUwMDY1NzU3OTE4NDIyOA.GAxqLF.INs279Ot1o9ZY_xKIAY0aWnZ9fPV7jk9Fo8jwY')