#!/usr/bin/env python3
"""
In this module, we create a class BasicCache that inherits from BaseCaching
and is a caching system
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
