#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 00:21:25 2018
@author     : Sourabh
"""

# %%

from os.path import exists

class FileManager:
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def read(self, filePath):
        contents = None
        if exists(filePath):
            with open(filePath, 'r') as file:
                contents = file.read()
        else:
            print('Read Error: file (%s) does not exist.' % filePath)
        return contents
    
    def write(self, filePath, contents):
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
