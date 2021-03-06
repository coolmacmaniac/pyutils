#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 24 01:23:44 2018
@author     : Sourabh
"""

# %%


import ntpath
import os
from pathlib2 import Path

class PathManager:
    
    @staticmethod
    def pathComponents(path):
        folder, file = ntpath.split(path)
        if file == '':
            raise Exception('Invalid file location')
        if folder == '':
            folder = './'
        elif folder == '.' or folder == '..' or folder == '~':
            folder = folder + '/'
        folder = os.path.expanduser(folder)
        folder = os.path.abspath(folder)
        abspath = os.path.join(folder, file)
        return (folder, file, abspath)
    
    @staticmethod
    def fileComponents(path):
        file = ntpath.basename(path)
        if file == '':
            raise Exception('Invalid file location')
        components = file.split(sep='.')
        return (components[0], components[1])
        
    @staticmethod
    def absPath(dirPath, fileName, extension=None):
        if extension is not None:
            completeFileName = '%s.%s' % (fileName, extension)
        else:
            completeFileName = fileName
        return os.path.join(dirPath, completeFileName)
    
    @staticmethod
    def exists(path):
        if path is None:
            return False
        loc = Path(path)
        return loc.exists()
    
    @staticmethod
    def isFile(path):
        if path is None:
            return False
        loc = Path(path)
        return loc.is_file()
    
    @staticmethod
    def isDir(path):
        if path is None:
            return False
        loc = Path(path)
        return loc.is_dir()
