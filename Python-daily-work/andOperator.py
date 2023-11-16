#logical operators
#and operator-both operator should be satisfied.
#W.A.P to read name and 2 subject  marks ,calculate total avg and result.
name=input("enter name")
sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
totalMarks=sub1+sub2
avg=totalMarks/2
result="pass" if sub1>=40 and sub2>=40 else "fail"
print(totalMarks)
print(avg)
print(result)
