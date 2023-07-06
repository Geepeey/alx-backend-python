#!/usr/bin/env python3
"""
Function that takes a string k and an int
or float as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "Returns a tuple"""
    return (k, float(v) ** 2)
