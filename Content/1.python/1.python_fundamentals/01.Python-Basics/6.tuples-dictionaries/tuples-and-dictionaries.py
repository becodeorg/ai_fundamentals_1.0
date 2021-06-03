#!/usr/bin/env python
# coding: utf-8

# # Lists, Tuples and dictionaries

# ## Lists

# Lists are sequences, ordered collections of objects separated by commas. They are declared with the indicating operator "[ ]":

# In[49]:


myList = ["a","b","c", "d"]


# A value can be accessed by indicating the index.

# In[50]:


print(myList[0])


# We can specify that we only want the first two elements of the list

# In[58]:


print(myList[:2])


# If we want to reverse the list

# In[53]:


print(myList[::-1])


# Warning, the indexes always start from 0. It's a little disturbing at first, but you have to get used to it.
# Other examples of what can be done with the lists.

# In[31]:


myList = myList * 5 
print(myList)


# In[32]:


myList.append("Add Text")
print(myList)


# You can put any type of data in it : 

# In[34]:


var = "Hello, i am a variable that contains String values"
otherList = [193.45, "Hello", ["Inception list", "Two elements"], 89, var]
print(otherList)


# You can also merge two tables

# In[41]:


x = [1, 2, 3, 4]
y = [4, 5, 1, 0]
x.extend(y)
print(x)

# OR 
x = [1, 2, 3, 4]
y = [4, 5, 1, 0]

xy = x + y
print(xy)


# There are many methods, I invite you to find them out by searching on google.

# ## Tuples 
# Python offers a type of data called tuple (term meaning "Table UPLEt"), which is quite similar to a list but cannot be modified. Tuples are therefore preferable to lists wherever you want to be sure that the data transmitted is not modified by mistake within a program. In addition, tuples are less "greedy" in terms of system resources (they take less memory space). Tuples are immutable objects *(We will see what this means a little later.)*

# In[19]:


tupleExample = ("Moriarty", "Sherlock", "Watson")
listExample = ["Moriarty", "Sherlock", "Watson"]


# ### tuple VS list
# As we can see, when we try to modify the content of a Tuple object, we get an error. However, no problem for the list

# In[20]:


tupleExample.append("Lestrade")


# In[21]:


listExample.append("Lestrade")
print(listExample)


# And as we have seen previously, even if we save the "listExample" variable in another variable and make a modification on one of the lists, both lists will be impacted.

# In[22]:


listExample2 = listExample
listExample2.append("Hudson")

print(listExample2)
print(listExample)


# So if you need to process a collection that will not change, use tuples. On the other hand, if you know that this collection will have to be changed, then use the lists.

# ## Dictionaries
# The dictionaries or "associative array" is not a sequence but another composite type. They look similar to the lists to some extent (they are editable like them), but the elements we are going to record will not be arranged in an unchanging order. On the other hand, we will be able to access any of them using a specific index called a key, which can be alphabetical, numerical, or even a composite type under certain conditions.
# Note: Like in a list, the elements stored in a dictionary can be of any type (numerical values, strings, lists, etc.).

# In dictionaries, indexes will be strings of characters, unlike lists.
# 
# Since the dictionary type is a modifiable type, we can start by creating an empty dictionary and then fill it in little by little. From a syntactic point of view, a dictionary-type data structure is recognized by the fact that its elements are enclosed in a pair of braces. An empty dictionary will therefore be noted ``{ }`

# In[30]:


heroes = {}
heroes["Batman"] = "Bruce Wayne"
heroes["Superman"] = "Clark Kent"
print(heroes)


# As you can see in the line above, a dictionary appears as a series of elements separated by commas (all enclosed between two braces). Each of these elements consists of a pair of objects: an index and a value, separated by a colon.
# 
# In a dictionary, indexes are called keys, so elements can be called key-value pairs. You may notice that the order in which the elements appear in the last line does not correspond to the order in which we provided them. This is absolutely irrelevant: we will never try to extract a value from a dictionary using a numerical index. Instead, we will use the keys: 

# In[36]:


print(heroes["Batman"])
print(heroes["Superman"])


# Here, Batman and Superman are the keys and Bruce Wayne and Clark Kent are the values.

# Unlike lists, it is not necessary to use a particular method to add new elements to a dictionary: simply create a new key-value pair. 

# In[43]:


heroes["Spiderman"] = "Peter Parker"
print(heroes)


# ## [Right, you can move here](./Drill-tuples-dictionaries-lists.ipynb)
