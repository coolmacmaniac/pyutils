#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Wed Apr 18 23:15:32 2018
@author     : Sourabh
"""

# %%

class HttpProxy:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def __str__(self):
        return '%s:%s' % (self.host, str(self.port))
    
    def __repr__(self):
        return '%r:%r' % (self.host, str(self.port))
