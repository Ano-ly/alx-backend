#!/usr/bin/env python3
""" LRUCaching module
"""
import time
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Class FIFOCache inherits from BaseCaching"""

    def __init__(self):
        """Initialise class instance"""
        super().__init__()
        self.timer = dict()
        self.usage = dict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            self.timer.update({key: time.time()})
            self.usage.update({key: 0})
            if self.MAX_ITEMS < len(self.cache_data):
                least_freq = min(self.usage.values())
                evict_list = [k for k in self.cache_data.keys()
                              if self.usage[k] == least_freq]
                min_time = min([self.timer[k] for k in evict_list])
                for k in self.cache_data:
                    if self.timer[k] == min_time:
                        evict_key = k
                print(self.timer)
                print(self.usage)
                del (self.cache_data[evict_key])
                print(f"DISCARD: {evict_key}")
                del (self.usage[evict_key])
                del (self.timer[evict_key])

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            ret = self.cache_data.get(key)
            if ret is not None:
                self.usage[key] += 1
            return ret
        return (None)
