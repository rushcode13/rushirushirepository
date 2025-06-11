L=[4,5,2,7,9,1,3]
print(L)
count=0
for i in L:
    count=count+i
avrg=count/len(L)
print("the avrage of the list is",avrg)
L.sort()
print("smallest number is in the first position",(L[0]))
print("biggest number is in the last position",(L[-1]))
Li=["mom","wow","amazing","sad","yay","not","for","rushika"]
c=0
newlist=[]
for word in Li:
    if len(word)>1 and word[0]==word[-1]:
        c+=1
        newlist.append(word)
print(c)
print(newlist)
