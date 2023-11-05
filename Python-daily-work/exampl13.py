#type casting or type conversion is the process of converting one type of object to another type.
#for example
#int into float
#int into string
#int into complex
#int into bool
#int into int

#and all these are in-built functions and available in default module imported by any python_builtins except that we have to import any module first like:
import math
math.sqrt(9)
dir(math)


import os
dir(os)
#in this way we can import module/libraries as per our requirements

#--------------------------------------------------------------------------------------------------

a1=int(10)
print(a1)

a2=int(1.2)
print(a2)

a3=int(True)
print(a3)

a4=int(False)
print(a4)

a6=int("65")
print(a6)

#a5=int(1+2j)
#print(a5)
#Traceback (most recent call last):
#  File "C:/Users/newtam/OneDrive/Desktop/Python_Folder/exampl13.py", line 33, in <module>
#    a5=int(1+2j)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'




#a7=int("1.24")
#print(a7)
#Traceback (most recent call last):
#File "C:/Users/newtam/OneDrive/Desktop/Python_Folder/exampl13.py", line 44, in <module>
#  a7=int("1.24")
#ValueError: invalid literal for int() with base 10: '1.24'

#a8=int("a")
#print(a8)

#a9=int("a",base=10)
#print(a9)

#Traceback (most recent call last):
# File "C:/Users/newtam/OneDrive/Desktop/Python_Folder/exampl13.py", line 56, in <module>
#a9=int("a",base=10)
#ValueError: invalid literal for int() with base 10: 'a'

a10=int("ff",base=16)
print(a10)

a11=int("ffff",base=16)
print(a11)

a12=int("1010",base=2)
print(a12)

a13=int("1010")
print(a13)





