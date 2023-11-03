Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(builtins)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dir(builtins)
NameError: name 'builtins' is not defined. Did you forget to import 'builtins'?
>>> a=(input("enter the value"))
enter the value12
>>> b=(input("enter the value"))
enter the value34
>>> c=int(a)+int(b)
>>> print(f'sum of two{a}and{b}is{c}')
sum of two12and34is46
>>> print(f'sum of two number is:,c')
sum of two number is:,c
>>> print(c)
46
