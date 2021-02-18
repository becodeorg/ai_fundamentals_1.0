#!/usr/bin/env python
# coding: utf-8

# # Basics operators

# ## Arithmetic operators
# Arithmetic Operators perform various arithmetic calculations like addition, subtraction, multiplication, division, %modulus, exponent, etc. There are various methods for arithmetic calculation in Python : you can use the eval function or declare variable & calculate, or call functions. 

# <table>
# 
# <tbody>
# 
# <tr>
# 
# <th style="text-align:center;width:10%">Operator</th>
# 
# <th style="text-align:center;width:45%">Description</th>
# 
# 
# </tr>
# 
# <tr>
# 
# <td>+ Addition</td>
# 
# <td>Adds values on either side of the operator.</td>
# 
# </tr>
# 
# <tr>
# 
# <td>- Subtraction</td>
# 
# <td>Subtracts right hand operand from left hand operand.</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >* Multiplication</td>
# 
# <td>Multiplies values on either side of the operator</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td>/ Division</td>
# 
# <td>Divides left hand operand by right hand operand</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td>% Modulus</td>
# 
# <td>Divides left hand operand by right hand operand and returns remainder</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td>** Exponent</td>
# 
# <td>Performs exponential (power) calculation on operators</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td>// Floor division</td>
# 
# <td>Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −</td>
# 
# </tr>
# 
# </tbody>
# 
# </table>

# Let's try it. We create two variables and assign two values to them. 

# In[2]:


a = 10 
b = 20


# **Addition**

# In[3]:


add = a + b
print(add)


# **Subtraction**

# In[4]:


sub = b - a
print(sub)


# **Multiplication**

# In[5]:


multi = a * b
print(multi)


# **Division**  
# Note that in this case, python returns a float.

# In[6]:


div = b / a
print(div)


# **Floor division**  
# To obtain an integer, you can use the floor division operator.

# In[7]:


floorDiv = b // a
print(floorDiv)


# **Modulus**  
# To obtain the rest of a division.

# In[8]:


modulus = b % a
print("modulus :", modulus)
modulus2 = 21 % 2
print("modulus2 :", modulus2)


# **Exponent**  
# 10 to the power 2

# In[9]:


exp = a**2
print(exp)


# ### Comparison Operators
# These operators compare the values on either side of the operands and determine the relation between them. It is also referred as relational operators. Various comparison operators are ( ==, != , <>, >,<=, etc) 

# <table>
# 
# <tbody>
# 
# <tr>
# 
# <th>Operator</th>
# 
# <th >Description</th>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td >==</td>
# 
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# 
# </tr>
# 
# <tr>
# 
# <td >!=</td>
# 
# <td>If values of two operands are not equal, then condition becomes true.</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td ><></td>
# 
# <td>If values of two operands are not equal, then condition becomes true. It has now been removed in Python 3</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td >></td>
# 
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td ><</td>
# 
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >>=</td>
# 
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td ><=</td>
# 
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# 
# 
# </tr>
# 
# </tbody>
# 
# </table>
# 
# 
# Let's try it. We create 2 variables and assign two values to them. 

# In[10]:


a = 10
b = 20


# **Equals**

# In[11]:


print(a==b)
print(a==10)


# **Not equals**

# In[12]:


print(a!=b)
print(a!=10)


# **Not equals but ``<>`` has now been removed in Python 3**  
# Use ``!=``

# In[13]:


print(a <> b)
print(a <> 10)


# **Bigger than**

# In[14]:


print(a>b)
print(b>a)


# **Bigger or equal than**

# In[15]:


print(a>=b)
print(b>=a)


# **Smaller than**

# In[16]:


print(a>b)
print(b>a)


# **Smaller or equal than**

# In[17]:


print(a>=b)
print(b>=a)


# ### Assignment Operators
# Python assignment operators are used for assigning the value of the right operand to the left operand. Various assignment operators used in Python are (+=, - = , *=, /= , etc.) 

# <table>
# 
# <tbody>
# 
# <tr>
# 
# <th style="text-align:center;width:10%">Operator</th>
# 
# <th style="text-align:center;width:45%">Description</th>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td >=</td>
# 
# <td>Assigns values from right side operands to left side operand</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >+= Add AND</td>
# 
# <td>It adds right operand to the left operand and assign the result to left operand</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >-= Subtract AND</td>
# 
# <td>It subtracts right operand from the left operand and assign the result to left operand</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td >*= Multiply AND</td>
# 
# <td>It multiplies right operand with the left operand and assign the result to left operand</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >/= Divide AND</td>
# 
# <td>It divides left operand with the right operand and assign the result to left operand</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td>%= Modulus AND</td>
# 
# <td>It takes modulus using two operands and assign the result to left operand</td>
# 
# 
# 
# </tr>
# 
# <tr>
# 
# <td>**= Exponent AND</td>
# 
# <td>Performs exponential (power) calculation on operators and assign value to the left operand</td>
# 
# 
# </tr>
# 
# <tr>
# 
# <td >//= Floor Division</td>
# 
# <td>It performs floor division on operators and assign value to the left operand</td>
# 
# 
# 
# </tr>
# 
# </tbody>
# 
# </table>

# **Assignment**

# In[18]:


a = 10
name = "Alan Turing"
print(a)
print(name)


# **Add AND**

# In[19]:


a += 10
name += " is a good mathematician"
print(a)
print(name)


# **❗ But beware, we can only add variables of the same type**  
# The variable ``a`` is of type integer and the variable ``name`` is of type string.

# In[20]:


name += a # It's the same as ``name = name + a``


# In[1]:


a += name# It's the same as ``a = a + name``


# **Subtract AND**

# In[ ]:


a = 20
a -= 10
print(a)


# This operator does not work with strings, unlike the += operator 

# In[40]:


name -="Alan Turing"


# **Multiply AND**  
# This operator works with strings.

# In[ ]:


a = 10
a *= 10
print(a)

text = "Alan Turing"
text *= 10
print(text)


# **Divide AND**

# In[ ]:


a = 100
a /= 10
print(a)


# This operator does not works with character strings unlike the ``*=`` operator.  
# Note that in this case, python returns a float.

# **Modulus AND**

# In[ ]:


a = 100
a %= 3
print(a)


# This operator does not works with character strings.

# **Exponent AND**

# In[ ]:


a = 2 
a **= 3 # ( 2 * 2 * 2)
print(a)


# This operator does not works with character strings.

# **Floor Division AND**

# In[ ]:


a = 20
a //= 3
print(a)


# This operator does not works with character strings.

# ## [Next one](../4.conditions-and-other-operators/conditions-and-other-operators.ipynb)

# In[ ]:




