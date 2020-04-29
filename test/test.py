import telegram
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


updater = Updater(token='1102225020:AAFhHf9COV5oy4zzSPiD3DntW3wFZ1M1QgA', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
