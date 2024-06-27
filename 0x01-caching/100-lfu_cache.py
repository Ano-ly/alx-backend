#!/usr/bin/env python3
""" LFUCaching module
"""
import time
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache inherits from BaseCaching"""

    def __init__(self):
        """Initialise class instance"""
        super().__init__()
        self.timer = dict()
        self.usage = dict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                print("INNNNN")
                self.usage[key] += 1
            else:
                self.usage.update({key: 0})
            self.cache_data.update({key: item})
            self.timer.update({key: time.time()})
            if self.MAX_ITEMS < len(self.cache_data):
                least_freq = min([v for k, v in self.usage.items()
                                 if k != key])
                evict_list = [k for k in self.cache_data.keys()
                              if self.usage[k] == least_freq]
                min_time = min([self.timer[k] for k in evict_list])
                for k in self.cache_data:
                    if self.timer[k] == min_time:
                        evict_key = k
                del (self.cache_data[evict_key])
                print(f"DISCARD: {evict_key}")
                del (self.usage[evict_key])
                del (self.timer[evict_key])
        print(self.usage)
        print(self.timer)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            ret = self.cache_data.get(key)
            if ret is not None:
                self.usage[key] += 1
                self.timer[key] = time.time()
            return ret
        return (None)
