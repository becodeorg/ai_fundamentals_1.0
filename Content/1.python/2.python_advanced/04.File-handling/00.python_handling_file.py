#!/usr/bin/env python
# coding: utf-8

# # Read and write files

# We have made good progress and now we can get down to the serious business of manipulating data files. This is one of the very important points concerning this training. 
# 
# 
# N.B: Most of the files in `./data/` are fiels that 

# To open/edit a file in python we use the `open()` function.
# 
# This function takes as first parameter the path of the file (*relative* or *absolute*) and as second parameter the type of opening, i.e. reading or writing mode.
# 
# *A relative path in computing is a path that takes into account the current location.*
# The path is **relative** to where it is called from.
# 
# *An absolute path is a complete path that can be read regardless of the reading location.*
# 
# 

# In[ ]:


f = open("./data/data.txt", "r") # r for "read"


# - `"r"`, for a read opening (READ).
# 
# - `"w"`, for a write opening (WRITE), each time the file is opened, the content of the file is overwritten. If the file does not exist, python creates it. 
# 
#     *The Python docs say that w+ will "overwrite the existing file if the file exists". So as soon as you open a file with w+, it is now an empty file: it contains 0 bytes. If it used to contain data, that data has been truncated — cut off and thrown away — and now the file size is 0 bytes, so you can't read any of the data that existed before you opened the file with w+. If you actually wanted to read the previous data and add to it, you should use r+ instead of w+* [[Source]](https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w#comment83227862_16208298)
#     
#     
# 
# - `"a"`, for an opening in add mode at the end of the file (APPEND). If the file does not exist, python creates it.
# 
# - `"x"`, creates a new file and opens it for writing
# 
# You can also append a `+` and a `b` to nearly all of the above commands. [[More info here]](https://stackabuse.com/file-handling-in-python/)

# Like any open element, it must be closed again once the instructions have been completed. To do this, we use the `close()` method.

# In[ ]:


f.close()


# In[ ]:


# Let's find out what's going on there
f = open("./data/data.txt", "r")
print (file.read())
f.close()


# Other possibility of opening without closing

# In[ ]:


with open("./data/data.txt", "r") as fichier:
    print (fichier.read())


# Can you put the contents of this file in the form of a list in which each element is a sentence ?  
# *(Use `.split()` for example...)*

# In[ ]:





# To write in a file, just open a file (existing or not), write in it and close it,. We open it in mode `"w"` so that the previous data is deleted and new data can be added.

# In[ ]:


file = open("./data/write.txt", "w")
file.write("Hi everyone, I'm adding sentences to the file !")
file.close()


# Can you take the content of the `data.txt` file from the `.data/` directory, capitalize all the words and write them in the file that you created just before, after the sentences you added?
# 

# In[ ]:


# It's up to you to write the end 
arr =[]
with open("./data/write.txt", "r+") as fichier:
    return # Add your code



# ## Management of directory paths...

# The `os` module is a library that provides portable way of using operating system dependent functionality.
# In this chapter, we are interested in using its powerful file path handling capabilities using `os.path`

# In[ ]:


import os


# Each file or folder is associated with a kind of address that makes it easy to find it without errors. It is not possible to identically name a file in the same folder (except if the extension is different).
# 
# As said before, there are two kind of paths: the absolute path from the root of your file system and the relative path from the folder being read.

# In[ ]:


import os.path


# By looking with the help function, we can see the available methods

# In[ ]:


help(os.path)


# To know your current absolute path, use `abspath('')`

# In[ ]:


# In python a path is a string, so there are methods to manipulate it.
path=os.path.abspath('')
print(path)
print(type(path))


#  To know the part of the path that consists of directories, use `dirname(path)`.

# In[ ]:


os.path.dirname(path)


#  To know the part of the path that is your file only, use `basename(path)`.

# In[ ]:


os.path.basename(path)


# To add a directory, let's say "text" to the path, we use `join()`

# In[ ]:


rep_text=os.path.join(path, "text")
print(rep_text)


# Too retrieve all the elements of a folder as a list, you can use the `listdir()` method

# In[ ]:


# Items are returned as a list and includes folders and hidden files.
os.listdir("../")


# ### How to display all the elements of a folder as well as its child folders? 
# 
# With the function `walk()`:
# 
# ```
# walk(top, topdown=True, onerror=None, followlinks=False)
# ```
# 

# In[ ]:


folder_path = os.path.abspath('./')
print(folder_path)

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)


# Put all the **`.txt` files** from the `data/` directory into a variable.
#     Then, copy the content of all the files from this variable into a file in `data/` that you will name `final.txt`
# 

# In[ ]:





# New task. Can you open all the files from your `data/` directory and save all their contents in a variable,
# using a loop?

# In[ ]:





# Finally, save this concatenated information (assemblies) in a new file.

# In[ ]:




