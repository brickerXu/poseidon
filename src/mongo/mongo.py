# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file mongo.py

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from utils.util import *
from mongo.errors import *

# mongoDB默认主机和端口
HOST = 'localhost'
PORT = 27017

class Mongo(object):
    def __init__(self, host, port, userName = None, password = None, serverSelectionTimeoutS = 10):
        if isNull(host):
            self.HOST = HOST
        else:
            self.HOST = host
        if port == None:
            self.PORT = PORT
        else:
            if not isinstance(port, int):
                raise TypeError("port must be an instance of int.")
            self.PORT = port
        if (isNull(userName) and isNull(password)) or (not isNull(userName) and not isNull(password)):
            self.USERNAME = userName
            self.PASSWORD = password
        else:
            raise TypeError("userName and password, Both must be empty at the same time or not at the same time.")
        self.SERVERSELECTIONTIMEOUTS = serverSelectionTimeoutS

        try:
            self.client = MongoClient(host=host, port=port, username=userName, password=password, serverSelectionTimeoutMS=serverSelectionTimeoutS*1000)
            self.client.admin.command('ping')
            self.connect = True
        except ServerSelectionTimeoutError:
            self.connect = False

    def getCollections(self, database):
        db = self.getDataBase(database)
        return db.list_collection_names()

    def getCollection(self, database, collection):
        collections = self.getCollections(database)
        if collection in collections:
            return collections[collection]
        else:
            raise CollectionNotFoundError

    def getDataBases(self):
        if self.connect:
            return self.client.list_database_names();
        else:
            raise MongoDisconnectError()

    def getDataBase(self, database):
        if database in self.getDataBases():
            return self.client[database]
        else:
            raise DatabaseNotFoundError()

    def getClient(self):
        return self.client