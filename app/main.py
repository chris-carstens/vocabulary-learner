from fastapi import FastAPI, Request
from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.word_utils import send_words
import pytz

LANGUAGE = 'italian'
TOPICS = ['computer science and artificial intelligence', 'house', 'animals', 'food']
N_WORDS = 5
SCHEDULED_TIME_HOUR = 9
SCHEDULED_TIME_MINUTE = 0
TIMEZONE = pytz.timezone("UTC")

app = FastAPI()
scheduler = BackgroundScheduler()

def scheduled_job():
    send_words(LANGUAGE, TOPICS, N_WORDS)

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(
        scheduled_job,
        'cron',
        hour=SCHEDULED_TIME_HOUR,
        minute=SCHEDULED_TIME_MINUTE,
        timezone=TIMEZONE
    )
    scheduler.start()

@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()

@app.get("/")
def index():
    return {"message": "FastAPI app with APScheduler running in background!"}

@app.post("/send")
async def send(request: Request):
    await send_words(LANGUAGE, TOPICS, N_WORDS)
