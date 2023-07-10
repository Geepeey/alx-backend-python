#!/usr/bin/env python3
"""
Function task_wait_random that takes an integer
max_delay and returns a asyncio.Task
"""
import asyncio
from typing import Coroutine
from random import random
from asyncio.tasks import Task


async def wait_random(max_delay: int) -> float:
    """Return delay"""
    delay = random() * max_delay
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Task:
    "Return task"""
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task
