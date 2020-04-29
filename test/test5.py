from telegram.ext import Updater, CommandHandler
import datetime

def daily_job(bot, update, job_queue):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    bot.send_message(chat_id=339450455, text='Setting a daily notifications!')
    t = datetime.time(7, 50, 0, 0)
    job_queue.run_daily(notify_assignees, t, days=tuple(range(5)), context=update)

def notify_assignees(bot, job):
    bot.send_message(chat_id=339450455, text="Some text!")

updater = Updater('1102225020:AAFhHf9COV5oy4zzSPiD3DntW3wFZ1M1QgA', use_context=True)
updater.dispatcher.add_handler(CommandHandler('notify', daily_job, pass_job_queue=True))
updater.start_polling()
updater.idle()
