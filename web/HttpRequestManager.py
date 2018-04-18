#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Tue Apr 17 22:20:56 2018
@author     : Sourabh
"""

# %%

import requests
from requests.auth import HTTPProxyAuth
import json

from .HttpMethod import HttpMethod
from .HttpException import HttpException
from .HttpRequest import HttpRequest
from .HttpResponse import HttpResponse

from .HttpProxy import HttpProxy
from .HttpProxyCredentials import HttpProxyCredentials

class HttpRequestManager:
    
    def __init__(self, logged=False):
        self.__loggingAllowed = logged
        pass
    
    def __log(self, r):
        if self.__loggingAllowed is True:
            print('-' * 20)
            print('URL:', r.request.url, '\n')
            print('Request Headers:', r.request.headers, '\n')
            print('Requst Method:', r.request.method, '\n')
            if (r.request.method.upper() == 'POST'):
                print('Request Payload:', r.request.body, '\n')
            print('Response Headers:', r.headers, '\n')
            print('Status Code:', r.status_code, '\n')
            print('Response Payload:', r.text)
            print('-' * 20)
    
    def __logErr(self, errStr):
        if self.__loggingAllowed is True:
            print('-' * 20)
            print(errStr)
            print('-' * 20)
    
    def invoke(self, request, method):
        try:
            if not isinstance(request, HttpRequest):
                raise HttpException('Invalid HTTP request object.', 400)
            elif request.uri is None:
                raise HttpException('Invalid HTTP request URI.', 400)
            
            # use proxies and credentials if provided
            proxies = None
            auth = None
            if request.useProxy is True:
                proxies = request.proxies
                if request.credentials is not None:
                    auth = HTTPProxyAuth(
                            request.credentials.username,
                            request.credentials.password
                            )
            
            r = None
            if method == HttpMethod.GET:
                r = requests.get(
                        url=request.uri,
                        params=request.queryParams,
                        headers=request.headers,
                        proxies=proxies,
                        auth=auth
                        )
            elif method == HttpMethod.POST:
                r = requests.post(
                        url=request.uri,
                        data=json.dumps(request.payload),
                        headers=request.headers,
                        proxies=proxies,
                        auth=auth
                        )
            
            self.__log(r)
            
            # handle if any error occurred
            if r.status_code >= 400:
                raise HttpException(r.message, r.status_code)
            
            return HttpResponse(r.text)
        
        except HttpException as ex:
            self.__logErr('Error: %s (Code: %d)' % ex.message, ex.erorCode)
            return HttpResponse(payload=ex.message, status=False)
        
        except requests.exceptions.ConnectionError as err:
            self.__logErr('Error: %s' % err.args[0])
            return HttpResponse(payload='Connection error', status=False)
        
        except requests.exceptions.Timeout as err:
            self.__logErr('Error: %s' % str(err))
            return HttpResponse(payload='Connection timed out', status=False)
        
        except requests.exceptions.TooManyRedirects as err:
            self.__logErr('Error: %s' % str(err))
            return HttpResponse(payload='Too many redirects', status=False)
        
        except requests.exceptions.RequestException as err:
            self.__logErr('Error: %s' % str(err))
            return HttpResponse(payload='Web request exception', status=False)
