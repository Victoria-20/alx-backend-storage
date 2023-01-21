#!/usr/bin/env python3
""" 0. Writing strings to Redis"""
import redis
import random
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a single method Callable
    argument and returns a Callable."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache():
    """ initializes Redis"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key

    def get(self, key: str, fn: Callable = None):
        """ take a key string argument and an
        optional Callable argument named fn"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get to str"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parametrize Cache.get to int"""
        return int(key)
