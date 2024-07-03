from abc import ABC, abstractmethod
import logging

class Notification(ABC):
    @abstractmethod
    def notify(self, message) -> None:
        pass

class ConsoleNotification(Notification):
    def notify(self, message) -> None:
        print(f'{message}')
        logging.info(f'{message}')