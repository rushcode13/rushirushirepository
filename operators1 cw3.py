English=int (input("enter your marks in English"))
Math=int (input("enter your marks in Math"))
Science=int (input("enter your marks Science"))
Hindi=int (input("enter your marks in Hindi"))
Kannada=int (input("enter your marks in Kannada"))
sum=English+Math+Science+Hindi+Kannada
print("the sum of all 5 marks is" ,sum)
average=sum/5
print("the average of all the marks is" ,average)
percentage=(sum/500)*100
print("the percentage of all the marks is" ,percentage)

amount=int(input("enter amount: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 rupee",note1)
print("notes of 50 rupee",note2)
print("notes of 10 rupee",note3)