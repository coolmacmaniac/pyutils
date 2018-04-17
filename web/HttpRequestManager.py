#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 22:20:56 2018
@author     : Sourabh
"""

# %%

import requests
import json

from HttpMethod import HttpMethod
from HttpException import HttpException
from HttpRequest import HttpRequest
from HttpResponse import HttpResponse

class HttpRequestManager:
    
    def __init__(self):
        pass
    
    def invoke(self, request, method):
        try:
            
            if not isinstance(request, HttpRequest):
                raise HttpException('Invalid HTTP request object.', 400)
            elif request.uri is None:
                raise HttpException('Invalid HTTP request URI.', 400)
            
            r = requests.Response()
            if method == HttpMethod.GET:
                r = requests.get(
                        url=request.uri,
                        params=request.queryParams,
                        headers=request.headers
                        )
            elif method == HttpMethod.POST:
                r = requests.post(
                        url=request.uri,
                        data=json.dumps(request.payload),
                        headers=request.headers
                        )
            
            # handle if any error occurred
            if r.status_code >= 400:
                raise HttpException(r.message, r.status_code)
            
            return HttpResponse(r.text)
        
        except HttpException as ex:
            print('Error: %s (Code: %d)' % ex.message, ex.erorCode)
            return HttpResponse(payload=ex.message, status=False)
