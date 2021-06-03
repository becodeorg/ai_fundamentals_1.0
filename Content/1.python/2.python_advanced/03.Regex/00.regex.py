#!/usr/bin/env python
# coding: utf-8

# # Regular expressions (regex) : love or hate?

# ![commit strip](http://www.commitstrip.com/wp-content/uploads/2014/02/Strips-Le-dernier-des-vrais-codeurs-650-finalenglsih.jpg)

# Regular expressions are used in almost all languages. It is a very powerful tool to check if the content of a variable has the shape of what you expect. 
# 
# For example, if you retrieve a phone number, you expect the variable to be composed of numbers and spaces (or dashes) but nothing more. 
# 
# Regular expressions not only warn you of an unwanted character but also delete/modify all those that are not desirable.
# 

# **There are two ways to use regexes:**
# * The first consists in calling the function with the pattern as the first parameter, and the string to be analyzed as the second parameter.
# * The second way is to compile the regex, and then use the methods of the created object to analyze a string passed as an argument. This method speeds up processing when a regex is used several times.  

# In[1]:


import re 


# In[2]:


pattern='[ ]'
string ='I am fine ! There are still 6 months left :()'

#Search the pattern in the past string and return a MatchObject if matches are found,
#otherwise return None.
print(re.search(pattern, string)) 


# In[3]:


pattern='[ ]'
string ='I am fine ! There are still 6 months left :()'

#Cut the string according to the occurrence of the pattern.
print(re.split(pattern, string))


# ### A little syntax
# 
#     [xy]  A possible segment list. Example[abc] equals: a, b or c
# 
#     (x|y) Indicates a multiple choice type (ps|ump) equals "ps" OR "UMP" 
# 
#     \d    the segment is composed only of numbers, which is equivalent to[0-9].
# 
#     \D    the segment is not composed of numbers, which is equivalent to[^0-9].
# 
#     \s    A space, which is equivalent to [ \t\n\r\r\f\v].
# 
#     \S    No space, which is equivalent to[^ ^ \t\n\r\f\v].
# 
#     \w    Alphanumeric presence, which is equivalent to[a-zA-Z0-9_].
# 
#     \W    No alphanumeric presence[^a-zA-Z0-9_].
# 
#     \     Is an escape character

# Let's try it 
# 
# If the answer is not None, it means the match matches. GREY is indeed a name beginning GR followed by a character and ending with Y

# In[ ]:



print(re.match("GR(.)?Y", "GREY")) 
# (.)? means that we expect 0 or 1 character


# In[10]:


pattern="GR(.)?Y"
string="GREY"

result = re.match(pattern, string)
print(result)

# It is equals to
prog = re.compile(pattern)
result = prog.match(string)
print(result)


# In[ ]:


#  So in a loop the second syntax is nice
pattern="GR(.)?Y"
prog = re.compile(pattern)
l=["GREY 'S","GRAY","GREYISH","A GREY"]
for elem in l:
    result = prog.match(elem)
    print(elem,result)


# To search for specific expressions in a character string.

# In[ ]:


print(re.findall("GR(.)?Y", "GREY"))
# so here we are looking for a unique element (.)? between GR and Y


# In[ ]:


# Ditto for two characters to be found
re.findall("G(.)?(.)?Y", "GREY")


# To keep only the numbers : 

# In[ ]:


# Only numbers
print(re.findall("([0-9]+)", "Hello I live on the 7th floor of 220 street of sims"))
# "+" Means 1 or more characters


# And conversely, if you only want to keep the words. 

# In[ ]:


# Only words
print(re.findall("([A-z]+)", "Hello I live on the 7th floor of 220 street of sims"))


# ### Stop, we recap !

# Character | Meaning   
# :-------------------------:|:-------------------------:
# **.** | **Refers to any character.**
# **^** | **Indicates that the beginning of the string must match <br/> (i.e. a string can only match if it starts in the same way, <br /> if it is preceded by spaces or a line break)**
# **$** | **Indicates that the end of the chain must match <br /> (the same remark as above applies, but at the end level).**
# **{n}**|**Indicates that the previous character must be repeated n times.**
# **{n, m}**|**Indicates that the previous character must be repeated between n and m times.**
#  *| **The previous character can be repeated none or several times. <br />For example, ab* may correspond to: a, ab, or a followed by any number of b.**
# **+**|**The previous character can be repeated once or several times. <br/>For example, to ab+ corresponds an a followed by any number of b.**
# **?**|**The previous character can be repeated zero or once.<br /> For example, to ab? correspond ab and a.**
# **\w** | **it corresponds to any alphabetical character, it is equivalent to [a-zA-Z].**
# **\W** | **it corresponds to everything that is not an alphabetical character.**
# **\d** | **it corresponds to any numeric character, i.e. it is equivalent to[0-9].**
# **\D** | **it corresponds to everything that is not a numeric character.**

