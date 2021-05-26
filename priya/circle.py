class cir:
   def __init__(self):
        self.rad = 0.0
        self.pi = 3.14
        self.app = 0.0
   def get(self):
        self.rad = float(input("Enter the radius of circle:\n"))
   def start(self):
        self.app = self.pi*(self.rad**2)
   def out(self):
        print("Area of circle is: "+ str(self.app))
