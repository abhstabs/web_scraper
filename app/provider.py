from settings import settings
from file_db import FileStorage
from notification import ConsoleNotification
import redis
import logging 

def get_db():
    storage = settings.storage
    match storage:
        case "FILE":
            return FileStorage()
        case _:
            return FileStorage()
        
def get_cache():
    cache = settings.cache
    logging.info(f"Cache type: {cache}")
    match cache:
        case "redis":
            return redis.Redis(host='redis', port=6379, db=0)
        case _:
            raise Exception("Invalid cache type")
        
def get_notification_service():
    notification = settings.notification
    match notification:
        case "console":
            return ConsoleNotification()
        case _:
            raise Exception("Invalid notification type")