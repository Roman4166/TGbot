from telebot import *
from Token import *

import sqlite3

bot = telebot.TeleBot(TOKEN, parse_mode=None) 

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL,
                                    data TEXT
                                )
''')


connection.commit()
connection.close()



# Реагирует на команды старт и хелп и смотрит есть ли пользователь в базе если нет добавляет
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    name = message.from_user.username
    data = datetime.now().strftime("%d.%m.%Y")
    
    
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM Users WHERE  username = "{name}" '.format(name = name))
    wer = cursor.fetchall()
    for i in range(len(wer)):
        if wer[i][0] == str(name):
            print('старый пользователь')
            break
    else: 
        cursor.execute('INSERT INTO Users (username, data) VALUES (?, ?)', ( name , data ))
        print('успешно',name)
    connection.commit()
    connection.close()
    bot.reply_to(message, f'{message.from_user.username} привет')
    bot.send_message(message.from_user.id,text='привет')



#Открывает сайт КазГАУ
@bot.message_handler(commands=['command1'])
def execute_the_command1(message):
    bot.send_message(message.from_user.id,text="https://kazgau.ru/")




@bot.message_handler(commands=['command2'])
def execute_the_command2(message):
    print("command2")






bot.infinity_polling()




