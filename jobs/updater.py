from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule, 'date', run_date=datetime(2021, 8, 13, 21, 17))
    scheduler.start()
