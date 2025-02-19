## part 0 - make errors

# Uncomment the lines below and fix all of the syntax and logical errors in this statement. It should 
# print "Print this when there are no errors"
# my_error = Its not working!"
# if "working" not in my_error
#     print"Print this when there are no errors")
# ese: 
#     print("its still not working

my_error = "Its not working!"
if "working" not in my_error:
    print("Print this when there are no errors")
else: 
    print("its still not working")


## Part 1 - Basic math 
# make a variable called my_pi and make it 3.14
my_pi = 3.14
# make a variable called radius_inches, give it the value 5 as a float 
# use the my_pi variable you made to calculate the area of a circle with
# that radius
radius_inches = 5.0
circle_area = my_pi * radius_inches**2
print("circle area (inches^2):", circle_area)

# Modify your program so that radius_inches is taken from a user input
radius_inches = float(input("Enter radius in inches: "))
circle_area = my_pi * radius_inches**2
print("circle area (inches^2):", circle_area)

# Modify your program so that the area of the circle is only calculated
# if the user inputs more than 10
radius_inches = float(input("Enter radius in inches greater than 10: "))
if radius_inches > 10.0:
    circle_area = my_pi * radius_inches**2
    print("circle area (inches^2):", circle_area)
else:
    print("Radius input is less than or equal to 10")

# Make another variable, with an appropriate name,
# that converts radius_inches to centimeters and displays both inches and 
# centimeters in a sentence. 
# To get centimeters, multiply the inch value by 2.54
# # use print(f'') to print the string 
radius_inches = float(input("Enter radius in inches: "))
radius_cm = 2.54 * radius_inches
print(f'The radius is {radius_inches} inches which is equivalent to {radius_cm} centimeters')

## Part 2 math module
# import math into this file
import math
# print pi using the math module
print(math.pi)
# Make a variable called math_radius and make it a float with the value five
# use math.pi to find the circumference and store it in a 
# variable named circle_circumference 
# use print(f'') to print a string that displays the radius and circumference
math_radius = 5
circle_circumference = math.pi * 2.0 * math_radius
print(f'The radius is {math_radius} and the circumference is {circle_circumference}')

# Make a variable called square_root_me and ask the user to input an integer
# Print the user input and result of the square root of that number using the math module
square_root_me = int(input("Enter an integer: "))
print(f'The square root of {square_root_me} is {math.sqrt(square_root_me)}')

# Make a variable called my_number and another called power_of which both
# take user input. Use the math module to print the user inputs, the result of my_number 
# to the power of power_of
my_number = float(input("Enter a number to apply the power operator to: "))
power_of = float(input("Enter power value to apply: "))
print(f'My number {my_number} to the power of {power_of} is {math.pow(my_number, power_of)}')

# If I have a right angle triangle that has a opposite side of 5 inches, and a
# adjacent side of 3 inches, find the missing side and the degrees or radians
# of all of the angles of the triangle. Store them all in appropriately 
# named variables and print them in a print(f'') string 
opposite_side = 5
adjacent_side = 3
hypotenuse_side = math.sqrt(math.pow(opposite_side, 2) + math.pow(adjacent_side,2))
angle_adjacent = math.degrees(math.atan(opposite_side/adjacent_side))
angle_opposite = 90.0 - angle_adjacent
print(f'The triangle hypotenuse is {hypotenuse_side}')
print(f'The adjacent triangle angle is {angle_adjacent} degrees')
print(f'The opposite triangle angle is {angle_opposite} degrees')

# Modify this code to accept user input for the adjacent and opposite sides
# of the triangle and display in radians 
opposite_side = float(input("Enter opposite: "))
adjacent_side = float(input("Enter adjacent: "))
hypotenuse_side = math.sqrt(math.pow(opposite_side, 2) + math.pow(adjacent_side, 2))
angle_adjacent = math.atan(opposite_side/adjacent_side)
angle_opposite = math.pi/2.0 - angle_adjacent
print(f'The triangle hypotenuse is {hypotenuse_side}')
print(f'The adjacent triangle angle is {angle_adjacent} radians')
print(f'The opposite triangle angle is {angle_opposite} radians')

## Part 3 - Strings + Math

# Create a program that asks the user if they want the area or circumference of 
# a circle. Then ask them what the radius of the circle is. Store their 
# answer in appropriately named variables. 
# if the user asked for area, calculate the area, if they asked for 
# circumference, calculate circumference 
# and display the result. 

radius = float(input("Enter radius: "))
choice = input("Enter letter 'c' for circumference or 'a' for area: ")
if choice == 'c':
    circle_circumference = math.pi * 2.0 * radius
    print("circle circumference:", circle_circumference)
elif choice == 'a':
    circle_area = math.pi * math.pow(radius,2)
    print("circle area:", circle_area)

# Create a program that asks the user for their favorite ice cream flavor
# use the length of their response (the number of characters in 
# the string) as their lucky number. Display their lucky number 
favourite_ice_cream = input("What's your favourite ice cream flavour? ")
print(f'Your lucky number is {len(favourite_ice_cream)}')

# BONUS QUESTION # 
# A circular room with a radius of 5 m can hold 10 people
# for every additional 1m of radius, the room can hold 5 more people
# Given the number of people as input, print the area of the circle that holds them
# if there are less than 10 people the room is 5m
people = int(input("how any people?"))
if people > 10:
    radius = 5 + 1 + (people-11)//5
else: 
    radius = 5
print(radius)
circle_area = math.pi*math.pow(radius,2)
print(circle_area)

hypotenuse_side = math.sqrt(hypotenuse_side)