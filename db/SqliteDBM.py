#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:42:09 2018
@author     : Sourabh
"""

# %%

import sqlite3
from functools import reduce
from .AbstractDBM import AbstractDBM
from .Field import Field
from pyutils.io import PathManager
from pyutils.io import FileManager

# %%

class SqliteDBM(AbstractDBM):
    def __init__(self):
        self.dbPath = None
        self.connection = None
        self.cursor = None
    
    def connectDB(self, dbpath):
        # close the existing connection before opening a new one
        self.closeDB()
        try:
            self.connection = sqlite3.connect(dbpath)
            self.cursor = self.connection.cursor()
            self.dbPath = dbpath
        except (sqlite3.DatabaseError, sqlite3.DataError,
                sqlite3.IntegrityError, sqlite3.ProgrammingError,
                sqlite3.InternalError, sqlite3.OperationalError) as e:
            print(str(e))
            raise e
    
    def closeDB(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
                self.cursor = None
            if self.connection is not None:
                self.connection.close()
                self.connection = None
        except (sqlite3.DatabaseError, sqlite3.DataError,
                sqlite3.IntegrityError, sqlite3.ProgrammingError,
                sqlite3.InternalError, sqlite3.OperationalError) as e:
            print(str(e))
            raise e
    
    def exportDB(self, tables=None):
        dirName, _, _ = PathManager.pathComponents(self.dbPath)
        if tables is None:
            print('Fetching tables list from DB')
            targetTables = self.listTables()
        else:
            targetTables = tables
        exportedFiles = []
        for table in targetTables:
            csvPath = PathManager.absPath(dirName, table, 'csv')
            records = self.fetchAllFromTable(table)
            headers = [col[0] for col in self.cursor.description]
            fm = FileManager()
            print('Exporting table ->', table)
            fm.writeCSV(csvPath, headers, records)
            exportedFiles.append(csvPath)
        return exportedFiles
    
    def importCSV(self, csvFiles):
        if csvFiles is None:
            print('Nothing to be imported')
            return
        tables = []
        for csvFile in csvFiles:
            print('Importing', csvFile, ':')
            headers, records = FileManager.readCSV(csvFile)
            if headers is None and records is None:
                continue
            schema = []
            for header in headers:
                schema.append(Field(header, 'TEXT'))
            name, _ = PathManager.fileComponents(csvFile)
            self.deleteTable(name)
            self.createTable(name, schema)
            self.insertIntoTable(name, records)
            tables.append(name)
            print('Table "%s" created in database file at location:\n%s' %
                  (name, self.dbPath))
            print()
        return tables
    
    def createTable(self, name, schema):
        fields = reduce(lambda a, b: str(a) + ',\n  ' + str(b), schema)
        query = 'create table ' + name + ' (\n  ' + fields + '\n)'
        self.executeQuery(query)
    
    def deleteTable(self, name):
        query = 'drop table if exists ' + name
        self.executeQuery(query);
    
    def insertIntoTable(self, name, records):
        try:
            if records is None:
                raise ValueError
            query = 'insert into ' + name + ' values ( ### )'
            qmarks = ['?'] * len(records[0])
            placeholders = reduce(lambda a, b: str(a) + ', ' + str(b), qmarks)
            query = query.replace('###', placeholders)
            self.executeQuery(query, records)
        except ValueError as e:
            print('Nothing to be inserted\n', str(e))
            raise e
    
    def fetchAllFromTable(self, name):
        query = 'select * from ' + name
        self.executeQuery(query)
        return self.fetchAll()
    
    def saveTable(self, name):
        self.connection.commit()
    
    def executeQuery(self, query, records=None):
        try:
            if records is None:
                print('Query:', query, sep='\n')
                self.cursor.execute(query)
            else:
                print('Query:', query, 'Objects:', records, sep='\n')
                self.cursor.executemany(query, records)
        except AttributeError as e:
            print('DB not connected\n', str(e))
            #raise e
        except (sqlite3.DatabaseError, sqlite3.DataError,
                sqlite3.IntegrityError, sqlite3.ProgrammingError,
                sqlite3.InternalError, sqlite3.OperationalError) as e:
            print(str(e))
            raise e
    
    def fetchOne(self):
        # returns the record as a tuple
        return self.cursor.fetchone()
    
    def fetchAll(self):
        # returns each record as a tuple
        return self.cursor.fetchall()
    
    def listTables(self):
        query = 'select name from sqlite_master'
        self.cursor.execute(query)
        return [row[0] for row in self.cursor
            if not row[0].startswith('sqlite')
            and not row[0].endswith('idx')]
