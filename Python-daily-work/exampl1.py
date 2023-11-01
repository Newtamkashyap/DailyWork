Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> "hello"
'hello'
>>> a=hello
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> a="hello"
>>> 
>>> 
>>> a
'hello'
>>> print(a)
hello
>>> demo="""hello world
... how are you
... i am fine world
... hpw are you"""
>>> print(demo)
hello world
how are you
i am fine world
hpw are you
>>> '''hello
... how
... are
... ypo'''
'hello\nhow\nare\nypo'
