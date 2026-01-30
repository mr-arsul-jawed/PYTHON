#---------------- Random ----------------
import random

# def generate_random_num(start, end):
#     """Generate a random integer between start and end (inclusive)."""
#     return random.randint(start, end)


# result = generate_random_num(1, 100)  # Example usage
# print(f"Random number between 1 and 100: {result}")


l = [1, 2, 3, 4, 5,6]

print(random.choice(l))  # Randomly selects an element from the list


#---------------- date ----------------------
# import datetime


# def get_current_date():
#     """Return the current date in YYYY-MM-DD format."""
#     return datetime.datetime.now().strftime("%d-%m-%Y")


# print(get_current_date())


# x = datetime.datetime.now()
# print(x.strftime("%A")) #Full weekday name
# print(x.strftime("%a")) #short weekday name
# print(x.strftime("%B")) #Full month name
# print(x.strftime("%b")) #short month name
# print(x.strftime("%C")) #century
# print(x.strftime("%c")) #locale's date and time
# print(x.strftime("%D")) #mm/dd/yy
# print(x.strftime("%d")) #day of month
# print(x.strftime("%F")) #yyyy-mm-dd
# print(x.strftime("%H")) #24-hour
# print(x.strftime("%I")) #12-hour
# print(x.strftime("%j")) #day of year
# print(x.strftime("%m")) #month
# print(x.strftime("%M")) #minute
# print(x.strftime("%p")) #AM/PM
# print(x.strftime("%S")) #second
# print(x.strftime("%U")) #week number of year (Sunday as first day)
# print(x.strftime("%W")) #week number of year (Monday as first day)



#---------------- math ----------------------
import math

# def calculate_circle_area(radius):
#     """Calculate the area of a circle given its radius."""
#     return math.pi * (radius ** 2)


# area = calculate_circle_area(5)  # Example usage
# print(f"Area of circle with radius 5: {area}")


x = math.sqrt(64)
# print(x)  

y = math.ceil(5.3)
# print(y)

z = math.floor(5.7)
# print(z)

a = math.factorial(5)
# print(a)

b = math.gcd(48, 180)
# print(b)

c = math.sin(math.radians(30))  # Sine of 30 degrees
# print(c)

d = math.pow(10,2) 
# print(d)

e = math.dist((2,3),(5,7))
# print(e)



