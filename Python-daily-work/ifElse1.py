#WAP to find input character is alphabet,digit or special characters.
char=input("enter any character")
print("alphabet") if char>='A' and char<='Z' or char>='a' and char<='z' else print("digit") if char>='0' and char<='9' else print("special character")
