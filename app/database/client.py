from pymongo import MongoClient
from app.config.settings import settings

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

mongodb=MongoDBClient()