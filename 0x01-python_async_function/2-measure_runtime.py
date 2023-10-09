#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for wait_n
    Args:
        n (int):
        max_delay (int)
    Returns:
        a float
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start

    return elapsed / n
