#multicpication("*") is used to perform two number.
#int
n1=20
n2=30
n3=n1*n2
print(n3)
print(type(n3))

#float
n4=2.0
n5=3.0
n6=n4*n5
print(n6)
print(type(n6))

#complex
n7=20+2j
n8=30+3j
n9=n7*n8
print(n9)
print(type(n9))

a=2
b=True
c=(a*b)
print(c)
print(type(c))

a1=2
b2=False
c1=(a1*b2)
print(c1)
print(type(c1))


#string(cannot multiply)
n10="hello"
n11="World"
n12=n10*n11
print(n12)
print(type(n12))
#Traceback (most recent call last):
#  File "C:/Users/newtam/OneDrive/Desktop/Python_Folder/example28.py", line 26, in <module>
 #   n12=n10*n11
#TypeError: can't multiply sequence by non-int of type 'str'
