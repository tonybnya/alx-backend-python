#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None])\
    -> Union[Any, T]:
    """
    Function definition
    """
    if key in dct:
        return dct[key]
    else:
        return default
