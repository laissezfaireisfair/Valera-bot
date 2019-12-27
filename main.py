import telegram.ext
import auth
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Купи слона')

def echo(update, context):
    answerText = 'Все говорят: \"' + update.message.text + '\", а ты купи слона'
    context.bot.send_message(chat_id=update.effective_chat.id, text=answerText)

def main():
    updater = telegram.ext.Updater(token = auth.token, use_context = True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)
    startHandler = telegram.ext.CommandHandler('start', start)
    dispatcher.add_handler(startHandler)
    echoHandler = telegram.ext.MessageHandler(telegram.ext.Filters.text, echo)
    dispatcher.add_handler(echoHandler)
    updater.start_polling()

main()
