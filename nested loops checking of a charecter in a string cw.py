string=input("please enter a string  : ")
char=input("please enter a charecter in the string  : ")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
      count=count+1
    i=i+1
print("the total number of times",char,"has occoured==",count)