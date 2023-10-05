#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats
and returns their sum as a float.
"""
import math
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Function definition
    """
    return math.fsum(mxd_lst)
