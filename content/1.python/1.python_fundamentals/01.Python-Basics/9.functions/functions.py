#!/usr/bin/env python
# coding: utf-8

# # The functions

# A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.
# 
# As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

# You can define functions to provide the required functionality. Here are simple rules to define a function in Python.
# 
# - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
# 
# - Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
# 
# - The first statement of a function can be an optional statement - the documentation string of the function or docstring.
# 
# - The code block within every function starts with a colon (:) and is indented.
# 
# - The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
# 

# Example: We will create a function that says hello and welcomes you.

# In[1]:


def hello():
    print("Hello and welcome")
    
hello()


# ## The parameters

# A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters.
# 
# Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function.
# 
# Example :

# In[2]:


def hello(name): # <- Parameter
    print("Hello {} and welcome".format(name))
    
hello("Alan") # <- Argument


# Exemple 2 :   
# Let's add a parameter to the "increaseMe()" function that will increment the variable by 2

# In[3]:


def increaseMe(a):
    return a + 2

increaseMe(1)


# ## Use a dictionary for the parameters

# It is possible to pass a dictionary as an argument that contains the parameters.

# In[9]:


name = {}
name["firstName"] =  "Alan"
name["lastName"] = "Turing"

def hello(firstName, lastName):
    print("Hello {} {} and welcome".format(firstName, lastName)) 
    
hello(**name)


# ## A parameter is required

# If we proceed as above, the passage of the argument becomes mandatory. But we have the possibility to assign a default value in case the user does not pass an argument. 

# In[15]:


def hello(name = "Anonymous"): # <- Parametre
    print("Hello {} and welcome".format(name))
    
hello() # <- Not argument


# ## The operator splat

# If we do not know the number of parameters, we have the possibility to indicate that the function receives an infinite number of parameters 

# In[14]:


def multiply(*elements): # Add "*" to indicate that the parameters are infinite
    res = 1
    for element in elements:
        res = res * element
    return res
multiply(1,2,3,4)


# ## A list as a parameter

# Functions which take lists as arguments and change them during execution are called modifiers and the changes they make are called side effects. Passing a list as an argument actually passes a reference to the list, not a copy of the list. Since lists are mutable, changes made to the elements referenced by the parameter change the same list that the argument is referencing. For example, the function below takes a list as an argument and multiplies each element in the list by 2:

# In[16]:


def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)


# ## Scope of variables (global and local variables)

# The scope of a variable refers to the places that you can see or access a variable.
# 
# If you define a variable at the top level of your script or module or notebook, this is a global variable:

# In[17]:


myVar = "This is a global variable"


# The variable is global because any Python function or class defined in this module or notebook, is able to access this variable. Example : 

# In[25]:


myVar = "This is a global variable"
def printMyVar():
    print(myVar)
    
printMyVar()


# On the other hand, if the variable is declared and assigned in function or class, this variable is variable local. 

# In[30]:


def declare(): 
    varLocal = "This is a local variable"
    
declare()
print(varLocal)


# ## Procedure and functions

# For your computer culture, be aware that a function is not required to return a value, we will then speak in this case rather of procedure.

# ## [Finished? Okay, come practice here.](./drill_functions.ipynb)

# In[ ]:




