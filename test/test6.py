import telegram
import telegram.ext
from telegram.ext import Updater
from telegram.ext import CommandHandler

u = Updater('1102225020:AAFhHf9COV5oy4zzSPiD3DntW3wFZ1M1QgA', use_context=True)
# j = u.job_queue

# def callback_minute(context: telegram.ext.CallbackContext, update: telegram.Update):
#     context.bot.send_message(chat_id=update.message.chat_id, 
#                              text='One message every minute')

# job_minute = j.run_repeating(callback_minute, interval=60, first=0)

def callback_alarm(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='BEEP')

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a timer for 1 minute!')

    context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)

timer_handler = CommandHandler('timer', callback_timer)
u.dispatcher.add_handler(timer_handler)
u.start_polling()
u.idle()
