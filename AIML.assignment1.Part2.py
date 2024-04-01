#!/usr/bin/env python
# coding: utf-8

# Python Sets and Dictionaries Task

# In[1]:


class DataAnalyzer:
    def __init__(self):
        self.dataset = set()
        self.data_dict = {}

    def add_to_set(self, item):
        self.dataset.add(item)

    def remove_from_set(self, item):
        if item in self.dataset:
            self.dataset.remove(item)
        else:
            print("Item not found in the set.")

    def get_set(self):
        return self.dataset

    def create_dictionary(self, key, value):
        if key not in self.data_dict:
            self.data_dict[key] = value
        else:
            print("Key already exists in the dictionary.")

    def update_dictionary(self, key, value):
        if key in self.data_dict:
            self.data_dict[key] = value
        else:
            print("Key not found in the dictionary.")

    def get_dictionary(self):
        return self.data_dict

    def search_dictionary(self, key):
        if key in self.data_dict:
            return self.data_dict[key]
        else:
            return None

    def remove_from_dictionary(self, key):
        if key in self.data_dict:
            del self.data_dict[key]
        else:
            print("Key not found in the dictionary.")


# Example usage:

analyzer = DataAnalyzer()


# In[2]:


# Adding items to the set
analyzer.add_to_set(10)
analyzer.add_to_set(20)
analyzer.add_to_set(30)
print("Set after adding items:", analyzer.get_set())


# In[3]:


# Removing an item from the set
analyzer.remove_from_set(20)
print("Set after removing item:", analyzer.get_set())



# In[4]:


# Creating dictionary
analyzer.create_dictionary('a', 1)
analyzer.create_dictionary('b', 2)
print("Dictionary:", analyzer.get_dictionary())



# In[5]:


# Updating dictionary
analyzer.update_dictionary('a', 100)
print("Updated Dictionary:", analyzer.get_dictionary())



# In[6]:


# Searching dictionary
print("Value for key 'a':", analyzer.search_dictionary('a'))



# In[7]:


# Removing from dictionary
analyzer.remove_from_dictionary('b')
print("Dictionary after removal:", analyzer.get_dictionary())

