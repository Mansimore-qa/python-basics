from selenium.webdriver.common.devtools.v130.css import set_local_fonts_enabled


class Bank_Account:

    Bank_Name = "Credence National Bank" # class variable
    def __init__(self, customer_name, account_number, balance=0 ): # Constructor/ Initializer
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance


    def account_details(self):
        print(f"\nBank Name : {self.Bank_Name}"
              f"\nCustomer Name : {self.customer_name}"
              f"\nAccount Number : {self.account_number}"
              f"\nBalance : {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of rs {amount} is successful in {self.customer_name}'s account "
              f"and the new balance is rs {self.balance}.")

    def withdraw (self, amount):
        self.balance -= amount
        print(f"Withdrawal of rs {amount} is successful from {self.customer_name}'s account "
              f"and the remaining balance is rs {self.balance}.")




# 01. Create an object of class Bank_Account
print("# Create an object of class Bank_Account")
account1 = Bank_Account("Rahul", "1234567890", 50000) # account1 --> Object
account2 = Bank_Account("Pooja", "9876543215", 20000) # account1 --> Object


# 02. Access the methods
print("# Access the methods")
account1.account_details()
account1.deposit(5000)
account1.withdraw(40000)

#Changing class variable for account2
account2.Bank_Name = "Credence International Bank"

account2.account_details()
account2.deposit(1000)



#01. Single inheritance
print("\n#01. Single inheritance")

class Saving_Bank_Account(Bank_Account):# child class

    def __init__(self, customer_name, account_number, balance=0, interest_rate = 0.05): # Constructor/ Initializer
        super().__init__(customer_name, account_number, balance)
        self.interest_rate = interest_rate


    def cal_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f" Interest on account {self.customer_name}'s saving account : rs {interest_amount} and "
              f"your new balance amount is {self.balance}")



print("\n Create the object of Saving_Bank_Account class")
saving_account1 = Saving_Bank_Account("Vijay", 234543212345, 10000, 0.1)


print("\n Access the methods of Saving_Bank_Account class")
saving_account1.cal_interest()


print("\nAccessing the Bank_Account's class methods from Saving_Bank_Account's object")
saving_account1.deposit(10000)
saving_account1.withdraw(5000)



#02. Multilevel inheritance
print("\n#02. Multilevel inheritance")


class Minor_Saving_Bank_Account(Saving_Bank_Account):

    def __init__(self, customer_name, account_number, balance=0, interest_rate = 0.05, age = 0 ): # Constructor/ Initializer
        super().__init__(customer_name, account_number, balance, interest_rate)
        self.age = age


    def minor_account_detail(self):
        print(f"\nMinor Bank account. \nAccount Holder_name : {self.customer_name} \nAge : {self.age} \nBalance : {self.balance} ")


print("\n Create the object of Minor_Saving_Bank_Account class")
minor_account1 = Minor_Saving_Bank_Account("Amit", 1234565432, 10000, 0.1, 16)


print("\n Access the methods of Minor_Saving_Bank_Account class")
minor_account1.minor_account_detail()


print("\nAccessing the Saving_Bank_Account's class methods from Minor_Saving_Bank_Account's object")
minor_account1.cal_interest()

print("\nAccessing the Bank_Account's class methods from Minor_Saving_Bank_Account's object")
minor_account1.deposit(3000)
