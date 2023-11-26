#WAP to add all the values of list
list1=[1,2,3,4,5,6,7,8,9,0]
a=len(list1)
print(len(list1))
total=0
for i in range(a):
    total=total+list1[i]
print(f'total is={total}')
print(f'avg is={total/len(list1)}')
print(f'sum of total={sum(list1)}')
print(f'min value={min(list1)}')
print(f'max value={max(list1)}')


#instead of len(list1) we are dividing ,there we can simply divide by a also.
