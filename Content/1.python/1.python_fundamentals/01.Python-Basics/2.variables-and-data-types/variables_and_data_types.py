#!/usr/bin/env python
# coding: utf-8

# # Variables and data types
# Variables are used to temporarily store a value in the computer's memory. We can then use it later, when we need it in the program. We can compare that to a small box in which we could store information. 
# 
# Since Python is a dynamically typed language, Python values, not variables, carry type. This has implications for many aspects of the way the language functions.
# 
# All variables in Python hold references to objects, and these references are passed to functions; a function cannot change the value of variable references in its calling function (but see below for exceptions). Some people (including Guido van Rossum himself) have called this parameter-passing scheme "Call by object reference." An object reference means a name, and the passed reference is an "alias", i.e. a copy of the reference to the same object, just as in C/C++. The object's value may be changed in the called function with the "alias", for example:
# 
# 
# 
# ## Naming and code writing conventions
# As in many programming languages, to name a variable, some conventions must be respected.
# 
# #### 1. The name of the variable must start with a **letter or an underscore**. The variable can not start with a number or a hyphen.         
# 
# ❌ Bad example :
# ```py
# # Do not do this
# 2Name = "James" 
# 
# # Do not do this
# -name = "James"
# 
# ```
# 
# ✅ Good example :
# ```py
# # Do this
# name = "James" 
# 
# # Do this
# _name = "James"
# 
# ```
# #### 2. **Never put space between words.** 
# 
# ❌ Bad example :
# ```py
# # Do not do this
# My name = "Odile" 
# ```
# 
# ✅ Good example :
# ```py
# # DO is
# my_name = "Odile"
# 
# ```
# 
# #### 3. No accents on the names of variables. **Use only English**
# 
# ❌ Bad example :
# ```py
# # Do not do this
# prénom = "Odile" 
# ```
# 
# ✅ Good example :
# ```py
# # Do this
# first_name = "Odile" 
# ```
# 
# #### 4. **Always give an explicit name** to the variable.
# 
# ❌ Bad example :
# ```py
# # Do not do this
# a = "Odile" 
# 
# # Do not do this
# fstnme = "Odile"
# 
# ```
# 
# ✅ Good example :
# ```py
# # Do this
# first_name = "Odile" 
# 
# # Do this
# magic_potion = 42
# 
# ```

# **Try it for yourself by clicking on the Run button**

# In[ ]:


# BAD 
2name = "James"


# In[ ]:


# BAD
-name = "Bond"


# In[ ]:


# BAD
My name = "bond"


# The print() function allows us to display the result. 

# In[ ]:


# GOOD
name = "Bond"
print("Your name is", name)


# To format the text, you can use the format() method in the class string

# In[1]:


last_name = "Bond"
first_name = "James"
text = "My name is {}, {} {}.".format(last_name, first_name, last_name)
print(text)


# Another example. Replace the value of the variable ``age`` with your age and the variable ``firstname`` with your First name.

# In[2]:


age = "34"
first_name ="Ludovic"
text = "Hello, my name is {} and i am {}".format(first_name, age)
print(text)


# ## Data types
# 
# Since Python is a high-level language, it has a dynamic variable typing.   
# By dynamics, understand that it is the computer that deals with defining what type of variable should be used.  
# To be perfectly accurate, **it is not the variable that is typed (unlike Java) but its content**
# 
# In java we declare a variable like this:
# ```java
# String fisrtName = "James"
# ```
# We define the type of variable ourselves. 
# 
#  With python we declare a variable like this:
# ```py
# first_name = "James"
# ```
# And so, it's python that will define what type will be used.

# In[4]:


first_name = "James" # String
last_name = "Bond"  # String
age = 39  # Integer
weigth = 81.56 # Float
double_agent = True # Boolean
login = "007" # String
agent = [first_name, last_name, age, weigth, double_agent, login] # List
print(agent)


# 1. Note that ``True`` and ``False`` are written with the first letter uppercase.
# 2. ``login`` is a string.
# 3. ``List`` is like an array, but you can store values of different types.

# Here is a not limited list of the types we use most often. These are the most frequently used.  
# For tuples, dictionaries and sets we'll see them later
# 
# |Name      | Type      | Description |
# |:---------|:---------:|------------:|
# |Integers  | int       | Whole numbers, such as : **1, 67, 5000** |
# |Floating point  | float | Decimal point numbers, such as : **1.89, 0.67, 9.99999** |
# |Strings  | str | Ordered sequence of characters : **"Hello", "10"** |
# |Lists  | list  | Ordered sequence of objects : **["hello", 10, 56.89]** |
# |Dictionaries  | dict | Unordered (Key : Value) pairs : **{"Key1": value, "name" : "Peter}** |
# |Tuples  | tuple |  Ordered sequence of objects (immutable) : **("hello", 10, 56.89)** |
# |Sets  | set | Unordered collections of unique objects : **{1,2}** |
# |Booleans  |bool| Logical value  : **True or False** |
# 

# **There is a native pyhton function that allows you to know what type of data you have. This is the type() function** 

# In[5]:


print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(weigth, type(weigth))
print(agent, type(agent))


# ## [Finished? Practice with these exercises](./drill-variables-data-types.ipynb).
