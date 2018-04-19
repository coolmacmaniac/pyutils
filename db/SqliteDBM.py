#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:42:09 2018
@author     : Sourabh
"""

# %%

import sqlite3

from .AbstractDBM import AbstractDBM

class SqliteDBM(AbstractDBM):
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connectDB(self, dbpath):
        # close the existing connection
        self.closeDB()
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()
    
    def closeDB(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None
    
    def createTable(self, schema):
        pass
    
    def deleteTable(self, name):
        pass
    
    def saveTable(self, name):
        pass
    
    def executeQuery(self, query):
        try:
            self.cursor.execute(query)
        except (sqlite3.DatabaseError, sqlite3.DataError,
                sqlite3.InternalError, sqlite3.OperationalError) as e:
            print('Unable to perform the transaction. ' % str(e))
    
    def fetchOne(self):
        return self.cursor.fetchone()
    
    def fetchAll(self):
        return self.cursor.fetchall()
