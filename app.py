import praw
import os
import time
import json
from datetime import datetime 
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()

def echo(text):
    print(f"[{datetime.now()}] {text}")

with open('jobs.json', 'r') as f:
    data = json.load(f)

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

for job in data['jobs']:
    print("Subreddit:", job['subreddit'])
    print("Date:", f"{job['year']}-{job['month']}-{job['day']} {job['hour']}:{job['minute']}")
    print("Content file:", job['content_location'])
    print("------")

# scheduler = BackgroundScheduler()

# # Define your jobs
# scheduler.add_job(echo, 'date', run_date=datetime(2025, 6, 25, 1, 8), args=["Job 1: 10:30"])
# scheduler.add_job(echo, 'date', run_date=datetime(2025, 6, 25, 1, 9), args=["Job 2: 11:00"])
# scheduler.add_job(echo, 'date', run_date=datetime(2025, 6, 25, 1, 10), args=["Job 3: 12:00"])

# scheduler.start()
# print("All jobs scheduled. Waiting...")

# try:
#     while True:
#         time.sleep(1)
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()