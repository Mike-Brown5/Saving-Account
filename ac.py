class Account:
    def __init__(self, file):
        self.file = file
        with open(file, "r+") as f:
            self.balance = int(f.read())

    def withdraw(self, amount):
        self.balance= int(self.balance) - int(amount)

    def deposit(self,amount):
        self.balance=int(self.balance)+int(amount)

    def submit(self):
        with open(self.file, "w") as f:
            f.write(str(self.balance))

ac = Account("balance.txt")
bl= ac.balance
print(f"Your Balance is {bl}$")
print("\n1-Withdraw. \n2-Deposit.")
user = input("\nWhat do you want to do:")
if user=="1":
    use=input("Enter the Amount:")
    if int(use) > ac.balance :
        print("\nYou don't have enough money.")
    else:
        ac.withdraw(use)
        bl= ac.balance
        ac.submit()
        print(f"You have Withdrawn {use} your remaining balance is {bl}$")
else:
    use=input("Enter the Amount:")
    ac.deposit(use)
    bl= ac.balance
    ac.submit()
    print(f"You have Deposited {use} your New balance is {bl}$")