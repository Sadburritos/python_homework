import functools


class DatabaseHandler:
    def __init__(self, db):
        self.db = db

    @functools.lru_cache(maxsize=128)
    def get_data(self, key):
        return self.db.get(key=key)


db = TinyDB('db.json')
handler = DatabaseHandler(db)

result1 = handler.get_data(1)
result2 = handler.get_data(1)
