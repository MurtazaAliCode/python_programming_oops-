# creat an accout class with 2 attributes balance and account no.
# creat method to dabit and credit & display the balance.

class account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        return f"Account No: {self.account_no}, Balance: {self.balance}"
        print("you total balance is :",self.balance)

    def credit(self, amount):
        self.balance += amount
        return f"Account No: {self.account_no}, Balance: {self.balance}"
        print("you total balance is :",self.balance)


    def total_balance(self):
        return f"Your tatal Balance: {self.balance}"    

account1 = account(1000, 123456)

# print total balance
print(account1.total_balance(),"\n")

# first print debit method
print("first print debit method")
print(account1.debit(500),"\n")

# then print credit method
print("then print credit method")
print(account1.credit(1000),"\n")


# encapsulation is a way to restrict access to some of the object's components.
# to warp every thing like class, method, attribute etc. in a single unit is called encapsulation. 
