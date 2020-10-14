import pymongo
from datetime import datetime

class Logger:

    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://teste:teste@cluster0.irx95.mongodb.net/log?retryWrites=true&w=majority")
        self.db = client.log

    def log(self, request, response):
        self.db.log.insert_one({"request": request, "response": response, "insertedAt": datetime.now()})
