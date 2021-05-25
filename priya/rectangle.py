class rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        return self.length * self.width
    def display(self):
        print("The Area Of Rectangle: ", self.Area())
class volume(rect):
    def __init__(self, length, width, height):
        rect.__init__(self, length, width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.height
    def dis(self):
        print("The Volume of Rectangle: ", self.volume())
