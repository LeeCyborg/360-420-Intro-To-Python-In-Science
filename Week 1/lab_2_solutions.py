
# Exercise 0
# Part 1
# Create a program that asks the user for how many minutes the user has been using their computer. 
# Calculate how many hours that is, and display the answer

# howManyMinutes = float(input("how many minutes did it take? "))
# hours = howManyMinutes / 60
# print("it took",hours,"hours")

# Part 2
# Create a program that asks the user for the temperature outside in celsius, convert
# convert their answer to Farenheit

# deg_c = int(input("What is the temp? "))
# # formula to convert C to F is: (degrees Celcius) times (9/5) plus (32)
# deg_f = deg_c * (9 / 5) + 32

# print(deg_c, " degrees Celsius is", deg_f, " degrees Farenheit.")

# Part 3
# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you
# return home after 10 nights you would return home on a Saturday (day 6) 
# Write a general version of the program which makes variables for the starting 
# day number and for the length of your stay, and it will tell you the number of 
# day of the week you will return on.

startDay = 0
daysGone = 6
dayBack = (startDay+daysGone)%7
print(dayBack)

# Exercise 1 
# Create a program where the user inputs 2 numbers. If the sum of those two numbers is under 
# 10, tell them they succeed. If it isn't, tell them they fail 
'''
num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))


if (num1+num2) < 10: 
    print("Correct!")
else: 
    print("try again")
'''

# Exercise 2
# Create a program where the user can pick between cake or pizza. If the user picks pizza, 
# as them how many slices they want. If the user picks pie, tell them there is none left. If they
# select anything else, tell them its not available 
# Bonus:
# Make a list of foods, For each food, make an unique set of questions to determine the user's
# preference in quantity and flavor. If the food isn't on the list, end the program. 

'''
myFood = input("Do you want pizza or cake?  ")

if "pizza" in myFood: 
    input("Okay, how many slices? ")
elif "pie" in myFood:
    print("There is none left")
else: 
    print("that wasn't an option")
'''

# Exercise 3
# Make a program where the user inputs a number. Tell them if it is even or odd
'''
num1 = int(input("Input a number: "))

if (num1 % 2): 
    print("It is odd")
else: 
    print("It is even")
'''