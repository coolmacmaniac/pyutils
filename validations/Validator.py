#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Sat Sep 15 14:15:06 2018
@author     : Sourabh
"""

# %%

import inspect
from pyutils.logger import lognone

class Validator:

    @staticmethod
    def __get_name_of(attribute=None, local_vars=None):
        """
        Gets the name of the variable in the scope of the caller

        :param attribute: the variable whose name is required as str type
        :param local_vars: the scope of the caller method
        :return: the name of the provided variable, otherwise None
        """
        name = None
        try:
            if attribute is None:
                raise AttributeError(
                    'The attribute whose name is to be found is missing'
                )
            if locals is None:
                raise AttributeError(
                    'The locals should be provided to find the attribute name'
                )
            name = [key for key, val in local_vars if val is attribute][0]
        except Exception as e:
            lognone(str(e))
        return name

    @staticmethod
    def validate_attribute(attribute=None, dtype=None, strict=False):
        """
        Validates the provided variable against boundary conditions.
        Currently the attributes of str, list and dict types are supported.

        :param attribute: the variable to be validated in the caller method
        :param dtype: the expected data type of the variable to be validated
        :param strict: if True, then length and empty checks are also done
        :return: True for successful validation, raises Exceptions otherwise
        """
        callers_locals = inspect.currentframe().f_back.f_locals.items()
        name = Validator.__get_name_of(attribute, callers_locals)
        #
        if attribute is None:
            raise AttributeError(
                'The attribute should be provided'
            )
        if dtype is None:
            raise AttributeError(
                'The data type for attribute "{}" should be '
                'provided.'.format(name)
            )
        if not isinstance(attribute, dtype):
            raise TypeError(
                'The data type of attribute "{}" is {} which is different '
                'from the expected {}'.format(
                    name, type(attribute), dtype
                )
            )
        if isinstance(attribute, str) \
            or isinstance(attribute, list) \
            or isinstance(attribute, dict):
            if strict and len(attribute) is 0:
                raise ValueError(
                    'The attribute "{}" is blank'.format(name)
                )
        return True
