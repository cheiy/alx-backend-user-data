#!/usr/bin/env python3
"""
Module contains filter_datum function
"""
from typing import List
import re

patterns = {
        'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
        'replace': lambda x: r'\g<field>={}'.format(x),
        }


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Given a log message, function returns the obfuscated version of the same
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
