#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))


class BasicCache(BaseCaching):
    """BasicCache inherits"""

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
