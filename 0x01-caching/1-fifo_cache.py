#!/usr/bin/env python3
""" BaseCaching module
"""
import time
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache inherits from BaseCaching"""

    def __init__(self):
        """Initialise class instance"""
        super().__init__()
        self.timer = dict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if self.MAX_ITEMS == len(self.cache_data):
                comp_list = [v for k, v in self.timer.items() if k in
                             self.cache_data.keys()]
                evicted = min(comp_list)
                for k in self.cache_data.keys():
                    if self.timer[k] == evicted:
                        to_evict = k
                del (self.cache_data[to_evict])
                print(f"DISCARD: {to_evict}")
            self.timer.update({key: time.time()})
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and item is not None:
            ret = self.cache_data.get(key)
            return ret
        return (None)
