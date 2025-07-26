class BMW:
    def fuel_type(self):
        print("BMW's fuel type is gasoline")
    def max_speed(self):
        print("BMW's speed is 200 miles per hour")
class Ferrari:
    def fuel_type(self):
        print("Ferrari's fuel type is petrol")
    def max_speed(self):
        print("Ferrari's speed is 250 miles per hour")

obj_BMW=BMW()
obj_Ferrari=Ferrari()

for c in (obj_BMW,obj_Ferrari):
    c.fuel_type()
    c.max_speed()
    