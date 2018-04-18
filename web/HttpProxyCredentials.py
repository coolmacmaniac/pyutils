#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Wed Apr 18 23:44:00 2018
@author     : Sourabh
"""

# %%

class HttpProxyCredentials:
    
    def __init__(self, uname, passwd):
        self.userName = uname
        self.password = passwd
    
    def __str__(self):
        return '(%s, %s)' % (self.userName, self.password)
    
    def __repr__(self):
        return '(%r, %r)' % (self.userName, self.password)
