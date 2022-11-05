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

  if 'hello' in message.content:
    await message.channel.send('nu te salut')

  if 'no' in message.content:
    await message.channel.send('adw')

  if 'adware' in message.content:
    await message.channel.send('aoeip')

  if 'aoeip' in message.content:
    await message.author.kick()

  if 'awdpokmaoeip' in message.content:
    await message.author.kick()

  if 'ban' in message.content:
    await message.author.ban()

  if 'mute' in message.content:
    timeout_duration = timedelta(days=0, hours=1, minutes=10, seconds=15)
    await message.author.timeout(timeout_duration)

client.run('MTAzODUwMDY1NzU3OTE4NDIyOA.GAxqLF.INs279Ot1o9ZY_xKIAY0aWnZ9fPV7jk9Fo8jwY')