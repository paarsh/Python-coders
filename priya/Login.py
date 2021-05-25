class bank:
    def __init__(self):
        self.bal = 0
        self.name = ""
        #self.loc = ""
        self.dep = 0
    def get(self):
        self.bal = input("Enter your bal:")
        self.name = input("Enter your name: ")
        self.loc = input("Enter your branch:")
    def deposit(self):
       # print("The total amt is:", + int(self.bal))
        self.dep = int(input("Enter the Amount u want to deposit: "))
        self.bal = self.dep
        print("The Amount u have deposited is: ", + int(self.bal))
    def withdraw(self):
        self.wit = int(input("Enter the amount you want to withdraw: "))
        self.bal = self.bal - self.wit
        print("Your balance after withdrawl is: ", + int(self.bal))

class login1(bank):
    def __init__(self):
        super().__init__()
        self.user_name = ""
        self.pwd = ""
        self.lgn_usr = ""
        self.lgn_pwd = ""
    def reg(self):
        super().get()
        self.user_name = input("Enter username:\n")
        self.pwd = input("Enter password:\n")
    def login(self):
        super().deposit()
        super().withdraw()
        print("Enter user's login username")
        self.lgn_usr = input("")
        print("Enter login password:")
        self.lgn_pwd = int(input())
        if(self.lgn_usr == self.user_name) & (self.lgn_pwd == self.pwd):
            print("Net Available balance is: "), + self.bal
        else:
            print("Please check ur username or password!")
