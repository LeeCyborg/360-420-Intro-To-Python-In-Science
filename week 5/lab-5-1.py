# Write a for loop that counts from 0 to 100 (inclusively) and prints each number 
for x in range(0, 101):
    print(x)

# Write a for loop that counts from 0 to 100 (inclusively) and prints
# only the even numbers 
for x in range(0, 101, 2):
    print(x)

# Write a for loop that counts from 0 to 100 (inclusively) and prints 
# y for even even number and n for every odd number 
for x in range(0, 101):
    if x%2: 
        print("y")
    else: 
        print("n")

# Write a loop that asks the user for a number every loop 9 times
# Add that number to the number of times the loop has run (starting at 1)
# and print "We are on loop {loop number} and our new number is {total}"
# Ex: the total is loop 1 + user number, the second is loop 2+ user number 

for x in range(1, 10):
    user_input = int(input("What is the new number?"))
    print(f"We are on loop {x} and our new number is {x+user_input}")

# Write a for loop that asks the user for a number. Add their number to their
# input from the previous loop and print it. Use the number "4" as
# your seed for the first loop. Run the loop 6 times
num1 = 4
for x in range(0, 6): 
    num2 = int(input("What is the new num?"))
    print(num1+num2)
    num1 = num2

# Write a function called modify_list that asks for user input, an integer called modifier. 
# Loop through the array below and add modifier to each element of the list, 
# and store them all in a new array called numbers_new
numbers = [2, 49, 29, 68, 29 ,10, 49, 60, 288, 21]
number_new = []
def modify_list():
    modifier = int(input("What is the modifier?"))
    for number in numbers: 
        number_new.append(number+modifier)
    print(number_new)
modify_list()

# Write a function called user_count that asks the user for two
# integers, num1 and num2. If num1 is greater than num2 run a for loop that 
# counts between those two numbers by 3 and prints "Three!" at every third 
# number and returns true. 
# If the range number between the numbers is not divisible by 3, 
# don't print anything, and return false.  
# If the user enters an invalid input, raise a value error. 
def user_count(): 
    try: 
        num1 = int(input("What is the first number? "))
        num2 = int(input("What is the second number? "))
        if (num1 > num2) and ((num1-num2)%3==0):
            for x in range(num2, num1,3):
                print("Three")
                return True
        else: 
            return False
    except ValueError:
        print("try again")
user_count()

# Write function called letter_checker that 
# takes a string called my_letter, and a boolean called count_flag
# If count_flag is true, loop through the array below. 
# If the my_letter appears at all in each word, replace
# it with the letter "z" and print each modified item only.
# If count_flag is false, reverse the entire list order
# and print it. 
animals = ["duck", "bear", "pig", "rat", "hamster", "bird", "cat" ]
def letter_checker(my_letter, count_flag):
    if count_flag:
        for animal in animals:
            if animal.count(my_letter) > 0:
                animal = animal.replace(my_letter, "z")
                print(animal)
    else:
        animals.reverse()
        print(animals)

# Call letter_checker with the result of user_count and the letter a
letter_checker("a", True)

### Bonus Floyds Triangle ####
# Floyd’s Triangle is a right-angled triangular array
# of natural numbers, where each row contains an incremented 
# sequence of numbers starting from 1. It is named after
# Robert Floyd, who popularized this pattern. This triangle 
# is constructed by filling the rows with consecutive 
# integers, and each row contains one more element than 
# the previous row.
# # 
# Here is an example of Floyd’s Triangle with 5 rows:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# As you can see, the numbers start from 1 and increment 
# by 1 in each row. The number of elements in each row corresponds
# to the row number.  

# Write a function called print_floyds_triangle that takes one 
# parameter, rows. Rows should indicate the number of rows of the 
# triangle to produce. Try to do this using for loops (or for loops
# inside other for loops!)

# https://www.prepbytes.com/blog/python/python-program-to-print-floyds-triangle/
def print_floyds_triangle(rows):
    number = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()
# Example usage
num_rows = 5
print_floyds_triangle(num_rows)
