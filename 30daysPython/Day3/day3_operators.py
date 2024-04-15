# Exercises - Day 3

# 1. Declare your age as integer variable
age = 36

# 2. Declare your height as a float variable
height = 5.7

# 3. Declare a variable that store a complex number
complex_number = 3+2j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input("Enter Base of triangle:")
height = input("Enter Height of triangle:")
area = 0.5 * float(base) * float(height)
print(str(area))

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = int(input("Enter a:"))
side_b = int(input("Enter b:"))
side_c = int(input("Enter c:"))
permiter = side_a+side_b+side_c
print(str(permiter))

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter length:"))
width = float(input("Enter Width:"))
area , permiter = (length * width) , (2 * (length+width))

print(str(area) +":"+str(permiter))
