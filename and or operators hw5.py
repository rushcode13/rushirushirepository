height=float(input("enter your height in cm:  "))
weight=float(input("enter your weight in kg:  "))
BMI=weight/(height/100)**2
print("your BMI is",BMI)
if BMI<=18.4:
   print("you are underweight")
elif BMI<=29.4:
   print("you are healthy")
elif BMI<=29.9:
   print("you are overweight")
elif BMI<=34.9:
   print("you are severly overweight")
elif BMI<=39.9:
   print("you are obease")
else:
   print("you are severly obease")