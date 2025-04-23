from telebot import *
from Token import *
import sqlite3

bot = telebot.TeleBot(TOKEN, parse_mode=None) 

connection = sqlite3.connect('my_database.db')




connection.close()






@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, f'{message.from_user.username}привет')
    bot.send_message(message.from_user.id,text='привет')

@bot.message_handler(commands=['command1'])
def execute_the_command1(message):
    print("command1")
@bot.message_handler(commands=['command2'])
def execute_the_command2(message):
    print("command2")

bot.infinity_polling()