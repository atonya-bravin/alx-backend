#!/usr/bin/env python3
"""
In this module, we create a class BasicCache that inherits from BaseCaching
and is a caching system
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def put(self, key, item):
        """
        This function checks if the key or item is equal to None
        and then assigns them respectively if not
        """

        if key is not None or item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Conversion of the dictionary into a list
            # This assists in the popping of the first index
            # This is because a dictionary has no indexes but key,value pairs
            dict_list = list(self.cache_data.items())

            # Pop of the first item the list, and extraction of the key,value

            removed_key, removed_value = dict_list.pop(0)

            # Removal of the same item using the key, from the dictionary
            self.cache_data.pop(removed_key)
            print(f"DISCARD: {removed_key}")

    def get(self, key):
        """
        This function returns a specific value
        """

        if key not in self.cache_data.keys:
            return None

        return self.cache_data.get(value)
