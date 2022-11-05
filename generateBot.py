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

hard_coded_data = {
  'on_msg': {

  }
}


def generate_bot(client_id: str):
  #fisierul de output
  bot_file = open(f'{client_id}.py', 'w') 

  #codul pe care il inseram initial
  input_file = open('discord_functions/init_bot.txt') 
  
  #aici vom salva codul final, pe care il inseram in bot_file
  bot_code = input_file.read() 


  # TEST CODE 
  bot_code = add_on_msg_event(bot_code)
  bot_code = add_function_to_bot(bot_code, add_mute_on_msg('yo', 1, 1, 1, 1))
  # END TEST CODE


  # ULTIMELE LINII DE COD
  bot_code += f"\nclient.run('{client_id}')"
  bot_file.write(bot_code)
  input_file.close()
  
generate_bot('MTAzODUwMDY1NzU3OTE4NDIyOA.Gc4d7a.'+'PJHSdS4eU2ffBhFScO2wH3_XMqEYi5R7qG3WYQ')
