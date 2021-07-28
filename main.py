import telebot

bot = telebot.TeleBot('1804284473:AAFmcKNmHK0Tc4cD1SJ3MqCvLoptSbJYzPQ')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я милашка бот. Приятно познакомиться {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    predicat = message.text.lower()
    if predicat == 'привет' or predicat == 'здравствуйте':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
