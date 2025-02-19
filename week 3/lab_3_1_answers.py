## Explain the following problem as Purpose, Input, and Output
# If there is a factory with any number of workers, and they are all working 8 hour shifts
# and earning 14 dollars an hour, what is the cost to pay all the workers, per day? 
# Ask for the input inside the function


# Purpose: To determine the cost of work per day
# Input: Number of workers 
# Output: total cost 

# Write pseudo code for the above problem 
# declair a function called worker_wages 
# Input the number of workers
# Multiple the number of workers by the number of hours 
# Multiply the result by the hourly rate 
# Print out the result in total cost 

## Now write and call this problem as a single function called worker_wages. Then call the function. 
def worker_wages():
    workers = int(input("number of workers: "))
    shift_hours = 8
    wage = 14
    cost = (workers*shift_hours) * wage
    print(cost)

worker_wages()

## write the purpose, input, and output for this function, and 
#  pseudo code for a function called grocery_boxes that solves this problem:
# In every grocery box there are at 3 fruits, two pieces of meat, and 4 canned goods. 
# Inside the function, Ask for the user to input how many times per week they want the box delivered. 
# How many items are given each week, based on user input?
# Print the total items delivered per week. 

# Purpose: Determine number of total grocery items delivered per week
# input How many boxes per week
# output: number of total items

def grocery_boxes():
    how_may_per_week = input("How many per week?")
    fruits = 3
    meat = 2
    cans = 4
    per_box = fruits+meat+cans
    total = int(how_may_per_week) * per_box
    print(total)

grocery_boxes()

## Make a new function similar to grocery_boxes but ask the user for how many of each item they want in their grocery box. This
# new function is named grocery_boxes_cost. Have it print the total cost assuming
# fruits are 1$, meat is 5$ and cans are 2$
# Print in the following strict format using print(f''): 
# You ordered {how_may_per_week} boxes per week, with {fruits} fruits, {cans} cans, {meat} meats, and it cost {total}$

#  Write the purpose, input and output

# Purpose: To determine the cost of grocery boxes
# Input: how many per week, how many cans, how many meats, how many fruits
# output: A string indicating the cost in the above format 

def grocery_boxes_cost():
    how_may_per_week = int(input("How many per week?"))
    fruits = int(input("How many fruits ?"))
    meat = int(input("How many meats?"))
    cans = int(input("How many cans?"))
    fruit_cost = (fruits * 1)*how_may_per_week
    meat_cost = (meat * 5)*how_may_per_week
    can_cost = (cans * 2)*how_may_per_week
    total = fruit_cost + meat_cost + can_cost
    print(f' You ordered {how_may_per_week} boxes per week, with {fruits} fruits, {cans} cans, {meat} meats, and it cost {total}$')

grocery_boxes_cost()

# Create a function weather_outside that takes no parameters. Inside the function, ask the user is asked 
# what the temp is outside as temp_outside
# Create a boolean variable called is_cold. If temp_outside is less than 15, make is_cold true and print is_cold. 
# Do not call the function. 

def weather_outside():
    temp_outside = float(input("What is the temp?"))
    is_cold = temp_outside < 20
    print(is_cold)

#Now call the function. 
weather_outside()

# Create a function called my_input_function that takes no parameters. Ask the user to input two numbers, add them
# together and print the result. Call the function. 

def my_input_function():
    take_my_number = int(input("What is the number? "))
    what_to_add = int(input("What do I add to it? "))
    print(take_my_number + what_to_add)

my_input_function()
