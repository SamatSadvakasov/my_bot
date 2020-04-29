import telegram
import telegram.ext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import time, datetime, timedelta

u = Updater('1102225020:AAFhHf9COV5oy4zzSPiD3DntW3wFZ1M1QgA', use_context=True)

def callback_alarm(update: telegram.Update, context: telegram.ext.CallbackContext):
    #print('Uraaaaaaaaaaaa, schedule works! ', datetime.now())
    #context.bot.send_message(chat_id=context.job.context, text='BEEP!' )
    keyboard = [
                [InlineKeyboardButton("Yes", callback_data='1'),
                 InlineKeyboardButton("No", callback_data='2')]
                 ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Have you refused to read manga?:', reply_markup=reply_markup)

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    message = ' Started !'
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=message)

    t = time(5,58,0)
    tt = datetime.now()
    delta = timedelta(seconds=10)
    ttt = datetime.now() + delta
    #context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)
    #context.job_queue.run_repeating(callback_alarm, interval=60, first=0, context=update.message.chat_id)
    context.job_queue.run_daily(callback_alarm, time=t, context = update.message.chat_id)


timer_handler = CommandHandler('timer', callback_timer)
u.dispatcher.add_handler(timer_handler)
u.start_polling()
u.idle()
