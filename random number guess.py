import random 
number=(random.randint(10,20))
print("i generated a random number from 10 to 20 and now u should give me ur best guess!")
print("the game ends when you guess the number")
while True:
    guess=int(input("come on give me your best one"))
    if guess==number:
        print("you win!! amazing job!")
        break
    else:
        print("nope.... try again")