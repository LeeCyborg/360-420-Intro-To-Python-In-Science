import math

my_angle_degrees = 90
my_angle_radians = math.radians(my_angle_degrees)
print(f'{my_angle_degrees} degrees is {my_angle_radians} radians')

print(math.degrees(1)) 
# this takes radians, prints degrees 
print(math.radians(90)) 
# this takes degrees, prints radians  

another_angle_radians = 1.1
another_angle_degrees = math.degrees(another_angle_radians)
print(f'{another_angle_degrees} degrees is {another_angle_radians} radians')


# # my_angle_degrees = float(input("Enter an angle in degrees: "))
# # my_angle_radians = math.radians(my_angle_degrees)
# # print(f'{my_angle_degrees} is {my_angle_radians} in radians')


# my_num = math.sqrt(4)
# print(my_num)
# my_num = math.pow(4, 4)
# print(my_num)

# p = [3]
# q = [1]
# # Calculate Euclidean distance
# print (math.dist(p, q))
# p = [3, 3]
# q = [6, 12]
# # Calculate Euclidean distance
# print (math.dist(p, q))


# # Create a program that finds the hypotenuse of a triangle by asking the user to 
# # enter any opposite or adjacent measurement using the math module 
# print("Hello, I am a triangle. I am looking for my hypotenuse. ")
# opposite = float(input("enter opposite side: "))
# adjacent = float(input("enter adjacent side: "))

# hypotenuse = math.sqrt(math.pow(opposite, 2)+math.pow(adjacent,2))

# print(f"thank you. My hypotenuse is {hypotenuse} ")
# now find all of the angles 
# print(" now find my missing angle")

# angle1 = math.degrees(math.atan((opposite/adjacent)))


# angle3 = 180-(angle1+90)

# A circular room with a radius of 5 m can hold 10 people
# for every additional 1m of radius, the room can hold 5 more people
# Given the number of people as input, print the area of the circle that holds them
# if there are less than 10 people the room is 5m

# people = int(input("how any people?"))

# if people > 10:
#     radius = 5 + 1 + (people-11)//5
# else: 
#     radius = 5
# print(radius)
# circle_area = math.pi*math.pow(radius,2)
# print(circle_area)

