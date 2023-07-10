#!/usr/bin/env python3
"""An async routine called wait_n"""
import asyncio
from typing import List
from random import random


async def wait_random(max_delay: int) -> float:
    """Import wait ramdom"""
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = []
    for coro in asyncio.as_completed(tasks):
        result = await coro
        completed.append(result)
    return completed
