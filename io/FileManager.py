#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 00:21:25 2018
@author     : Sourabh
"""

# %%

from os.path import exists
import csv

class FileManager:
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    @staticmethod
    def read(filePath):
        contents = None
        if exists(filePath):
            with open(filePath, 'r') as file:
                contents = file.read()
        else:
            print('Read Error: file (%s) does not exist.' % filePath)
        return contents
    
    @staticmethod
    def write(filePath, contents):
        proceed = True
        if exists(filePath):
            consent = input('The file already exists, overwrite [yes]? ')
            if consent.lower() == 'yes':
                proceed = True
            else:
                proceed = False
        if proceed is True:
            with open(filePath, 'w') as file:
                file.write(contents)
                print('Contents written successfully to file (%s).' % filePath)
        else:
            print('The file contents were not written.')
    
    @staticmethod
    def readCSV(filepath):
        with open(filepath, mode='rt', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel')
            try:
                for row in reader:
                    print(row)
            except csv.Error as e:
                print('file {}, line {}: {}'.format(
                        filepath, reader.line_num, e))
                raise e
    
    @staticmethod
    def writeCSV(filepath, headers, rows):
        with open(filepath, mode='wt', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel')
            try:
                writer.writerow(headers)
                writer.writerows(rows)
            except csv.Error as e:
                print('file {}, line {}: {}'.format(
                        filepath, writer.line_num, e))
                raise e
