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

### Task 0 [Solution]
**Featured file** -> 0-basic_cache.py

### Task 0 [Solution Breakdown]



