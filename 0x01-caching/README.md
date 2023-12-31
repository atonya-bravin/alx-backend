# 0x01-caching
In this project, you learn different caching algorithms.

## Objectives
This project is aimed at providing knowledge in;
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Featured files
- **base_caching.py** -> This file contains the code to the base class for this project.

## Featured Tasks
The following are the main tasks of this project and their solutions.

### Task 0
Create a class BasicCache that inherits from BaseCaching and is a caching system:

- You must use self.cache_data - dictionary from the parent class BaseCaching
- This caching system doesn’t have limit
- def put(self, key, item):
	- Must assign to the dictionary self.cache_data the item value for the key key.
	- If key or item is None, this method should not do anything.
- def get(self, key):
	- Must return the value in self.cache_data linked to key.
	- If key is None or if the key doesn’t exist in self.cache_data, return None.
  
  

**0-main.py**
  
```
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
```


### Task 0 [Solution]
**Featured file** -> 0-basic_cache.py

### Task 0 [Solution Breakdown]
- Creation of the class and inherit the BaseCaching class.
- Implementation of the put() method that checks whether the key or item is equal to None and if not, assigns them respectively.
```
  if key is not None or item is not None:
            self.cache_data[key] = item
```
- Implementation of the get() method that returns a specific key
```
return self.cache_data.get(key)
```

## Task 1
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
- def put(self, key, item):
	- Must assign to the dictionary self.cache_data the item value for the key key.
	- If key or item is None, this method should not do anything.
	- If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
		- you must discard the first item put in cache (FIFO algorithm)
		- you must print DISCARD: with the key discarded and following by a new line
- def get(self, key):
	- Must return the value in self.cache_data linked to key.
	- If key is None or if the key doesn’t exist in self.cache_data, return None.
  
  

**1-main.py**
  
```
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
```

### Task 1 [Solution]
**Featured file** -> 1-fifo_cache.py

### Task 1 [Solution Breakdown]
- Creation of the class and inherit the BaseCaching class. 
- Implementation of the put method. This method;
	- Converts a list into a dictionary;
	```
	dict_list = list(self.cache_data.items())
	```
	- Pops the first item from the list, and extraction of the key,value
	```
	removed_key, removed_value = dict_list.pop(0)
	```
	- Removes the same item using the key, from the dictionary
	```
	self.cache_data.pop(removed_key)
	```
- Implementation of the get method. This method 
	- Returns the value linked to a key in a dictionary
	```
	if key not in list(self.cache_data.keys()):
            return None

        return self.cache_data[key]
	```

### Task 2
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
- def put(self, key, item):
	- Must assign to the dictionary self.cache_data the item value for the key key.
	- If key or item is None, this method should not do anything.
	- If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
		- you must discard the last item put in cache (LIFO algorithm)
		- you must print DISCARD: with the key discarded and following by a new line
- def get(self, key):
	- Must return the value in self.cache_data linked to key.
	- If key is None or if the key doesn’t exist in self.cache_data, return None.
  
  
**2-main.py**
  
````
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

### Task 2 [Solution]
**Featured file** -> 2-lifo_cache.py

### Task 2 [Solution Breakdown]
