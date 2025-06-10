try:
   i=int(input("please enter your age"))
   rem=i%2
   if rem==0:
    print("your age is a even number")
   elif rem==1:
    print("your age is a odd number")
except ValueError:
    print("invalid entry")
else:
    print("your age is",i)
    