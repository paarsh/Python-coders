class Bank:

    def __init__(self):
        self.name = " "
        self.age = " "
        self.address = " "
        self.phone = " "
        self.branch = " "

        self.result = 0
        self.balance = 0

    def details(self):

        self.name = input("Name \n")
        self.age = int(input("Age\n"))
        self.address = input("Address\n")
        self.phone = int(input(" phone\n"))
        self.branch = input("Branch")

    def deposit(self):
        amount = float(input("Deposit "))
        self.balance += amount
        print(" \n Amount Deposited:", amount)

    def withdraw(self):

        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(" \n You Withdraw:", amount)
        else:
            print(" \n Insufficient balance")

    def display(self):

        print(" \n Net Available Balance=", self.balance)