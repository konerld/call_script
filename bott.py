# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)
chat = config.chat_id


# Приветственная надпись
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

bot.polling()
