print("""
Inheritance :
It is a mechanism, in which one class acquires the property of another class.
It means reusing existing blueprint or prototype in another class .
""")

class Calculator:# parent class
    power_source = "Battery"

    def __init__(self,
                 brand,
                 model,
                 price,
                 colour):  # Constructor/ initializer
        self.brand = brand  # self.brand  -- > variable , brand -- > value
        self.model = model
        self.price = price
        self.colour = colour


    def add(self,
            a,
            b):
        sum = a + b
        print(f" The sum of {a} + {b} = {sum}")

    def sub(self,
            a,
            b):
        sub = a - b
        print(f" The sub from  {a} - {b} = {sub}")

    def mul(self,
            a,
            b):
        mul = a * b
        print(f" The mul of  {a} * {b} = {mul}")

    def cal_info(self):
        print(f"Brand name of the calculator is {self.brand}. \nThe power source of this calculator is {self.power_source}"
            )


#Create an object/instance of class calculator
print(f"\n01. Create an object/instance of class calculator")
# syntax --> object_name = class_name()

cal1 = Calculator("Samsung", "S1", "200", "black")
cal2 = Calculator("Apple", "A1", "400", "white")
cal3 = Calculator("Casio", "C1", "250", "Red")


#Access the methods
print("\n Access the methods")
cal1.add(10,5)
cal1.sub(10,5)
cal1.mul(10,5)
cal1.cal_info()
print(Calculator.power_source)



#01. Single inheritance
print("\n#01. Single inheritance")

class Scientific_Calculator(Calculator):# child class

    def square(self, num):
        print(f"The square of {num} : {num**2}")

    def square_root(self, num):
        print(f"The square root of {num} : {num**1/2}")


# Creating an object
print("# Creating an object of Scientific_Calculator")
sci_cal1 = Scientific_Calculator("HP", "HP101", "2000", "Silver")

# Accessing the Scientific_Calculator's methods
print("# Accessing the Scientific_Calculator's methods")
sci_cal1.square(4)
sci_cal1.square_root(4)

# Accessing the Calculator's class methods from Scientific_Calculator's object
print("# Accessing the Calculator's class methods from Scientific_Calculator's object")
sci_cal1.add(10,2)
sci_cal1.sub(10,2)
sci_cal1.cal_info()

print(Scientific_Calculator.power_source)

#cal1.square(4) # we cannot access the child class method using parent class object.


#02. Multiple inheritance
print("\n#02. Multiple inheritance")

class Tax_Calculator: # parent class
    def cal_tax(self,amount,tax_rate ):
        print(f" For amount {amount} and for tax_rate {tax_rate}, "
              f"you total tax amount will be {amount*(tax_rate/100)}")


class Finance_calculator(Calculator, Tax_Calculator): # child class
    def calculate_interest(self, principal_amount, interest_rate, time_period):
        print(f"Interest_amount {((principal_amount * interest_rate * time_period)/100)}")


# Creating an object
print("\nCreating an object of Finance_calculator")
fin_cal1 = Finance_calculator("Casio", "CS201", "2400", "Black")

# Accessing the Finance_calculator's methods
print("\nAccessing the Finance_calculator's methods")
fin_cal1.calculate_interest(1000,10,1)


# Accessing the Calculator's class methods from Finance_calculator's object
print("\nAccessing the Calculator's class methods from Finance_calculator's object")
fin_cal1.add(10,2)
fin_cal1.sub(10,2)
fin_cal1.cal_info()


# Accessing the Tax_Calculator's class methods from Finance_calculator's object
print("\nAccessing the Tax_Calculator's class methods from Finance_calculator's object")
fin_cal1.cal_tax(1000,10)





#03. Multilevel inheritance
print("\n#03. Multilevel inheritance")

class Advance_Calculator(Finance_calculator):

    def __init__(self, brand, model, price, colour, interest_rate):  # Constructor/ initializer
        super().__init__(brand, model, price, colour) # inherit the constructor from parent class
        self.interest_rate = interest_rate

    def cal_compound_interest(self, principal_amount, time_period):
        Amount = principal_amount * ( 1 + (self.interest_rate/100)**time_period)
        Compound_Interest  = Amount - principal_amount
        print(f" Compound_interest--> {Compound_Interest}")



# Creating an object
print("\nCreating an object of Advance_Calculator")
adv_cal1 = Advance_Calculator("Casio", "CS201", "2400", "Black", 10)


# Accessing the Advance_Calculator's methods
print("\nAccessing the Advance_Calculator's methods")
adv_cal1.cal_compound_interest(10000,2)

# Accessing the Finance_calculator's class methods from Advance_Calculator's object
print("\nAccessing the Finance_calculator's class methods from Advance_Calculator's object")
adv_cal1.calculate_interest(100,10,10)


# Accessing the Calculator's class methods from Advance_Calculator's object
print("\nAccessing the Calculator's class methods from Advance_Calculator's object")
adv_cal1.add(10,2)
adv_cal1.sub(10,2)
adv_cal1.cal_info()


