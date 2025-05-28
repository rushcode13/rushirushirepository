import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=4
sidelen=88
angle=360.0/numsides
for i in range(numsides):
 polygon.forward(sidelen)
 polygon.right(angle)
turtle.done()
