print("""
What is polymorphism ?
The same method behaves differently depending upon the object which is calling it.
Polymorphism has two types 
1. Method overriding and 
2. Method overloading.
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



print("Method overriding : The subclass or child class redefines the behavior of method as in parent class."
      "Here parameters are same as parent class ")


class Scientific_Calculator(Calculator):

    def square(self, num):
        print(f"The square of {num} : {num**2}")

    def square_root(self, num):
        print(f"The square root of {num} : {num**1/2}")

    def add(self,a,b): # this code is different than parent class but method name  and parameters are  same.
        print("This method is for addition, created in Scientific_Calculator class ")
        sum = a + b
        return sum

    def sub(self, a, b): # this code is different than parent class but method name  and parameters are  same.
        print("This method is for Subtraction, created in Scientific_Calculator class")
        sub = a - b
        return sub

# Creating an object
print("# Creating an object of Scientific_Calculator")
sci_cal1 = Scientific_Calculator("HP", "HP101", "2000", "Silver")

# Accessing the Scientific_Calculator's methods
print("\nAccessing the Scientific_Calculator's methods")

print(sci_cal1.add(10,2))
print(sci_cal1.sub(10,2))
sci_cal1.mul(10,2)



print("\nMethod Overloading : Redefining the uses of parameter or arguments in a method.")


class Finance_Calculator(Calculator):

    def calculate_interest(self, principal_amount, interest_rate, time_period):
        print(f"Interest_amount {((principal_amount * interest_rate * time_period)/100)}")


    def mul(self, *args): #(10*20*30*40)
        result = 1
        for i in args :
            result *= i
        return  result

    def add(self, a, b , c = 0):
        sum = a + b + c
        print(f" The sum of {a} + {b}  + {c}= {sum}")



# Creating an object
print("\nCreating an object of Finance_calculator")
fin_cal1 = Finance_Calculator("Casio", "CS201", "2400", "Black")

# Accessing the Finance_calculator's methods
print("\nAccessing the Finance_calculator's methods")
print (fin_cal1.mul(10*20*30*40))
fin_cal1.add(1,2, 3)

fin_cal1.add(1,2)



