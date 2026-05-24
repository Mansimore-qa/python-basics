# Data Type - Range
# Range is sequence of number, it is immutable.
# It is used to generate number and mostly used to iterate the loop.


#01 Range
print("\n#01 Range")
range1 = range(10)
print(range1)
print(list(range1))
print(f"The data type:{type(range1)}")


#02 Range-example
print("\n#02 Range-example:")
range1 = range(10) # range(value1, value2, value3) -(start-default(0), stop-10, step-default(1))
print(f"print range1-->{range1}-->{list(range1)}")

range2 = range(2,10) # range(value1, value2, value3) -(start-2, stop-10, step-default(1))
print(f"print range2-->{range2}-->{list(range2)}")

range3 = range(2,10,2) # range(value1, value2, value3) -(start-2, stop-10, step-2)
print(f"print range3-->{range3}-->{list(range3)}")

range4 = range(10,0,-1) # range(value1, value2, value3) -(start-10, stop-0, step- -1)
print(f"print range2-->{range4}-->{list(range4)}")


#03 Range-method
print("\n#02 Range-example:")

range1 = range(11)
print(f"print range1-->{range1.index(5)}-->{list(range1)}")
print(f"start value of range1-->{range1.start}")
print(f"step value of range1-->{range1.step}")
print(f"stop value of range1-->{range1.stop}")
print(f"count value of range1-->{range1.count(2)}") # return only 1 or 0