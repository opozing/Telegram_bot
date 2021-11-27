import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Какую вы хотите пиццу? '
                                      'Большую или маленькую?')


@bot.message_handler(func=lambda m: True)
def question1(message):
    global size
    if message.text.lower() == ('большую').lower() or (
            message.text.lower() == ('маленькую').lower()):
        size = message.text
        bot.send_message(message.chat.id, 'Как вы будете платить?')
        bot.register_next_step_handler(message, question2)
    else:
        bot.send_message(message.chat.id, 'Недопустимый размер пиццы')


def question2(message):
    global cash
    if message.text.lower() == ('наличкой').lower():
        cash = message.text
        bot.send_message(message.chat.id, f'Вы хотите {size} пиццу, '
                                          f'оплата - {cash}?')
        bot.register_next_step_handler(message, question3)
    else:
        bot.send_message(message.chat.id, 'Недопустимый вид оплаты')
        bot.register_next_step_handler(message, question2)


def question3(message):
    if message.text.lower() == ('да').lower():
        bot.send_message(message.chat.id, 'Спасибо за заказ')
    else:
        bot.send_message(message.chat.id, f'Вы хотите {size} пиццу, '
                                          f'оплата - {cash}?')
        bot.register_next_step_handler(message, question3)


bot.polling(none_stop=True)
