from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_cron_job(schedule, hour=23, minute=50)
    scheduler.start()
