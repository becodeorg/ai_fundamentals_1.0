#!/usr/bin/env python
# coding: utf-8

# **1. Create a variable ``name`` that contains the value "Alan Turing".**

# In[5]:





# **2. Create a variable ``age`` that contains the value 42.**

# In[6]:





# **3. Create a person variable that contains a list with the following values ``name``, ``age``** and "mathematician"

# In[16]:





# **4. Create a variable ``text`` that contains "Hello, my name is Alan Turing and I am 42 years old and I am a mathematician".  
# Use the format method and the variable ``person``  to do this.**

# In[ ]:





# **5. Create a variable ``typeAge`` that contains type of variable ``age.``**

# In[ ]:





# ## Testing
# Every good developer tests his code. So we're going to get the right habits now. Do not change the code, execute it.

# In[ ]:


import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_name(self):
        self.assertEqual(name, "Alan Turing")
    
    def test_age(self):
        self.assertEqual(age, 42)
    
    def test_person(self):
        self.assertEqual(person,["Alan Turing", 42, "mathematician"])
    
    def test_text(self):
        self.assertEqual(text,"Hello, my name is Alan Turing and I am 42 years old and I am a mathematician.")
        
    def test_type(self):
        self.assertEqual(typeAge,type(int()))
    

unittest.main(argv=[''], verbosity=2, exit=False)


# ## [Is everything okay? Well, you can move on.](../3.basics-operators/basics-operators.ipynb)
