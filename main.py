from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import auth
import logging
import dialogs
from database import PeopleDatabase

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.start)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.help)

def name(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.askSurename)

def surename(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.askBirthDay)

def birthDay(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.askBirthMonth)

def birthMonth(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.askBirthYear)

def birthYear(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=dialogs.askGender)

def gender(update, context):

def main():
    updater = Updater(token = auth.token, use_context = True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)

    startHandler = CommandHandler('start', start)
    dispatcher.add_handler(startHandler)

    helpHandler = CommandHandler('help', help)
    dispatcher.add_handler(helpHandler)

    updater.start_polling()

main()
