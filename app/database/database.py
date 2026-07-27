from app.database.client import mongodb

def get_database():
    return mongodb.db