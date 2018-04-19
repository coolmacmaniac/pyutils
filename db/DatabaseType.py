#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Thu Apr 19 22:37:40 2018
@author     : Sourabh
"""

# %%

from enum import Enum

class DatabaseType(Enum):
    sqlite = 1
    default = sqlite
