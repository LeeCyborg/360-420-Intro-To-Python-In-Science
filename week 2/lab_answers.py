'''
PART 1: Types and arithmetic operators
'''

# 1. Make a variable called "pi" that has the value 3.14
#    Print the type of that variable
pi = 3.14

# 2. Make a new variable called "three" and use the variable "pi"
#  to assign the value 3 by using integer divide // 
three = pi//1



# 3. Order of operations works like it does in math (BEDMAS / PEMDAS)
#    Uncomment these 2 lines (delete the # part) and run the file:
print(3 * 2 ** 2)
print((3 * 2) ** 2)
'''
PART 2: Strings, string operators, and string methods
'''
# 1. Make two variables for your first and last names.
#    Give the variables whatever names you think are reasonable.
first_name = "lee"
last_name = "wilkins"

# 2. Print those together as one string, using '+' to concatenate them.
print(first_name + last_name)

# 3. Write a new print statement that includes a space between the two variables
#    Using concatentation, print your first name, a space, and your last name all
#    on one line.
print(first_name + " " + last_name)

# 4. Make a string variable with any string value. Give a name that makes sense
#    for that value.
#    Use math operators to print it 5 times
my_catchphrase = "lee rocks"
print(my_catchphrase * 4)
# 5. String operations also follow order of operations (BEDMAS/PEDMAS)
# Given these two variables, use string operations to print 'Hello!!' and 'Hello! Hello!'
say = "hello"
tone = "!"
print(say + tone*3)
print((say+tone)*3)
# 6. Using string indexing, make a new variable that has your first initial
#    (from your first name variable), followed by a period (.), a space ( ),
#    and your last name.
#    Remember: in Python, we count the index starting from 0 (that is, the first
#    letter has an index of 0, the second has an index of 1, etc)
#    We call this "zero-indexing" or "zero-based indexing"
first = "lee"
last = "wilkins"
name = first[0]+". "+last
print(name)
# bonus for capitalizing print(first[0].upper()+". "+last.capitalize())

# 7. We can use negative numbers to index backwards from the end of a string.
#    So, -1 is the last character, -2 is the second to last, etc.
#    Make a variable with the value 2025. Make sure it's a string.
#    Then use negative index numbers to make a new variable called two_digit_year
#    with just the last two digits of the current year.
year = "2025"
two_digit_year = year[-2:]

# 8. Now use slicing to print the second to fifth characters of the 'greeting' variable above
greeting = "hello"
print(greeting[1:6])

# 9. Using your previous variables and string interpolation (f-string), create a variable with
#    a personalized message to yourself that includes your name and the year. Print it.
my_greeting = f'{greeting}, my name is {name} and it is {year}'
print(my_greeting)
# 9. Print an all-caps version of your message using the .upper() method
print(name.upper())

# 10. How many letter e's are in your message? Use the .count() method to print it.
print(my_greeting.count("e"))

# 11. Create a program that takes user input and asks the user a yes or no question. Make 
# the program respond whether the user inputs capital letters or lower case letters 
my_answer = input("what is the question?")
if "yes" in my_answer.lower(): 
    print("its there")
else:
    print("its not there")

# 12. Print a sentence including the name of the 2, 3, and 10th object of this list using split and print format (print)
#my_list = "a cat, a dog, a monkey, a rabbit, a snake, a hamster, a whale, a bug, a spider, a cow, a chicken, a bird, a duck, an airplane"
# bonus for removing all the white space at the beginning and end AND between 

my_list = "cat, dog, monkey, rabbit, snake, hamster, whale, bug, spider, cow, chicken, bird, duck, airplane"
# my_list = my_list.replace(" ", "")
my_list = my_list.split(",")
print(f'my fav animals are {my_list[1]} and {my_list[2]} and {my_list[9]}')