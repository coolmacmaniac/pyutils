#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Sat Apr 21 19:29:25 2018
@author     : Sourabh
"""

# %%

class Field:
    
    def __init__(self, name, dtype, constraint=''):
        self.name = name
        self.dtype = dtype
        self.constraint = constraint
    
    def __str__(self):
        if self.constraint is None:
            return '%s %s' % (self.name, self.dtype)
        return '%s %s %s' % (self.name, self.dtype, self.constraint)
    
    def __repr__(self):
        if self.constraint is None:
            return '%r %r' % (self.name, self.dtype)
        return '%r %r %r' % (self.name, self.dtype, self.constraint)
