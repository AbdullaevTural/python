import telebot
from telebot import types
import requests
import time
from random import randint
import requests
import json

bot = telebot.TeleBot("", parse_mode=None)



@bot.message_handler(content_types=["text"])
def send_welcome(message): 
    data = open('user.txt','a+', encoding='utf-8')
    data.writelines(f"{str(message.from_user.id)} {message.from_user.first_name}: {message.text} \n")
    data.close()
    ch = '?'
    with open("user.txt", 'r', encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
            if line.find(ch) != -1: 
                bot.reply_to(message, 'Это вопрос?')
                # message = message.id - 1 
                # bot.reply_to(message, 'Большпавпааве!')
        
             
bot.infinity_polling()
# @bot.message_handler(conten   t_types=["text"])
# def hello_user(message):
#     data = open('user_message.txt','a+', encoding='utf-8')
#     data.writelines(f"{str(message.from_user.id)} {message.from_user.first_name}: {message.text} \n")
#     data.close()

# new_list = []
# with open("user_message.txt", 'r', encoding="utf-8") as file:
#      new_list = file.read()
# for i in new_list:
#      send_msg(i)

bot.infinity_polling()