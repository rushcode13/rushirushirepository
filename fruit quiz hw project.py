import random
class fq:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','bannana':'yellow'}
    def quiz(self):
        while (True):
            fruit,color=random.choice(list(self.fruits.items()))
            print('what is the color of{}'.format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option=int(input("eneter 0 if you want to play again and eneter 1 if u dont:  "))
            if(option):
                break
print("welcome to fruit quiz")
FRQ=fq()
FRQ.quiz