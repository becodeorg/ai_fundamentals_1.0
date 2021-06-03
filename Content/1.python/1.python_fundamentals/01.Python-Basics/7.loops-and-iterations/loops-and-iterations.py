#!/usr/bin/env python
# coding: utf-8

# # Loops and iteration

# We will now discuss an element more complex and obscure than the conditions, I have named: the loops!  
# 
# Loops are an essential element in programming. They allow instructions to be repeated a number of times. They also help to avoid repetition. Let's say you want to display the numbers from 1 to 10. Without the loops, we should write something like this:

# In[ ]:


print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)


# We could do copy and paste, but it's not clean and a good developer never **repeats himself**. Be [D.R.Y](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), think [D.R.Y](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
# ![Bart, don't reapeat yourself](https://jenwlee.files.wordpress.com/2016/11/bart.jpg)

# ## While

# The while loop repeats the sequence of actions several times until the condition has the value False. The condition is given before the loop body and is checked before each execution of the loop body. As a general rule, the while loop is used when it is impossible to determine the exact number of iterations of the loop in advance.

# The syntax of the while loop in the simplest case looks like this: 

# In[ ]:


while expression:
    block of statements


# Example if you want to display the numbers from 1 to 10.

# In[ ]:


i = 1
while i <= 10:
    print(i)
    i += 1


# In python, the equivalent of the loop do...while does not exist. The loop do...while does not know in advance how many times it will iterate but it will run at least once. On the other hand, it is very easy to create the same behaviour. 

# In[ ]:


while True:
    n = int(input("give a integer > 0 : "))
    print("You have provided", n)
    if n > 0:
        break
print("correct answer")


# ## For

# A `"for"` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# 
# Unlike the for keyword in other programming language, it works more like an iterator method as found in other object-orientated programming languages.
# 
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# With the strings

# In[ ]:


for x in "banana":
  print(x)


# ## Range 

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# In[20]:


for i in range(10):
    print(i)


# In[21]:


for i in range(2 ** 3):
    print(i)


# With starting sprecified : 

# In[22]:


for i in range(4,10):
    print(i)


# With step :

# In[23]:


for i in range(0,10,2):
    print(i)


# ## Continue and Break

# #### Continue

# The instruction "continue" allows you to move on to the next loop turn early. It continues on the next iteration of the loop.

# In[ ]:


for i in range(4):
    print("Start of iteration", i)
    print("Hello")
    if i < 2:
        continue
    print("End of iteration", i)
print("After the loop")


# #### Break

# The instruction "break" is used to interrupt the execution of a loop (while or for). It exits the loop and proceeds to the next instruction.

# In[ ]:


for i in range(10):
    print("Start of iteration", i)
    print("Hello")
    if i == 2:
        break
    print("End of iteration", i)
print("After the loop")


# ## Else 

# Loop instructions have an "else" clause. It is executed when the loop ends with exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is interrupted by a break instruction. This is illustrated in the following loop, which looks for prime numbers:

# In[16]:


i = 1
while i < 10:
    print(i)
    i += 1
else:
    print('Finally finished!, i =', i)


# In[17]:


for i in range(1, 10):
  print(i)
else:
  print("Finally finished!, i =", i) 


# ## [Ok, now pratice](./drill-loops-iterations.ipynb)
