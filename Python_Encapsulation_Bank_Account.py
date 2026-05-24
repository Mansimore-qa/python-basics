print(""" Date : 05 - Jan -2026
What is Encapsulation ?
It restricts direct access of variables/attribute and methods of class.
""")

class Bank_Account:

    Bank_Name = "Credence National Bank" # class variable
    def __init__(self, customer_name, account_number, balance=0 ): # Constructor/ Initializer
        # Public attribute - accessible from anywhere
        self.customer_name = customer_name
        # protected attribute - accessible from anywhere, but showing a warning
        self._account_number = account_number
        # private attribute - not accessible from anywhere
        self.__balance = balance


    def deposit(self, amount): # Public Method-accessible from anywhere
        self.__balance += amount
        print(f"Deposit of rs {amount} is successful in {self.customer_name}'s account "
              f"and the new balance is rs {self.__balance}.")

    def withdraw (self, amount): # Public Method-accessible from anywhere
        self.__balance -= amount
        print(f"Withdrawal of rs {amount} is successful from {self.customer_name}'s account "
              f"and the remaining balance is rs {self.__balance}.")

    def _display_account_details(self): # Protect Method-accessible from anywhere, but showing warning
        print(f"Customer Name : {self.customer_name}")
        print(f"Account Number : {self._account_number}")


    def __account_name_balance(self): # private method-not accessible from anywhere
        print(f"Customer Name : {self.customer_name}")
        print(f"Balance  : {self.__balance}")

    def get_balance(self): # public method defined here just to access the private attribute and this public method is called as getter method.
        print(f"Access Balance: {self.__balance}")

    def get_account_name_balance(self): # public method defined here just to access the private method and this public method is called as getter method.
        return self.__account_name_balance()




# 01. Create an object of class Bank_Account
print("\n#01. Create an object of class Bank_Account")
account1 = Bank_Account("Rahul", "1234567890", 50000) # account1 --> Object
account2 = Bank_Account("Pooja", "9876543215", 20000) # account1 --> Object

#02. Accessing the public attribute and methods
print("\n#02. Accessing the public attribute and methods")
print(account1.customer_name) #  public attribute
account1.deposit(100)  #  public method
account1.withdraw(2000)  #  public method

#03. Accessing the protected attribute and methods
print("\n#03. Accessing the protected attribute and methods")
print(account1._account_number) #  protected attribute
account1._display_account_details()  #  protected method

#04. Accessing the private attribute and methods
print("\n#04. Accessing the private attribute and methods")
#print(account1.__balance) #  private attribute --  # Error --> AttributeError: 'Bank_Account' object has no attribute '__balance'
#account1.__account_name_balance()  #  private method -- # Error --> AttributeError: 'Bank_Account' object has no attribute '__account_name_balance'

#05. Accessing the private attribute and methods thr public method
print("\n#05. Accessing the private attribute and methods and methods thr public method")
account1.get_balance()
account1.get_account_name_balance()



print("\n# Child Class- Saving_Bank_Account")

class Saving_Bank_Account(Bank_Account):# child class

    def __init__(self, customer_name, account_number, balance=0, interest_rate = 0.05): # Constructor/ Initializer
        super().__init__(customer_name, account_number, balance)
        self.interest_rate = interest_rate


    # def cal_interest(self):
    #     interest_amount = self.__balance * self.interest_rate
    #     self.__balance += interest_amount
    #     print(f" Interest on account {self.customer_name}'s saving account : rs {interest_amount} and "
    #           f"your new balance amount is {self.__balance}")



print("\n Create the object of Saving_Bank_Account class")
saving_account1 = Saving_Bank_Account("Vijay", 234543212345, 10000, 0.1)



#02. Accessing the public attribute and methods from parent class
print("\n#02. Accessing the public attribute and methods from parent class")
print(saving_account1.customer_name) #  public attribute
saving_account1.deposit(100)  #  public method

#03. Accessing the protected attribute and methods from parent class
print("\n#03. Accessing the protected attribute and methods from parent class")
print(saving_account1._account_number) #  protected attribute
saving_account1._display_account_details()  #  protected method

#04. Accessing the private attribute and methods from parent class
print("\n#04. Accessing the private attribute and methods from parent class")
#print(saving_account1.__balance) #  private attribute --  # Error --> AttributeError: 'Saving_Bank_Account' object has no attribute '__balance'
#saving_account1.__account_name_balance()  #  private method -- # Error --> AttributeError: 'Saving_Bank_Account' object has no attribute '__account_name_balance'


#05. Accessing the private attribute and methods thr public method of parent class
print("\n#05. Accessing the private attribute and methods and methods thr public method")
saving_account1.get_balance()
saving_account1.get_account_name_balance()














'''
ALL SCRIPT RUN 5-10 TIMES AND get the understanding of code every code
put it into the gpt and ask for very simple and clear explanation of code.

All data types
conditional statements
loops--> for
Just check how to define function.
how we can use ready made thing in python, importing
list comprehension just for knowlege.
exception handling
file handling--> excel 
class objects
inheritance


Selenium - 5 to 7 day
Pytest -  5 to 7 day
allure - 1 day
jerkins-GIT - 2 day



Sr. candidates
ETL automation
API automation

'''