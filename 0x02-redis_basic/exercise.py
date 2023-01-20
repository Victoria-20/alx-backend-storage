#!/usr/bin/env python3
""" 0. Writing strings to Redis"""
import redis
import random
from typing import Union
import uuid


class Cache():
    """ initializes Redis"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key
