#!/usr/bin/env python
# coding: utf-8

# # Drill : built-in functions
# Use the native python functions to do these exercises.

# ### 1. Create a variable ``countAlpha`` that contains the number of characters contained in the string "Hello world!".

# In[ ]:





# ### 2. Create a variable ``countFloat`` and cast the variable countAlpha in float

# In[ ]:





# ### 3. Round the variable ``pi`` value to -10² and save it in a variable ``roundPi``.

# In[ ]:





# ### 4. Create a variable ``reversedText`` which contains the character string "Hello world !" backwards.
# The result must be a ``list()`` value.

# In[ ]:





# ### 5. Create a variable age  and ask the user to enter his age. Then display it and display its type. 

# In[ ]:





# ### 6. Create a variable `sortNum` that contains the sorted ``num`` list.
# 

# In[39]:


num = [2, 8, 1, 4, 6, 3, 7] 


# ### 7. Create a variable ``sumOfList`` which contains the sum of all the elements in the list ``num``

# In[40]:


num = [2, 8, 1, 4, 6, 3, 7] 


# ### 8. Create a variable ``minValue`` that contains a minimum value of list ``num``

# In[41]:


num = [2, 8, 1, 4, 6, 3, 7] 


# ### 9. Create a variable maxValue that contains a maximum value of list num

# In[ ]:





# ### 10. Find a function that will interpret the string of the variable calc
# Save the result in a variable named ``stringInterpret``

# In[42]:


calc  = "1 + 2"


# ## Testing
# You don't have to modify the code, you just have to execute it

# In[ ]:


import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_countAlpha(self):
        self.assertEqual(countAlpha, 12)
    
    def test_countFloat(self):
        self.assertEqual(type(countFloat), type(float()))
        
    def test_pi(self):
        self.assertEqual(3.14, roundPi)
    
    def test_reversed(self):
        self.assertEqual(reversedText, ['!', ' ', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H'])
    
    def test_age(self):
        self.assertEqual(type(age), type(str()))
        
    def test_sorted(self):
        self.assertEqual(sortNum, [1, 2, 3, 4, 6, 7, 8])
    
    def test_sum(self):
        self.assertEqual(sumOfList, 31)
    
    def test_min(self):
        self.assertEqual(minValue, 1)
    
    def test_max(self):
        self.assertEqual(maxValue, 8)
    
unittest.main(argv=[''], verbosity=2, exit=False)


# ## [Next one](../6.tuples-dictionaries/tuples-and-dictionaries.ipynb)
