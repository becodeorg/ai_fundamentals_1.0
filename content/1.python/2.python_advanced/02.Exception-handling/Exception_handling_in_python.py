# %%
"""
# Exception handling
"""

# %%
"""
Exception handling allows a program to deal with runtime errors and continue its normal execution.
Consider the following instructions:

"""

# %%
a=input("Enter integer: ")
num=int(a)
inverse=1/num
print(number,inverse)

# %%
"""
What happens if the user enters a null or non-numeric value? The program will stop and raise an error as shown below.
"""

# %%
"""
```
Traceback (most recent call last):
File "", line 3, in
<u>ZeroDivisionError: division by zero</u>
```
"""

# %%
"""
```
Traceback (most recent call last):
File "", line 2, in
<b>ValueError: invalid literal for int() with base 10: 'sss'</b>
```
"""

# %%
"""
Error messages provide information about the line that caused the error by tracing back to the function calls that lead to this instruction. The line numbers of the function calls are displayed in the error message to enable quick correction of the code.  

An error that occurs during execution is also called an exception. How can you deal with an exception so that the program can catch the error and prompt the user to enter a correct number?

"""

# %%
"""
## try and except
See the difference. 
in the first case, the program crashes and the last `print("finished")` instruction did not execute.  
"""

# %%
3 / 0
print("Finished")

# %%
"""
If the "try" instruction is used, the error is detected and the program is not interrupted. 
"""

# %%
try:
    3 / 0    
except:
    print('Not ok, there is an error')

print("Finished")

# %%
"""
Now, we will try to avoid the exceptions mentioned above by rewriting our code as follows.   
We have the ability to capture the type of exception
"""

# %%
try:
    3/0
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except ValueError:
    print("Error: Non-numeric value")
except BaseException:
    print("Error: there is a problem")

# %%
try:
    3/int('ssss')
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except ValueError:
    print("Error: Non-numeric value")
except BaseException:
    print("Error: there is a problem")

# %%
"""
### Finally and else
try/except can be completed with two other keywords: finally and else.  
else is the block executed if no exception is thrown:
"""

# %%
try:
    3/3
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except ValueError:
    print("Error: Non-numeric value")
except BaseException:
    print("Error: there is a problem")
else: 
    print("Everything is ok")

# %%
"""
I'll do executing in the end no matter what.finally is a block that is executed after all other blocks have been executed, regardless of whether there was an exception or not, and **even if the program crashes**. 

"""

# %%
try:
    3/0
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except ValueError:
    print("Error: Non-numeric value")
except BaseException:
    print("Error: there is a problem")
finally: 
    print("I'll do executing in the end no matter what..")

# %%
"""
### raise
"""

# %%
"""
It is possible to trigger exceptions ourselves.
"""

# %%
"""
``raise`` a python statement that can trigger any Error. This means that an error is explicitly triggered. 
"""

# %%
def division(num, div):
    if div == 0:
        raise ZeroDivisionError()
    else:
        return num / div

division(5,0)

# %%
"""
Well we agree, the function ``division()`` is completely useless! 

### Creating an exception
As you can imagine, we can create our own executions. 
Just create a class that will inherit the "Exception" class.
"""

# %%
class MyError(Exception):
    pass

# %%
raise MyError("Hello")

# %%
