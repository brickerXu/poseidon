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
    def __init__(self, host, port, user_name = None, password = None, server_selection_timeout = 10):
        if is_null(host):
            self.host = HOST
        else:
            self.host = host
        if port is None:
            self.port = PORT
        else:
            if not isinstance(port, int):
                raise TypeError("port must be an instance of int.")
            self.port = port
        if (is_null(user_name) and is_null(password)) or (not is_null(user_name) and not is_null(password)):
            self.username = user_name
            self.password = password
        else:
            raise TypeError("userName and password, Both must be empty at the same time or not at the same time.")
        self.server_selection_timeout = server_selection_timeout

        try:
            self.client = MongoClient(host=host, port=port, username=user_name, password=password, serverSelectionTimeoutMS=server_selection_timeout*1000)
            self.client.admin.command('ping')
            self.connect = True
        except ServerSelectionTimeoutError:
            self.connect = False

    def get_collections(self, database):
        db = self.get_database(database)
        return db.list_collection_names()

    def get_collection(self, database, collection):
        collections = self.get_collections(database)
        if collection in collections:
            return collections[collection]
        else:
            raise CollectionNotFoundError

    def get_databases(self):
        if self.connect:
            return self.client.list_database_names()
        else:
            raise MongoDisconnectError()

    def get_database(self, database):
        if database in self.get_databases():
            return self.client[database]
        else:
            raise DatabaseNotFoundError()

    def get_client(self):
        return self.client