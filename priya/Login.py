class bank:
    def __init__(self):
        self.bal = 5000
        self.name = ""
        self.loc = ""
        self.dep = 0
    def get(self):
        self.name = input("Enter your name: ")
        self.loc = input("Enter your branch:")
    def deposit(self):
        self.dep = int(input("Enter the Amount u want to deposit: "))
        self.bal = self.dep
        print("The Amount u have deposited is: ", + int(self.bal))
    def withdraw(self):
        self.wit = int(input("Enter the amount you want to withdraw: "))
        self.bal = self.bal-self.wit
        print("Your balance after withdrawl is: ", + int(self.bal))
