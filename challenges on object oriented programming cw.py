#activity no.one flashcards
class flashcard:
    def __init__(self,word,meaning):
      self.word=word
      self.meaing=meaning
    def __str__(self):
       return self.word+': '+self.meaing
flash=[]
print("welcome to the best flashcard appplication in the worllllllld :) ")
while True:
   word=input("eneter the word")
   meaning=input("eneter the word meaning")
   flash.append(flashcard(word,meaning))
   option=int(input("if you want to continue please press 1 or if you dont want to " \
   "please press 0"))
   if (option)==0:
      break
print("your flashcard/s:")
for i in flash:
   print(i)
########################################################################################
#######################################################################################
class A:
    def __init__(self,a):
       self.a=a
    def __lt__(self,other):
       if(self.a<other.a):
               return"ob1 is less than ob2"
       else:
               return"ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "both are equal"
        else:
            return "not equal"
ob1=A(2)
ob2=A(3)
print("passed values are:",ob1.a,ob2.a)
print(ob1<ob2)
ob3=A(4)
ob4=A(4)
print("passed values are:",ob3.a,ob4.a)
print(ob3==ob4)
