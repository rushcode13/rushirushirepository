#activity 1
try:
    number=int(input("enter a number"))
    print("the number you entered is",number)
except ValueError as x:
    print("There is a error, you are not supposed to enter a string with alphabets please enter a integer")
#activity 2
try:
    num1,num2=eval(input("enter 2 numbers seprated by are a coommmmmmmmmmma:"))
    result=num1/num2
    print("after division the answer is",result)
except ZeroDivisionError:
    print("no zeros allowed")
except SyntaxError:
    print("very bad you forgot to put a comma")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this statement will print no matter what")
#activity 3
valid=False
while not valid:
    try:
        n=int(input("enter a number"))
        while n%2==0:
            print("bye")
            valid=True
    except ValueError:
        print("invalid")
    
