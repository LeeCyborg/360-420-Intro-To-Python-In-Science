# Write a while loop that counts to 10 and prints the counter


#Write a while loop that begins with "while true" and counts up by 1 every loop.
# It should print the number at every loop
# Make the loop end when the count reaches 10 with break


#write a while loop that asks the user for 2 numbers. Continue the loop
# until the user enters the same number twice



#Write a for loop that prints each number in this list:
my_for_loop_list = [20, 40, 2, 5 ,29]



# Write a loop  to display only those numbers from a list that satisfy the following conditions
#  - The number must be divisible by five
#  - If the number is greater than 150, then skip it and move to the following number
#  - If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]


# Write a function called fruit_mixed that takes one parameter, a list of strings, 
# Write a loop that goes through every item in the list and if the
# item has more than 3 letters, convert every letter A to a B
# print every item as its been altered 


    
# Call the function with this string list
my_string_list = ["apple", "oranges", "bananas"]


# Write a function called add_two_nums which takes two numbers and adds them together 
# and returns the result. 
# In a while loop, call the function with a new number from the user as num2 and num1 as the 
# number from the previous loop. If the result of add_two_nums is greater than 10, keep looping
# and if not, break the loop. 
# use numm1= 10 as a seed for the first loop. 
num1 = 10
def add_two_nums(num1, num2):
    return num1+num2

while True:
    num2 = int(input("new number"))
    print(add_two_nums(num1, num2))
    if add_two_nums(num1, num2) > 10:
        num1 = num2
    else: 
        break
