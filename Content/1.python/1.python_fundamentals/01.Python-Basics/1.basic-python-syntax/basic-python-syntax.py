#!/usr/bin/env python
# coding: utf-8

# # Basic python syntax

# The syntax of the Python programming language is the set of rules that defines how a Python program will be written and interpreted (by both the runtime system and by human readers).The Python language has many similarities to Perl, C, and Java. However, there are some definite differences between the languages. 

# ### Design philosophy
# 
# Python was designed to be a highly readable language. It has a relatively uncluttered visual layout and uses English keywords frequently where other languages use punctuation. Python aims to be simple and consistent in the design of its syntax, encapsulated in the mantra "There should be one—and preferably only one—obvious way to do it", from *"The Zen of Python"*
# 
# With Python, forget the semicolons and curly braces to delimit the blocks. Python works by line and prioritization is done with indendation.  
# We will see this later with the conditions and functions.
# 

# ### Indentation 

# Python uses whitespace to delimit control flow blocks (following the off-side rule). Python borrows this feature from its predecessor ABC: instead of punctuation or keywords, it uses indentation to indicate the run of a block.
# 
# In so-called "free-format" languages — that use the block structure derived from ALGOL — blocks of code are set off with braces ({ }) or keywords. In most coding conventions for these languages, programmers conventionally indent the code within a block, to visually set it apart from the surrounding code (prettyprinting). 

# In[4]:


def foo(x):
    if x == 0:
        bar()
        baz()
    else:
        qux(x)
        foo(x - 1)


# ### Comments in Python
# A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

# In[2]:


# My first comment 
name = "BeCode" # Name of school


# Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:

# In[1]:


"""
This is a multiline
comment.
"""


# ### Quotation in Python  
# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
# 
# The triple quotes are used to span the string across multiple lines. For example, all the following are legal :

# In[3]:


word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print(word)
print(sentence)
print(paragraph)


# ### Reserved Words
# 
# The following list shows the Python keywords. These are reserved words and you cannot use them as constants or variables or any other identifier name. All Python keywords contain only lowercase letters.
# 
# * and	
# * exec	
# * not
# * assert	
# * finally	
# * or
# * break	
# * for	
# * pass
# * class	
# * from	
# * print
# * continue	
# * global	
# * raise
# * def	
# * if	
# * return
# * del	
# * import	
# * try
# * elif	
# * in	
# * while
# * else	
# * is	
# * with
# * except	
# * lambda	 
# * yield

# ## [All right, you can move on!](../2.variables-and-data-types/variables_and_data_types.ipynb)
