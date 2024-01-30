#!/usr/bin/env python3
"""
Task 1 module. FIFO caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Retrieves and add items to a dictionary with a FIFO removal
    policy when the limit is reached
    """
    def __init__(self):
        """
        Initialize cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves an item by key from the cache
        """
        return self.cache_data.get(key, None)
