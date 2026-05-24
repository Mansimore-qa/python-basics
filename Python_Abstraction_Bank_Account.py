
print(""" Date : 05 - Jan -2026
What is Abstraction ?
Abstraction enforce the subclass or child class to
implement the same method which is present in a base class or parent class.

""")


from abc import ABC, abstractmethod


class Bank_Account(ABC): # this bank account is defined as abstract class

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

    @abstractmethod # decorator --> Enhance the functionality of the method
    def deposit(self, amount):
        pass
    '''
   The deposit method is not defined here in a 
   bank_account abstract class. we have to define this into the child class. 
    '''

    @abstractmethod
    def withdraw (self, amount):
        pass
    '''
   The withdraw method is not defined here in a 
   bank_account abstract class. we have to define this into the child class. 
    '''



class Saving_Bank_Account(Bank_Account):# child class

    def __init__(self, customer_name, account_number, balance=0, interest_rate = 0.05): # Constructor/ Initializer
        super().__init__(customer_name, account_number, balance)
        self.interest_rate = interest_rate


    def cal_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f" Interest on account {self.customer_name}'s saving account : rs {interest_amount} and "
              f"your new balance amount is {self.balance}")


    def account_details(self):
        print(f"\n This is saving bank account")
        super().account_details() # It should work same as parent class method.


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of rs {amount} is successful in {self.customer_name}'s account "
              f"and the new balance is rs {self.balance}.")

    def withdraw (self, amount):
        self.balance -= amount
        print(f"Withdrawal of rs {amount} is successful from {self.customer_name}'s account "
              f"and the remaining balance is rs {self.balance}.")


print("\n Create the object of Saving_Bank_Account class")
saving_account1 = Saving_Bank_Account("Vijay", 234543212345, 10000, 0.1)



print("\n Access the methods of Saving_Bank_Account class")
saving_account1.account_details()
