from abc import ABC, abstractmethod

class Cache(ABC):
    RECORDS_UPDATED = 'records_updated'
    RECORDS_INSERTED = 'records_inserted'
    RECORDS_SKIPPED = 'records_skipped'

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self, key):
        pass