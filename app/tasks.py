import os
import requests
from bs4 import BeautifulSoup
from celery import Celery
from utilities import write_to_database, parse_web_page, notify_user
from provider import get_cache
from cache import Cache
import logging

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/1')
celery.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/1')

@celery.task(name = 'scrape_web_page')
def scrape_web_page(url: str, page: int = 1) -> None:
    url = f'{url}/page/{page}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = parse_web_page(soup)
        write_to_database(products)
    else:
        logging.error(f"Failed to fetch the page: {url}, status code: {response.status_code}, response: {response.content}")
        raise Exception("Failed to fetch the page")

@celery.task(name = 'notify_process_results')
def notify_process_results(result: list, cache: Cache = get_cache()) -> None:
    notify_user(
        int(cache.get(Cache.RECORDS_INSERTED)) if cache.get(Cache.RECORDS_INSERTED) else 0, 
        int(cache.get(Cache.RECORDS_UPDATED)) if cache.get(Cache.RECORDS_UPDATED) else 0, 
        int(cache.get(Cache.RECORDS_SKIPPED)) if cache.get(Cache.RECORDS_SKIPPED) else 0,
    )