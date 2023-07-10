#!/usr/bin/env python3
"""Asynchronous coroutine"""
import asyncio
import time
from typing import List
from random import random


async def wait_random(max_delay: int) -> float:
    """Return delay"""
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine with 2 int"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = []
    for coro in asyncio.as_completed(tasks):
        result = await coro
        completed.append(result)
    return completed


def measure_time(n: int, max_delay: int) -> float:
    """Return total_time / n"""
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
