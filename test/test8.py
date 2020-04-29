import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from datetime import time, datetime, timedelta

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    keyboard = [
                [InlineKeyboardButton("Yes", callback_data='1'),
                 InlineKeyboardButton("No", callback_data='2')]
                 ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    print(context)
    update.message.reply_text('Have you refused to read manga?:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.data)
    query.edit_message_text(text="Selected option: {}".format(query.data))

def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def callback_timer(update, context):
    message = ' Started !'
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=message)

    t = time(5,53,0)
    context.job_queue.run_daily(start, time=t, context = update.message.chat_id)


updater = Updater("1102225020:AAFhHf9COV5oy4zzSPiD3DntW3wFZ1M1QgA", use_context=True)
updater.dispatcher.add_handler(CommandHandler('timer', callback_timer))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
updater.idle()
