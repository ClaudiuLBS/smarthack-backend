from flask import Flask
from flask import request
from flask_cors import CORS
import subprocess

app = Flask('')
CORS(app)
def add_function_to_bot(bot_code: str, function: str):
  # Adauga un anumit text in cod
  bot_code += f"\n{function}\n"
  return bot_code


def add_on_msg_event(bot_code: str):
  # Adauga eventul on_message
  input_file = open('discord_functions/on_msg_event.txt')
  bot_code += f"\n{input_file.read()}\n"
  return bot_code

# Efectiv scriem if-uri in eventul de on_message
def add_msg_on_msg(user_msg: str, bot_msg: str):
  input_file = open('discord_functions/msg_on_msg.txt')
  bot_fct = input_file.read()

  bot_fct = bot_fct.replace('USER_MSG', user_msg)
  bot_fct = bot_fct.replace('BOT_MSG', bot_msg)

  input_file.close()
  return bot_fct


def add_kick_on_msg(user_msg: str):
  input_file = open('discord_functions/kick_on_msg.txt')
  bot_fct = input_file.read()

  bot_fct = bot_fct.replace('USER_MSG', user_msg)

  input_file.close()
  return bot_fct


def add_ban_on_msg(user_msg: str):
  input_file = open('discord_functions/ban_on_msg.txt')
  bot_fct = input_file.read()

  bot_fct = bot_fct.replace('USER_MSG', user_msg)

  input_file.close()
  return bot_fct


def add_mute_on_msg(user_msg: str, days: int, hours: int, minutes: int, seconds: int):
  input_file = open('discord_functions/mute_on_msg.txt')
  bot_fct = input_file.read()

  bot_fct = bot_fct.replace('USER_MSG', user_msg)
  bot_fct = bot_fct.replace('DAYS', str(days))
  bot_fct = bot_fct.replace('HOURS', str(hours))
  bot_fct = bot_fct.replace('MINUTES', str(minutes))
  bot_fct = bot_fct.replace('SECONDS', str(seconds))

  input_file.close()
  return bot_fct  

def on_member_join(bot_msg: str):
  input_file = open('discord_functions/on_member_join.txt')
  bot_fct = input_file.read()
  bot_fct = bot_fct.replace('BOT_MSG', bot_msg)

  input_file.close()
  return bot_fct


def generate_bot(bot_data: dict):
  client_id = bot_data["token"]
  #fisierul de output
  bot_file = open(f'{client_id}.py', 'w') 

  #codul pe care il inseram initial
  input_file = open('discord_functions/init_bot.txt') 
  
  #aici vom salva codul final, pe care il inseram in bot_file
  bot_code = input_file.read() 


  # ADD ON MESSAGE FUNCTIONS
  bot_code = add_on_msg_event(bot_code)
  other_things = []
  for item in bot_data['features']:
    if item['action'] == 'msg':
      bot_code = add_function_to_bot(bot_code, add_msg_on_msg(item['user_msg'], item['params'][0]))
    elif item['action'] == 'kick':
      bot_code = add_function_to_bot(bot_code, add_kick_on_msg(item['user_msg']))
    elif item['action'] == 'ban':
      bot_code = add_function_to_bot(bot_code, add_ban_on_msg(item['user_msg']))
    elif item['action'] == 'mute':
      bot_code = add_function_to_bot(bot_code, add_mute_on_msg(
        item['user_msg'], 
        item['params'][0],
        item['params'][1],
        item['params'][2],
        item['params'][3],
      ))
    else:
      other_things.append(item)
  
  for item in other_things:
    if item['action'] == 'on_join':
      bot_code = add_function_to_bot(bot_code, on_member_join(item['params'][0]))


  # ULTIMELE LINII DE COD
  bot_code += f"\nclient.run('{client_id}')"
  bot_file.write(bot_code)
  input_file.close()


@app.route('/generate-bot', methods=['POST'])
def generateBot():
  data = request.json
  generate_bot(data)
  subprocess.Popen(["python3",f"{data['token']}.py"])
  return data

def run():
  app.run(host='0.0.0.0',port=8000)

run()


# generate_bot('MTAzODUwMDY1NzU3OTE4NDIyOA.Gc4d7a.'+'PJHSdS4eU2ffBhFScO2wH3_XMqEYi5R7qG3WYQ', hard_coded_data)
