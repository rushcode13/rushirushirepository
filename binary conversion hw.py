num=int(input("enter a value"))
#ans=num//2
#rem=num%2
#ans1=ans//2
#rem1=ans1%2
#ans2=ans1//2
#rem2=ans2%2
#ans3=ans2//2
#rem3=ans3%2
ans=num
s=''
while ans>0:
    rem=ans%2
    ans=ans//2
    s=str(rem)+s
print("the number in binary is",s)