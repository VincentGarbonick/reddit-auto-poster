import praw
import os
import time
import json
from datetime import datetime 
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()
scheduler = BackgroundScheduler()

with open('jobs.json', 'r') as f:
    data = json.load(f)

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

def submit_to_reddit(subreddit_name, title, content_path):
    try:
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()

        submission = reddit.subreddit(subreddit_name).submit(
            title=title,
            selftext=content
        )
        print(f"[{datetime.now()}] ✅ Posted to r/{subreddit_name}: {submission.url}")
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Failed to post to r/{subreddit_name}: {e}")

# Load all scheduled jobs from JSON
with open('jobs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx, job in enumerate(data['jobs']):
    try:
        subreddit = job['subreddit']
        title = job['title']
        content_file = job['content_location']
        run_time = datetime(
            int(job['year']),
            int(job['month']),
            int(job['day']),
            int(job['hour']),
            int(job['minute'])
        )

        print(f"⏰ Scheduling Job {idx + 1}: r/{subreddit} at {run_time} from '{content_file}'")

        scheduler.add_job(
            submit_to_reddit,
            'date',
            run_date=run_time,
            args=[subreddit, title, content_file]
        )
    except Exception as e:
        print(f"⚠️ Failed to schedule Job {idx + 1}: {e}")

# Start and block
scheduler.start()
print("🚀 All jobs scheduled. Waiting for execution...")

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("🛑 Scheduler shut down.")