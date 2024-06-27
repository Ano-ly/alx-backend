#!/usr/bin/env python3
""" BaseCaching module for caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from basecaching"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            ret = self.cache_data.get(key)
            return ret
        return (None)
