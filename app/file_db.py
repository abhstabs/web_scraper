import json
import os

from storage import Storage


class FileStorage(Storage):
    def __init__(self, file_name = 'products.json'):
        self.file_name = file_name

    def save(self, data):
        file_contents = self.read()
        file_contents.extend(data)
        with open(self.file_name, 'w') as file:
            json.dump(file_contents, file, indent=2)
        

    def read(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.loads(file.read())
        return []