#example on list

list1=[1,2,-3,-4,5,6,7]
a=len(list1)
print(a)
for i in range(-1,-(a),-1):
    print(list1[i],end=' ')
print()
for i in range(a):
     print(list1[i],end=' ')
