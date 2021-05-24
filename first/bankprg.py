class bank:
    def __init__(self):
        self.blnc=20000
        self.name=""
        self.location=""
        self.dep=0
        self.w=0

    def get(self):
        self.name=input("enter your name")
        self.location=("enter your location")

    def deposit(self):
        self.dep=int(input("enter the amount to be deposited"))
        self.blnc+=self.dep
        print("your balance after deposit is="+str(self.blnc))

    def withdraw(self):
        self.w=int(input("enter the amount to be withdrwan"))
        self.blnc-=self.w
        print("your balance after withdrawal is="+str(self.blnc))