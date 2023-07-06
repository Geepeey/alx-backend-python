#!/usr/bin/env python3
"""
Function that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(num: float) -> float:
        """returns a function that multiplies a float by multiplier"""
        return num * multiplier
    return multiply
