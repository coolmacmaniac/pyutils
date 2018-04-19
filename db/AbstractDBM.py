#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:29:34 2018
@author     : Sourabh
"""

# %%

from abc import ABC
from abc import abstractmethod

class AbstractDBM(ABC):
    
    @abstractmethod
    def connectDB(self, dbpath):
        pass
    
    @abstractmethod
    def closeDB(self):
        pass
    
    @abstractmethod
    def createTable(self, schema):
        pass
    
    @abstractmethod
    def deleteTable(self, name):
        pass
    
    @abstractmethod
    def saveTable(self, name):
        pass
    
    @abstractmethod
    def executeQuery(self, query):
        pass
    
    @abstractmethod
    def fetchOne(self):
        pass
    
    @abstractmethod
    def fetchAll(self):
        pass
