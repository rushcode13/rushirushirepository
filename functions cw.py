def wishes():
    print("hiiiiiiiiiiiiiiiiiiiiii")
    print("have a nice day")

wishes()

def weather_condition():
    print('the weather is pleasent in:',spring)
    print('the weather is same in:',autmn)

spring='autmn'
autmn=spring
    
weather_condition()




def add(P,Q):
    return P+Q

def sub(P,Q):
    return P-Q

def mul(P,Q):
    return P*Q

def div(P,Q):
    return P/Q

print("select the operation")
print("a.Add\nb.subtract\nc.multiply\nd.divide")

choice=(input("please enter choice (a/b/c/d)"))
num_1=int(input("enter the first number"))
num_2=int(input("enter the second number"))

if choice=='a':
    print("result :",add(num_1,num_2))
elif choice=='b':
    print("result :",sub(num_1,num_2))
elif choice=='c':
    print("result :",mul(num_1,num_2))
elif choice=='d':
    print("result :",div(num_1,num_2))
else:
    ("this is a invalid input")