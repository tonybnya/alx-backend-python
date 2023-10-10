#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine
    """
    start = perf_counter()
    await gather(*[async_comprehension() for _ in range(4)])

    return perf_counter() - start
