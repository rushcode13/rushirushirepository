mc=input("did you have a medical cause Y or N:")
att=int(input("enter the attendace of the student"))
if mc=='Y':
    print("you are allowed")
else:
    if att>=75:
        print("allowed")
    else:
        print("not allowed")
    