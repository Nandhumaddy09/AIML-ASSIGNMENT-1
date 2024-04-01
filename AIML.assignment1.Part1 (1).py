#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# **Python List Manipulation  Task**


# In[3]:


ListManipulator = []


# In[4]:


ListManipulator = ["Mahesh","anusha","siva"]


# In[5]:


# Take a list of elements ass a parameter and appends them to the internal list

ListManipulator = ["Mahesh","anusha","siva"]
ListManipulator.append("Suri")
print(ListManipulator)


# In[6]:


# Remove Duplicate values from the internal list

ListManipulator = ["Mahesh","anusha","siva",'Suri',"Mahesh","Venu","Suri"]
new_list = []
for item in ListManipulator:
    if item not in new_list:
        new_list.append(item)
print(new_list)


# In[7]:


# Reverse the order of the elements in the internal list

ListManipulator = ["Mahesh","anusha","siva",'Suri',"Mahesh","Venu","Suri"]
ListManipulator.reverse()
print(ListManipulator)


# In[8]:


# Sort the elements in the internal list in ascending order

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)


# In[9]:


# Get unique elements

ListManipulator = ["Mahesh","anusha","siva",'Suri',"Mahesh","Venu","Suri"]
unique_elements = list(set(ListManipulator))
print(unique_elements)


# In[10]:


# remove elements ass a parameter and appends them to the internal list

ListManipulator = ["Mahesh","anusha","siva","Suri"]
ListManipulator.remove("Suri")
print(ListManipulator)


# In[11]:


# Returns the current state of the internal list

class ListManipulator:
    def __init__(self, elements=[]):
        self.elements = elements

    def get_elements(self):
        return self.elements

# Create an instance of ListManipulator
list_manipulator = ListManipulator([1, 2, 3, 4])

# Retrieve the current state of the internal list value
current_list_state = list_manipulator.get_elements()

print(current_list_state)  # Output: [1, 2, 3, 4]

