class dog:
    speciality='amazing'
    speciality2='awesome'
    def __init__(self,name,color,breed):
       self.name=name
       self.color=color
       self.breed=breed
obj1=dog('Coco','White','Poodle')
obj2=dog('Hazel','Dark golden','Golden Retriever')
print(obj1.name,"is",obj1.speciality,'! Its color is',obj1.color,',and its breed is',obj1.breed)
print(obj2.name,"is",obj2.speciality2,'! Its color is',obj2.color,',and its breed is',obj2.breed)