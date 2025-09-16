import numpy as np
dt=[('name','S15'),('class',int),('height',float)]
details=[('Rushika',7,5.2),('Saanvi',8,5.3),('Rishita',3,4.7)]
student=np.array(details,dtype=dt)
print("orignal array: ",student)
print("acending sort by height")
print(np.sort(student,order='height'))