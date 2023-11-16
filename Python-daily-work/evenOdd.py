#Conditional Operators.
#w.A.p to find input number is even or odd
num=int(input("enter any number"))
a=num%2 #remainder should be zero
b=f'{num} is even'if a==0 else f'{num} is odd'
print(b)

print("------------------------------------------------------------------------")

#2nd way to find odd and even number
num=int(input("enter number"))
if num%2==0:
    print(f'even number')
else:
    print(f'odd number')



