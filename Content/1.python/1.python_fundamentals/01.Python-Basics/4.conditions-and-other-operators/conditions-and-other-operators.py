#!/usr/bin/env python
# coding: utf-8

# ## Conditions

# This notion is one of the most important in programming. It introduces logic and allows to create algorithms
# 
# The idea is to express this: 
# ````
# - If the variable is equal to something then do this.
#     - Do an action
# - If not, do this.
#     - Do an action 
# ````

# Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. For example:

# In[70]:


x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


# Notice that variable assignment is done using a single equal operator "=", whereas comparison between two variables is done using the double equals operator "==". The "not equals" operator is marked as "!=".

# Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination.
# 
# Here is an example for using Python's "if" statement using code blocks:

# **if**

# In[ ]:


age = 23
if age >= 18:
    print("You're an adult!")


# **elif**  
# contraction of words "else if"

# In[ ]:


age = 17
if age >= 18:
    print("You're an adult!")
elif age == 17 :
    print("You are one year short of being an adult")


# **else**  
# It is possible to give instructions whatever the possible choices with the keyword "else".

# In[ ]:


age = 16
if age >= 18:
    print("You're an adult!")
elif age == 17:
    print("You are one year short of being an adult")
else:
    print("Come back later")


# ### Logical operators
# Logical operators in Python that are used for conditional statements are true or false. Logical operators in Python are AND, OR and NOT. For logical operators following condition are applied. 
# The "and" and "or" boolean operators allow building complex boolean expressions, for example:

# **Operator and**

# In[ ]:


student1 = "John"
student2 = "Eric"

if student1 == "John" and student2 == "Eric":
    print("You are John AND Eric")   
else :
    print("Welcome anonymous")


# **Operator or**

# In[ ]:


student1 = "John"
student2 = "Ludovic"

if student1 == "John" or student2 == "Eric":
    print("Your name is either John or Eric.")
else :
    print("Welcome anonymous")


# ### The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:

# In[ ]:


name = "Valérian"
coach = ["Valérian", "Ludovic"]
if name in coach:
    print("Your are Coach!")
else :
    print("You are not coach")


# ### The "not" operator
# Using "not" before a boolean expression inverts it:

# In[ ]:


print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# In[ ]:


name = "Ayaan"
if name not in ["Valérian", "Ludovic"]:
    print("Your are not coach")
else :
    print("You are coach")


# ### The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:

# In[ ]:


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


# But this operator will be further explained later.

# ## [Ok right, you can move here](./drill-conditions-operators.ipynb)

# In[ ]:




