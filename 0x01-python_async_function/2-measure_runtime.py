#!/usr/bin/env python3
import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n
"""Import wait_n"""


def measure_time(n: int, max_delay: int) -> float:
    """Return total_time / n"""
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
