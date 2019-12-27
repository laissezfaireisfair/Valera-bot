import telebot
import auth

bot = telebot.TeleBot(auth.token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text == '/start'):
        answ = 'Купи слона.'
    else:
        answ = 'Все говорят: \"' + message.text + '\", а ты купи слона.'
    bot.send_message(message.from_user.id, answ)

def main():
    bot.polling(none_stop=True, interval=0)

main()
