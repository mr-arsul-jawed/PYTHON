#datetime module is used to work with dates as date objects.
#datetime module supplies classes for manipulating dates and times in both simple and complex ways.
import datetime

Date = datetime.datetime.now()
# print(Date)

#random module is used to generate random numbers.

#-------Example:1 - this is use randint() function to generate random number between 1 to 10.
# import random

# res = random.randint(1, 10)
# print(res)


#-------Example:2 - This is use choice() function to generate random string from list.
# L = ["hello", "hi", "bye"]
# res = random.choice(L)
# print(res)


#-------Example:3 - This is use choice() function to generate random number from list.
# dice = [1, 2, 3, 4, 5, 6]
# res = random.choice(dice)
# print(res)

#  math module is used to work with mathematical operations.

#-------Example:1 This is find out the max and min values and power values.
import math

max_val = max(1,2,3,5,7)
# print(max_val)

min_val = min(1,2,3,5,7)
# print(min_val)

power_val = pow(2, 3)
# print(power_val)

#-----Example:2 This is find out the square root value.

sqrt_val = math.sqrt(121)
# print(sqrt_val)

#-----Example:3 This is find out the factorial value.

fact_val = math.factorial(5)
# print(fact_val)


abs_val = abs(-7) # This is find out the absolute value.
# print(abs_val)

#-----Example:4 This is find out the ceil and floor value.

ceil_val = math.ceil(7.8) # This is find out the ceil value.
# print(ceil_val)

floor_val = math.floor(7.8) # This is find out the floor value.
# print(floor_val)







