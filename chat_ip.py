# -*- coding: utf-8
import config
import telebot
import time

bot = telebot.TeleBot(config.token)
chat = config.chat_id


#updates = bot.get_updates()
#print([u.message.text for u in updates])


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

'''
def log(message, answer):
    from datetime import datetime
    print("\n"+"="*20)
    print(datetime.now())
    print("Message from: {} {} (id = {}) \nText: {} ".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("Answer: %s" % answer)

@bot.message_handler(commands=["start"])
def button_action (message):
    bot.send_message(chat_id=chat, text='WHAT DO YOU WANT TO OPEN?', reply_markup=user_markup)
'''

if __name__ == '__main__':
#    bot.polling(none_stop=True)
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print('1')
	    #print(e)  # или п�~@о�~A�~Bо print(e) е�~Aли �~C ва�~A логге�~@а не�~B,
            # или import traceback; traceback.print_exc() дл�~O пе�~Gа�~Bи полной ин�~D�~K
            #time.sleep(15)

