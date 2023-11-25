#Display +ve and -ve value from list.
list1=[10,20,30,-20,2,-2,5,6,-19,-30]
a=len(list1)
for i in range(a):
    if list1[i]<0:
        print(list1[i],end=' ')
print()
for i in range(a):
    if list1[i]>=0:
        print(list1[i],end=' ')
