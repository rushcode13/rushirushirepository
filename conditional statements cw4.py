num=1
if num > 0:
     print(num,"is a positive number")
num=-3
if num < 0:
    print(num,"is a negitive number")

actualcost=float(input("please enter the actual products price"))
salescost=float(input("please enter the sales amount"))
if(salescost>actualcost):
   amount=salescost-actualcost
   print("total profit = {0}.format(amount)")
else:
  print("no profit")

  i=int(input("enter a number:"))
  if(i<15):
      print("i is smaller than 15")
      print("i'm in if block")
  else:
     print("i is greater than 15")
     print("i'm in if block")
     print("im not in if block and not in else block")
     
if i%2==0:
    print("the number is even")
else:
    print("the number is odd")

