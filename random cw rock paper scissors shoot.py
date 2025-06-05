import random
while True:
    user_ac=input("enter a choice[rock,paper,scissors]")
    possible_ac=["rock","paper","scissors"]
    comp_ac=random.choice(possible_ac)
    print(f"you choose{user_ac}and the computer choose{comp_ac}")

    if user_ac==comp_ac:
        print("its a tie")
    elif  user_ac=="rock":
        if comp_ac=="scissors":
          print("rock smashes scissors u win!")
        else:
           print("paper covers rock u lose!")

    elif  user_ac=="scissorr":
        if comp_ac=="paper":
          print("scissor cuts paper u win")
        else:
           print("rock smashes scissor u lose!")

    elif  user_ac=="paper":
        if comp_ac=="scissors":
          print("xcissor cuts paper u lose!")
        else:
           print("rock smashes scissors u win!")
    else:
       print("invaid choice")          
