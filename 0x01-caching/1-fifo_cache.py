#!/usr/bin/env python3



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
            dict_list = list(self.cache_data.items())
            removed_key, removed_value = dict_list.pop(0)
            self.cache_data.pop(removed_key)
            print(f"DISCARD: {removed_key}")

    def get(self, key):
        """
        This function returns a specific key
        """
        
        if key not in self.cache_data.keys:
            return None

        return self.cache_data.get(value)
