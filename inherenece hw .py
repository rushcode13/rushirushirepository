class vehicle:
    def __init__(self,tax):
       self.tax=tax
       print("the tax is",tax)
class bus(vehicle):
    def __init__(self,km,tax):
       self.km=km
       fare=km*5
       print("the total fare is",fare)
       total=fare+tax
       print("the total fare and tax is",total)
       vehicle.__init__(self,tax)
obj=bus(10,2)

