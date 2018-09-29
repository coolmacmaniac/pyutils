#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on  : Sat Sep 15 14:04:15 2018
@author     : Sourabh
"""

# %%

import re
from datetime import datetime
from datetime import timedelta
from enum import Enum
from pyutils.validations import Validator


class DateTime:
    
    __fmt_short = '%d-%m-%Y'
    __fmt_medium = '%d-%b-%Y'
    __fmt_long = '%d-%m-%Y %H:%M:%S'
    __fmt_short_rev = '%Y-%m-%d'
    __fmt_medium_rev = '%Y-%b-%d'
    __fmt_long_rev = '%Y-%m-%d %H:%M:%S'
    __re_fmt_short = '(\d+)-(\d+)-(\d+)'
    __re_fmt_medium = '(\d+)-(\S+)-(\d+)'
    __re_fmt_long = '(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)'
    
    # date parser to be used while reading CSV files
    dateparser_short = lambda ds: datetime.strptime(ds, DateTime.__fmt_short)
    
    # date formatter to be used while resetting indexes for plotting
    dateformatter_short = lambda dt: dt.strftime(DateTime.__fmt_short)

    class Format(Enum):
        short = 1
        medium = 2
        long = 3

    def __init(self):
        assert False, '{} can not be instantiated'.format(__class__)

    @staticmethod
    def __dt_format_specifier(rev: bool, dtf: Format) -> str:
        if dtf is DateTime.Format.short:
            if rev is False:
                fmt = DateTime.__fmt_short
            else:
                fmt = DateTime.__fmt_short_rev
        elif dtf is DateTime.Format.long:
            if rev is False:
                fmt = DateTime.__fmt_long
            else:
                fmt = DateTime.__fmt_long_rev
        else:
            if rev is False:
                fmt = DateTime.__fmt_medium
            else:
                fmt = DateTime.__fmt_medium_rev
        return fmt

    @staticmethod
    def __re_format_specifier(dtf: Format) -> str:
        if dtf is DateTime.Format.short:
            fmt = DateTime.__re_fmt_short
        elif dtf is DateTime.Format.long:
            fmt = DateTime.__re_fmt_long
        else:
            fmt = DateTime.__re_fmt_medium
        return fmt

    @staticmethod
    def formatted_string_from_seconds(fmt_spec, seconds) -> str:
        if isinstance(seconds, str):
            seconds = int(seconds)
        printable_str = datetime.fromtimestamp(seconds).strftime(fmt_spec)
        return printable_str

    @staticmethod
    def components_from_date_string(ds: str) -> (int, int, int):
        match = re.match(r'{}'.format(DateTime.__re_fmt_short), ds)
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))

    @staticmethod
    def components_from_date_time_string(dts: str) \
            -> (int, int, int, int, int, int):
        match = re.match(r'{}'.format(DateTime.__re_fmt_long), dts)
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)),
                int(match.group(4)), int(match.group(5)), int(match.group(6)))

    @staticmethod
    def date_string_from_seconds(seconds) -> str:
        return DateTime.formatted_string_from_seconds(
                DateTime.__fmt_short, seconds
                )

    @staticmethod
    def date_time_string_from_seconds(seconds) -> str:
        return DateTime.formatted_string_from_seconds(
                DateTime.__fmt_long, seconds
                )

    @staticmethod
    def seconds_from_date(ds: str) -> str:
        (d, m, Y) = DateTime.components_from_date_string(ds)
        seconds = datetime(Y, m, d).strftime('%s')
        return seconds

    @staticmethod
    def seconds_from_date_time(dts: str) -> str:
        (d, m, Y, H, M, S) = DateTime.components_from_date_time_string(dts)
        seconds = datetime(Y, m, d, H, M, S).strftime('%s')
        return seconds

    @staticmethod
    def datetime_from_date_str(fmt: str, ds: str) -> datetime:
        Validator.validate_attribute(fmt, str, True)
        Validator.validate_attribute(ds, str, True)
        dt = datetime.strptime(ds, fmt)
        return dt

    @staticmethod
    def formatted_date(fmt_from: str, fmt_to: str, ds: str) -> str:
        Validator.validate_attribute(fmt_to, str, True)
        dt = DateTime.datetime_from_date_str(fmt_from, ds)
        printable_str = dt.strftime(fmt_to)
        return printable_str
    
    @staticmethod
    def date_time_to_formatted_date(dt: datetime, rev=False) -> str:
        fmt = DateTime.__dt_format_specifier(rev, DateTime.Format.short)
        printable_str = dt.strftime(fmt)
        return printable_str

    @staticmethod
    def standardized_date(ds: str) -> str:
        return DateTime.formatted_date(
            DateTime.__fmt_medium, DateTime.__fmt_short_rev, ds
        )

    @staticmethod
    def earlier_date(ds: str, days: int) -> datetime:
        this_dt = DateTime.datetime_from_date_str(
            DateTime.__fmt_short_rev, ds
        )
        Validator.validate_attribute(days, int)
        earlier_dt = this_dt - timedelta(days=days)
        return earlier_dt

    @staticmethod
    def later_date(ds: str, days: int) -> datetime:
        this_dt = DateTime.datetime_from_date_str(
            DateTime.__fmt_short_rev, ds
        )
        Validator.validate_attribute(days, int)
        later_dt = this_dt + timedelta(days=days)
        return later_dt

    @staticmethod
    def last_quarter_end_date(ds: str) -> str:
        dt = DateTime.datetime_from_date_str(
            DateTime.__fmt_short_rev, ds
        )
        # get the last quarter month
        qm = int(((dt.month - 1) // 3) * 3)
        if qm is 0:
            qm = 12
        # get the month end day for the last quarter
        qd = 31
        if qm is 6 or qm is 9:
            qd = 30
        # get the year for the last quarter
        qy = dt.year
        if qm is 12:
            qy = qy - 1
        # format last quarter end date
        return '{:4}-{:0>2}-{:0>2}'.format(qy, qm, qd)

    @staticmethod
    def today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        return datetime.today().strftime(fmt)
    
    @staticmethod
    def today_extended(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        # add one more day for some specific cases to consider till today EOD
        dt = datetime.today() + timedelta(days=1)
        return dt.strftime(fmt)

    @staticmethod
    def one_week_ago_from_today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        ago = datetime.today() - timedelta(days=7)
        return ago.strftime(fmt)

    @staticmethod
    def one_month_ago_from_today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        ago = datetime.today() - timedelta(days=30)
        return ago.strftime(fmt)

    @staticmethod
    def six_months_ago_from_today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        ago = datetime.today() - timedelta(days=182)
        return ago.strftime(fmt)

    @staticmethod
    def one_year_ago_from_today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        ago = datetime.today() - timedelta(days=365)
        return ago.strftime(fmt)

    @staticmethod
    def five_years_ago_from_today(rev=False, dtf=Format.short) -> str:
        fmt = DateTime.__dt_format_specifier(rev, dtf)
        ago = datetime.today() - timedelta(days=1825)
        return ago.strftime(fmt)
