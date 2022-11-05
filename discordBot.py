import discord


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


if __name__ == "__main__":
  client.run('MTAzODUwMDY1NzU3OTE4NDIyOA.Gc4d7a.'+'PJHSdS4eU2ffBhFScO2wH3_XMqEYi5R7qG3WYQ')

