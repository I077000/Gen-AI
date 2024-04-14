# Write a python comment saying 'Day 2: 30 Days of python programming'

"""
Day 2: 30 Days of python programming(inbuilt functions and varibales)
"""

#Declare a first name variable and assign a value to it

import math


first_name = "shrijan"

# Declare a full name variable and assign a value to it
last_name = "shri"

# Declare a country variable and assign a value to it
country = "INDIA"

#Declare a city variable and assign a value to it
city = "Bangalore"

#Declare an age variable and assign a value to it
age = 34

# Declare a year variable and assign a value to it
year = 2024

#Declare a variable is_married and assign a value to it

is_married = True

#Declare a variable is_true and assign a value to it

is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line


a, b = 4, 8
print("value assigned to a")
print(a)
print("value assigned to b")
print(b)

# # Variable assignment in a single line can also be done for different data types.

print("assigning values of different datatypes")
a, b, c, d = 4, "geeks", 3.14, True
print(a)
print(b)
print(c)
print(d)

# Assigning different operation results to multiple variable.

a, b = 8, 3
add, pro = (a+b), (a*b)
print(add)
print(pro)

# we are storing different characters in a different variables.

string = "Geeks"
a, b, c = string[0], string[1:4], string[4]
 
print(a)
print(b)
print(c)


""" Excercise 2:
- Check the data type of all your variables using type() built-in function
- Using the len() built-in function, find the length of your first name
- Compare the length of your first name and your last name
- Declare 5 as num_one and 4 as num_two
- Add num_one and num_two and assign the value to a variable total
- Subtract num_two from num_one and assign the value to a variable diff
- Multiply num_two and num_one and assign the value to a variable product
- Divide num_one by num_two and assign the value to a variable division
- Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
- Calculate num_one to the power of num_two and assign the value to a variable exp
- Find floor division of num_one by num_two and assign the value to a variable floor_division
- The radius of a circle is 30 meters.
- Calculate the area of a circle and assign the value to a variable name of area_of_circle
- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
- Take radius as user input and calculate the area.
- Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
- Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""

print(type(first_name),type(last_name), type(age), type(country), type(city), type(year))

print("Length of first Name: ", len(first_name))

num_one , num_two = 5, 4

total , diff ,  product, division = (num_one+num_two), (num_two-num_one),(num_one*num_two),(num_one/num_two)

print(total,diff,product,division)

reminder = num_one%num_two
print(reminder)

floor_division = num_one//num_two
print(floor_division)

"""
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
"""

radius = 30
radius = float(input("Enter Raidus of  circle"))
area_of_circle = math.pi* math.pow(radius,2)
print("Area: "+ str(area_of_circle) )
circumference_of_circle = 2 * math.pi * radius
print(circumference_of_circle)

print(help('keywords'))


