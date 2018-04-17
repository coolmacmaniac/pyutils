#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 23:33:07 2018
@author     : Sourabh
"""

# %%

class HttpResponse:
    
    def __init__(self, payload, status=True):
        self.payload = payload
        self.status = status
    
    def __str__(self):
        return "Status: %s\nPayload: %s" % (
                self.status, self.payload
                )
    
    def __repr__(self):
        return "Status: %r\nPayload: %r" % (
                self.status, self.payload
                )
