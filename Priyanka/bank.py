


class bank:

    def __init__(self):
        self.name = " "
        self.age = " "
        self.address = " "
        self.phone = " "
        self.branch = " "

        self.result = 0
        self.balance = 20000

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


    # inherited the bank class

class Account(bank):
    def __init__(self):
            super().__init__()
            self.username = " "
            self.password = " "
            self.login_username = " "
            self.login_password = " "

    def registration(self):
        super().details()
        self.username = input("Enter username\n")
        self.password = int(input("Enter password\n"))

    def login(self):
            print(" login username:")
            self.login_username = (input())

            print("login password:")
            self.login_password= int(input())

            if (self.login_username == self.username) and (self.password == self.login_password):

                print("Net Available Balance=", self.balance)
            else:
                print("can't login to account")

