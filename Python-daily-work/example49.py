#count even and odd number from a list
list1=[1,2,3,4,5,6,7,8,9,0,10,20,30,40,50,51]
print(list1)
a=len(list1)
ecount,ocount=0,0
for i in range(a):
    if list1[i]%2==0:
        ecount=ecount+1
else:
    ocount=ocount+1
  
    print(f'even number{ecount}')
    print(f'odd number{ocount}')
     

