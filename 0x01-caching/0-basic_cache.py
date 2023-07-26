#!/usr/bin/env python3
"""
In this module, we create a class BasicCache that inherits from BaseCaching
and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits the BaseCaching class
    for the module base_caching.py
    """

    def put(self, key, item):
        """
        This function checks if the key or item is equal to None
        and then assigns them respectively if not
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        This function returns a specific key
        """

        return self.cache_data.get(key)
