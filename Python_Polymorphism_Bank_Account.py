print("""
What is polymorphism ?
The same method behaves differently depending upon the object which is calling it.
Polymorphism has two types 
1. Method overriding and 
2. Method overloading.
""")




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
print("\n Access the methods")
account1.account_details()

#Changing class variable for account2
account2.Bank_Name = "Credence International Bank"




print("\n01. Method overriding : The subclass or child class redefines the behavior of method as in parent class."
      "Here parameters are same as parent class ")


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



print("\n Create the object of Saving_Bank_Account class")
saving_account1 = Saving_Bank_Account("Vijay", 234543212345, 10000, 0.1)


print("\n Access the methods of Banking_Account class")
account1.account_details()


print("\n Access the methods of Saving_Bank_Account class")
saving_account1.account_details()



print("\n02. Method Overloading : Redefining the uses of parameter or arguments in a method.")

class Current_Bank_Account(Bank_Account):

    def account_details(self):
        print(f"\n This is Current bank account") # method overriding
        super().account_details() # It should work same as parent class method.

    def deposit(self, *amount): # Method Overloading
        for i in amount:
            self.balance += i
            print(f"Deposit amount of rupees {i} is successful in{self.customer_name}'s account"
                  f"and the New Balance is {self.balance}")


print("\n Create the object of Current_Bank_Account class")
crt_account1 = Current_Bank_Account("Vijay", 4234543234, 10000)


print("\n Access the methods of Banking_Account class")
account1.account_details()
account1.deposit(1000)


print("\n Access the methods of Current_Bank_Account class")
crt_account1.account_details()
crt_account1.deposit(1000, 500, 400,100, 50, 25, 25)


# search for investment baking/ healthcare domain example for polymorphism

# charges-parent
# intra day - child 2
# long terms - 1
# short 0
# options 1.5
# future 10

