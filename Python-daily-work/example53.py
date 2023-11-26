list1=[1,2,3,4,5,6,7,8,9,0]
print(list1)

#sort() using for sorting the value from ascending to descending and descending to ascending.
list1.sort()
print(list1)

list1.sort(reverse=True)# decending order if reverse = True
print(list1)
list1.sort(reverse=False)# ascending order if reverse =False;this is real and true work of sort
print(list1)


list2=["d","e","b","k","m","o"]
print(list2)

list2.sort()
print(list2)
print(len(list2))
a=list2
print(a)

list3=["d","e","b","A","M","K","m","o"]
list3.sort()
print(list3)
list3.sort(key=str.upper)
print(list3)
list3.sort(key=str.upper,reverse=False)
print(list3)

list5=["A","B","D","K","C"]
list5.sort(key=str.upper,reverse=True)
print(list5)

#count(value)function is using here
list8=[1,2,3,3,4,5,6,6,6,67]
print(len(list8))
list8.count(3)
print(list8)


