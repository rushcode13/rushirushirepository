class circle:
    def radi(self):
        self.i=float(input("eneter the radius of the circle"))
    def ansa(self):
        self.ans=3.14*self.i*self.i
        print("the area of the circle is:",self.ans)
    def ansp(self):
        self.ans=2*3.14*self.i
        print("the perimeter of the circle is:",self.ans)
c=circle()
c.radi()
c.ansa()
c.ansp()
