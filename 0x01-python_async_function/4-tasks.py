#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called
"""
import asyncio
from typing import List
from asyncio.tasks import Task


async def wait_random(max_delay: int) -> float:
    """Function def wait_random"""
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Task:
    """Function def task_wait_random"""
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function def task_wait_n"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = []
    for coro in asyncio.as_completed(tasks):
        result = await coro
        completed.append(result)
    return completed
