#!/usr/bin/env python
# coding: utf-8

# ## Remember this, with Python, everything is object
# 
# Let's look at the type of data.

# In[2]:


firstName = "James"
lastName = "Bond" 
age = 39
weigth = 81.56 
doubleAgent = True 
login = "007"
agent = [firstName, lastName, age, weigth, doubleAgent, login] 

print(firstName, type(firstName))
print(lastName, type(lastName))
print(age, type(age))
print(weigth, type(weigth))
print(agent, type(agent))


# Look when you check the data type, you can see that there is the word class in front of all types. The String type is a class (so an object), but also integers, float, etc. Everything in python is an object! 
# 
# This implies that each object has methods and attributes, and you already know some! Example : 
# Imagine that we want to capitalize the first letter of a character string. There is already a **method** for this in the String class. This is the "capitilize" method

# In[1]:


txt = "hello, and welcome to my world."
capitalizeTxt = txt.capitalize()
print(capitalizeTxt) 


# ``capitalize()`` is a method of the string object.

# We will explore this subject further along the way.

# ❗ Although Python is object-oriented, it allows you to write in procedural mode. And for now, we're going to do procedural programming, but very quickly, we will do object-oriented programming.

# ## Mutable vs Immutable Objects 

# In most object-oriented languages, objects are manipulated by references. This means that when you create an object, an ID is assigned to it. This ID is not the object itself but refers to the location of the object in the memory.This is the case, for example, of Java, class objects of C # and Swift (unlike objects of type struct), Python, JavaScript and Ruby. In this case, the fact that the state of an object shared by reference may or may not be modified is important.
# 
# When an object is considered immutable, a copy can be obtained by simply duplicating its reference, instead of copying the entire object. Since a reference (which usually stores only the size of a pointer) is usually much smaller than the object itself, this technique both saves memory and improves the speed of execution.
# 
# The reference copying technique is much more complex to use for variable objects, because if any element using the reference to a variable object modifies it, the modification will become visible to all other elements using the reference.
# 
# The technique of always using references instead of copies of identical immutable objects, storing their value only once in memory, is called "interning". In this context, two objects are considered equal if and only if their references, typically represented by integers, are equal.
# 
# In Python language, the types bool, tuple, str, bytes, frozenset, range are immutable, as well as the numerical types int, float and complex. The list is not exhaustive.
# 
# Tuple objects are immutable lists of heterogeneous objects in Python. We can see the tuple type as the immutable counterpart of the list, and frozenset as the immutable counterpart of the set. Contrary to what we observe for example in Ruby language, strings (str) are immutable. Bit strings (bytes) also, but there is a variable bytearray type. 
# 
# Let's look at this with a practical case.

# #### We will create an immutable object with the class int.
# *(``id()`` is a native python function that allows you to know the reference of the object. It is expressed in Integer)*. 

# In[ ]:


x = 10 # Creating the int() instance
y = 10
print(id(x), id(y))
print(x is y) # comparing the types


# It can be seen here that both the x and y variables point to the same reference. Now, let's change the value of the variable x

# In[ ]:


x += 1
print(id(x), id(y))
print(x is y) # comparing the types


# This time we see that the variable no longer points to the same reference. 
# #### Now we will create a mutable object with the List class.

# In[ ]:


person = ["James", "Bond", "007", "Secret agent"]
person2 = person
print(id(person), id(person))


# Let's modify both lists

# In[ ]:


person += ["English"]
person2 += ["Man"]
print(id(person),id(person2))
print(person, person2)


# This time you can see: 
# 1. Despite the changes made in the ``List``, the references do not change.
# 2. The changes affect both the variable ``person`` and the variable ``person2``.
# 
# So we understand the consequences that this could have. It is therefore very useful to know if you are handling a mutable or immutable object. 

# ## [Next One](../9.functions/functions.ipynb)

# In[ ]:




