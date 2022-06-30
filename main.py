import telebot
bot = telebot.TeleBot("5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI")


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,'<b>Привет!</b>',parse_mode = 'html')

bot.polling(none_stop = True)
