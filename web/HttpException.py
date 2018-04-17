#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 22:44:31 2018
@author     : Sourabh
"""

# %%

class HttpException(Exception):
    
    def __init__(self, message, code):
        super().__init__(message)
        
        self.errorCode = code
