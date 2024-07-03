from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def read(self):
        pass
