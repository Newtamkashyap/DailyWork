#W.A.P to find max number of two number.
num1=int(input("enter ist number"))
num2=int(input("enter 2nd number"))
result=f'{num1}is max'if num1>num2 else f'{num2}is max' #this is expression can not write in different line.
print(result)

print('--------------------------------------We can write like this also---------------------------------')

num1=int(input("enter ist number"))
num2=int(input("enter 2nd number"))
if num1>num2:
    print(f'{num1}is max number')

else:
    print(f'{num2}is max number')
