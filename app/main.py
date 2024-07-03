from fastapi import FastAPI
from tasks import scrape_web_page, notify_process_results
from celery import chord
from utilities import reset_cache

app = FastAPI()
URL = 'https://dentalstall.com/shop'

# This endpoint will trigger the task
# Has two optional query parameters: no of pages and parse string
@app.post("/scrap_data")
async def read_item(no_of_pages: int = 1, parse_string: str = "") -> dict:
    reset_cache()
    chord([scrape_web_page.s(URL, page) for page in range(2, no_of_pages + 1)])(notify_process_results.subtask())
    return {"status": "Task has been created"}

    

