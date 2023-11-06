#WAP to find simple interest.

p=float(input("enter amount"))
t=int(input("enter time"))
r=float(input("enter rate"))
si=p*t*r/100
print(si)
print(f"""
amount:{p}
time:{t}
rate:{r}
simple interest{si:.2f}""")
