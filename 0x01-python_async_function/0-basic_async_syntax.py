#!/usr/bin/env python3
"""
The basics of async
"""

from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that writes an asynchronous coroutine
    Args:
        max_delay (int): integer with 10 as default value
    Returns:
        delay (float): random waiting time for the coroutine
    """
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
