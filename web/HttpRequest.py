#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 22:12:05 2018
@author     : Sourabh
"""

# %%

class HttpRequest:

    def __init__(self, uri=None, headers=None, params=None, payload=None):
        self.uri = uri
        self.headers = headers
        self.queryParams = params
        self.payload = payload

    def __str__(self):
        return "URI: %s\nQuery Params: %s\nHeaders: %s\nPayload: %s" % (
                self.uri, self.queryParams, self.headers, self.payload
                )
    
    def __repr__(self):
        return "URI: %r\nQuery Params: %r\nHeaders: %r\nPayload: %r" % (
                self.uri, self.queryParams, self.headers, self.payload
                )