# ![alt text](http://www.codercaste.com/wp-content/uploads/2013/01/regex.gif)

# ### Some useful resources
# http://www.rexegg.com/regex-quickstart.html  
# http://www.dreambank.net/regex.html#examples  
# https://pythex.org/ *(Pythex is a real-time regular expression editor for Python, a quick way to test your regular expressions.)*   
# https://regex101.com/   
# *(Regex101 is online regex editor and debugger. Regex101 allows you to create, debug, test and have your expressions explained for PHP, PCRE, Python, Golang and JavaScript. The website also features a community where you can share useful expressions.)*

# #### How to check that the entered string is that of a number ?

# In[ ]:


nb = input('Your number : ')
if (re.match("^[0-9]+$", nb)): 
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number")


# Another way

# In[ ]:


prog = re.compile("^[0-9]+$")
if  prog.search(nb) is not None : 
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number")


# ## Drill 

# 
# **1. Create a regex that finds integers without size limit.**

# In[ ]:


s='sssgdds8sfsfs'


# **2. Create a regex that finds negative integer without size limit.**

# In[ ]:


s='sssgdds-8sfsfs'


# **3. Create a regex that finds (positive or negative) integer without size limit.**

# In[ ]:


s='sssgdds-8s8fsfs'


# **4. Capture all the numbers of the following sentence :**

# In[ ]:


text = '21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy.'


# **5. Find all words that end with 'ly'.**

# In[ ]:


text = "He had prudently disguised himself but was quickly captured by the police."


# **6. License plate number**  
# A license plate consists of 2 capital letters, a dash ('-'), 3 digits, a dash ('-') and finally 2 capital letters. Write a script to check that an input string is a license plate (input () method).  
# If it's correct, print "good". If it's not correct, print "Not good".

# In[ ]:


plate = input("Enter your License plate number:")


# **7 . Address IPV4**  
# An IPv4 address is composed of 4 numbers between 0 and 255 separated by '.'   
# Write a script to verify that a string entered is that of an IPv4 address (input() method)

# In[ ]:


ip = input("Enter your IP address :")


# **8. Valid Mail**  
# An email is composed of alphanumeric characters followed by @ and a domain name.  
# Write a script that checks that the string entered by a User is indeed that of an email, otherwise ask him to re-enter it again (until he gets a valid email)?

# In[ ]:


mail = input("Enter your email :")


# **9. Valid Password**  
# Add in the script the verification of the password (obviously if the email is valid) where the only specificity of the password is to contain at least 6 characters

# In[ ]:


password = input("Enter your Password :")


# **10. Valid Password bis**  
# The password must now contain at least 6 characters:  
# At least one lowercase letter AND at least one uppercase letter AND at least one number AND at least one special character (among $#@).

# In[ ]:


password = input("Enter your Password :")


# **11. Search by groups**  
# It is possible to search by group, and it is very powerful!  
# ``?P<x>\w+`` means the capture of a "group" named x, this group is an alphanumeric (\ w) of at least one character (+)

# In[ ]:


m = re.search("Welcome to (?P<where>\w+) ! You are (?P<age>\d+) years old ?", "Welcome to olivier ! You are 32 years old ?")
print(m.group('where'))
print(m.group('age'))


# In[ ]:


# Another Example
m = re.search("^(?P<who>\w*)[.]?(?P<who2>\w*)@(?P<operator>\w+)[.](?P<zone>\w+$)", "audrey.boulevart@benextcomapgny.com")
if m is not None:
   print (m.group("who"))
   print (m.group('who2'))
   print (m.group('operator'))
   print (m.group('zone'))  


# Load the file ``./assets/mail.txt`` and clean it with the regex. The goal is to retrieve the last name, first name, operator and zone, as in the previous example. And store these information in associated lists.

# In[ ]:


list_mail = open("../data/mail.txt")


# **12. Another way of doing things.**

# In[16]:


mail="audrey.boulevart@benextcomapgny.com"
splitMail = mail.replace('.',' ').split('@').copy()

firstName =[]
name =[]
ope =[]
zone =[]

firstName.append(splitMail[0].split()[0])
name.append(splitMail[0].split()[-1])
ope.append(splitMail[1].split()[0])
zone.append(splitMail[1].split()[-1])

firstName, name, ope, zone


# Repeat the previous exercise with this new formula and compare the length of your lists with those of the previous exercise.  
# What do you notice ?

# In[ ]:




