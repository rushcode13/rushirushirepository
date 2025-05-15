print("This is a program to get the reverse order of digits")
y=int(input("please enter the whole number altogether"))
x=0
while y>=0:
 digit=y%10
 x=x*10+digit
 y=y//10
print(x)
