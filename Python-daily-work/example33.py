#WAP to input roll no,,name,3subject marks
#calculate total,avg marks.

rollno=int(input("enter rollno:"))
name=input("enter name:")
subj1=int(input("enter subj1 marks:"))
subj2=int(input("enter subj2 marks:"))
subj3=int(input("enter subj3 marks:"))
totalMarks=subj1+subj2+subj3
print(f'total marks={totalMarks}')
avgMarks=totalMarks/3
print(F'avr marks={avgMarks}')
