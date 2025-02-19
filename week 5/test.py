# Write piece of code that adds "rat" at position 1 in the array below
# print the result 
animals = ["lions", "tigers", "bears" ]
animals.insert(1, "rat")
print(animals)

#Write a piece of code that removes the element 3 of the animals list and
# print the result 
animals.pop(3)
print(animals)

# Write a loop that turns the list into all capital letters. 
# Print the animals list in all capitals. 
for index, animal in enumerate(animals):
    animals[index] = animal.upper()
print(animals)

# Make a new list called num_chars that contains only the number of characters in 
# each element of the animals list
# Print the new num_chars list
num_chars = []
for animal in animals:
    num_chars.append(len(animal))
print(num_chars)

# Make a function called animal_list_checker that takes no parameters.
# Create a loop that asks the user for an animal. If the animal 
# is in the possible_animals list and not in the animals list,
# add it to the animals list and print 
# if it isn't in the possible_animals list, add it to the rejected_animals list. 
# If the animal is already in the animals, print "its already at {index}" 
# and ends the loop"
# When the loop is done, return a list of rejected animal. 
# Write a docstring to describe the function. 
# Do not call the function

# Use these lists 
# animals = ["lions", "tigers", "bears"]
# possible_animals = ["fish", "bird", "cat", "dog" ]

def animal_list_checker():
    """ Check if user input animals are in a set list. Breaks when 
    an input is already in the list. 
    Args: none
    Return: a list of rejected animals. 
    """
    animals = ["lions", "tigers", "bears"]
    possible_animals = ["fish", "bird", "cat", "dog" ]
    rejected_animals = []
    while True: 
        user_input = input("What animal is next?")
        if user_input in possible_animals and user_input not in animals:
            print("We've added it to the list. ")
            animals.append("user_input")
        elif user_input in animals:
            print(f"Its there and it is at {animals.index(user_input)}")
            break
        else: 
            print("That animal is a reject!")
            rejected_animals.append(user_input)
    return rejected_animals

# Write a function called animal_shout that takes one parameter,
# a list of strings. The function should print each element of the
# list in all capital letters without altering the list. 
def animal_shout(animal_list):
    for animal in animal_list:
        print(animal.upper())
#call animal_shout with the returned list of animal_list_checker 
animal_reject_list = animal_list_checker()
animal_shout(animal_reject_list)

# Create a loop that iterates through each element of 
# the num_list list below and removes every element that 
# contains the number 3 and put them in a new list called
# three_nums. Print both lists. 
num_list = ["339", "62", "592", "94", "4", "43", "542"]
three_nums = []
for i, nums in enumerate(num_list):
    if "3" in nums: 
        three_nums.append(nums)
        num_list.pop(i)
print(num_list)
print(three_nums)

## Bonus: Make the same function work with the following list:
# Why does it not work, and what is your fix? 
tricky_num_list = ["339", "362", "592", "94", "34", "43", "542"]
three_nums = []
non_three_nums = []
for i, nums in enumerate(tricky_num_list):
    if "3" in nums: 
        three_nums.append(nums)
    else: 
        non_three_nums.append(nums)
print(non_three_nums)
print(three_nums)

# Write a function called sq_nums that takes an list of integers
# The function should return a new array that 
# contains only the square root of each element in the list
import math
def sq_nums(my_list):
    new_sq_list = []
    for nums in enumerate(my_list):
        new_sq_list.append(math.sqrt(int(nums)))
    return new_sq_list

# Call that function sq_nums with the list below and print the 
# second element in the new list
sq_list = [34,36,1,77,352,485]
print(sq_nums(sq_list)[1])
# or
# my_var = sq_nums(sq_list)
# print(my_var[1])


# plt.plot([1, 2, 3, 4], 
#          [1, 4, 9, 16], 'ro')
# plt.axis((0, 6, 0, 20))
# plt.show()

