def cube(number):
    return number*number*number
def divided_3(number):
    if number %3==0:
        return cube(number)
    else:
        return False
print(divided_3(9))
print(divided_3(5))

     