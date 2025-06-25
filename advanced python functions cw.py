n1=[1,2,3]
n2=[4,5,6]
res=map(lambda x,y:x+y,n1,n2)
print("addition of 2 lists")
print(list(res))
#################################################################
num=[1,2,84,4,50,6]
def sq(n):
    return n*n
squ=list(map(sq,num))
print("the squares of the numbers in the list are:",squ)
##################################################################
l1={3,5,6}
l2={'s','g','k'}
ans=list(zip(l1,l2))
print(ans)
##################################################################
li1=[10,20,30,40]
li2=[400,234,122,106]
for x,y in zip(li1,li2[::-1]):
    print(x,y)
##################################################################
comp={'tcs','persistent','codingal'}
prices=[234,321234567,223456776543212345655]
new_comp={comp:prices for comp,
          prices in zip(comp,prices)}
print(format(new_comp))
###################################################################
for i in range (10):
    if i==5:
        print(exit)
        exit()
    print(i)