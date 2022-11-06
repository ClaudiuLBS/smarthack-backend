import discord


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
  print('yeads')
  await member.send("Welcome son!")

if __name__ == "__main__":
  client.run('MTAzODUwMDY1NzU3OTE4NDIyOA.Gc4d7a.'+'PJHSdS4eU2ffBhFScO2wH3_XMqEYi5R7qG3WYQ')

