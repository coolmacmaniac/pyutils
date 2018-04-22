#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Sat Apr 21 16:45:05 2018
@author     : Sourabh
"""

# %%

import logging
from enum import IntEnum
from enum import Enum

class LogLevel(Enum):
    DBG    = logging.DEBUG
    INFO   = logging.INFO
    WARN   = logging.WARNING
    ERR    = logging.ERROR

class Log:
    
    # class scope variables
    # by default the enabled logging level is the lowest level
    print("Logging for module:", __name__)
    logging.basicConfig(level=LogLevel.DBG.value)
    __logger = logging.getLogger(__name__)
    print(logging.getLogger().getEffectiveLevel())
    
    @staticmethod
    def setLevel(level):
        logging.basicConfig(level=level)
    
    @staticmethod
    def INFO(*fmt, **kwargs):
        Log.__logger.info(fmt, kwargs)
    
    @staticmethod
    def WARN(*fmt, **kwargs):
        Log.__logger.warning(fmt, kwargs)
    
    @staticmethod
    def ERR(*fmt, **kwargs):
        print('**********', fmt)
        print('**********', kwargs)
        if kwargs:
            Log.__logger.error(fmt, kwargs)
        else:
            Log.__logger.error(fmt)
    
    @staticmethod
    def DEBUG(*fmt, **kwargs):
        Log.__logger.debug(fmt, kwargs)


if __name__ == '__main__':
    print('in', __name__)
    print(LogLevel.DBG.value)
    print(LogLevel.DBG)
    Log.setLevel(LogLevel.ERR)
    Log.ERR("test err %d", val=1)
#    Log.ERR("%s", "test err")
#    Log.WARN("test warn")
#    Log.INFO("test info")
#    Log.DBG("test dbg")
