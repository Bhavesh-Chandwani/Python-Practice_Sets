class BankAccount:
    def __init__(self, __balance):
        self.__balance = __balance  #Private attribute created
    
    #Let's write the methods which performs operation on attribute.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Amount : {amount}. New Balance : {self.__balance}")
        else:
            print(f"The amount cannot be negative.")

    def withdraw(self, amount):
        if  0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew : rs{amount}. Remaining Balance : {self.__balance}")
        else:
            print("Invalid withdraw amount or insufficient funds")
    
    def get_balance(self):
        return f"Current Balance : {self.__balance}"
    
account_1 = BankAccount(50000)
account_1.deposit(10000)
account_1.withdraw(5000)
print(account_1.get_balance())