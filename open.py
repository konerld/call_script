# -*- coding: utf-8
import config
import telebot
import subprocess
import time

bot = telebot.TeleBot(config.token)
chat = config.chat_id

def log(message, answer):
    from datetime import datetime
    print("\n"+"="*20)
    print(datetime.now())
    print("Message from: {} {} (id = {}) \nText: {} ".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("Answer: %s" % answer)

#a Инициализируем кнопки с их содержимым
user_markup = telebot.types.ReplyKeyboardMarkup()
user_markup.row("/NASH", "/MAGNOLIYA", "/BOPOTA")


@bot.message_handler(commands=["start"])
def button_action (message):
    bot.send_message(chat_id=chat, text='WHAT DO YOU WANT TO OPEN?', reply_markup=user_markup)

@bot.message_handler(commands=["NASH"])
def call1 (message):
        answer="Открываю НАШ шлагбаум (возле подъезда.)"
        log(message, answer)
        bot.send_message(chat_id=chat, text=answer, reply_markup=user_markup)
        #subprocess.call('echo -e "ATD+79104445691;\n;\r" > /dev/ttyUSB1', shell=True)

@bot.message_handler(commands=["МАГНОЛИЯ"])
def call2 (message):
        answer="Открываю шлагбаум возле магазина МАГНОЛИЯ."
        log(message, answer)
        bot.send_message(chat_id=chat, text=answer, reply_markup=user_markup)

@bot.message_handler(commands=["ВОРОТА"])
def call3 (message):
        answer="Открываю ВОРОТА в аркe."
        log(message, answer)
        bot.send_message(chat_id=chat, text=answer, reply_markup=user_markup)

"""
    else:
        answer="Неверная команда! \n Повторите попытку."
        log(message, answer)
        bot.send_message(chat_id="-1001251940194", text=answer)
"""
#bot.polling(none_stop=True)

if __name__ == '__main__':
#    bot.polling(none_stop=True)
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)  # или просто print(e) если у вас логгера нет,
            # или import traceback; traceback.print_exc() для печати полной инфы
            time.sleep(15)



