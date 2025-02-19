# Make a function that adds two and three together. Call the function.
def my_function():
    answer = 2 + 3
# Make another function that prints the result of two plus three. 
# Do not call the function. 
def my_printing_function():
    print(3+5)
# make another function that adds three and five, 
# and assigns the result to a variable named my_result. 
def my_result_function():
    result = 3 + 5
    return result
my_result = my_result_function()
# make a function that adds any two numbers together and prints the result
def my_adding_function(num1, num2):
    print(num1+num2)
# Ask the user to input 2 numbers, use 
# the two numbers in two different functions. The first function
# should return the area of a square, the second should return the
# perimeter of a square. Print both in a single printf statement
my_length = int(input("What is the length?"))
my_width = int(input("What is the width?"))
def my_area_function(length, width):
    result = length * width
    return result
def my_perimeter_function(length, width):
    result = (length*2) + (width*2)
    return result
print(f'The perimeter is {my_perimeter_function(my_length,my_width)} and the area is {my_area_function(my_length,my_width)}')
# Or, you could do
# my_area = my_area_function(my_length,my_width)
# my_perimeter = my_perimeter_function(my_length,my_width)
# print(f'The perimeter is {my_perimeter} and the area is {my_area}')
