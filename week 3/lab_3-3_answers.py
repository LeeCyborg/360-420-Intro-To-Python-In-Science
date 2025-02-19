# # ## Write a function called threshold_num that takes one parameter.
# # # Inside the function, write a statement that checks if the number is
# # # above 0 and below 10 (non inclusively), print a statement that says in range. If it is out of range,
# # # print a statement that it is out of range. Do not call the function. 

# def threshold_num(myNum):
#     if (myNum > 0) and (myNum < 10):
#         print("my number is in range ")
#     else:
#         print("num is out of range" )

# # # Now all the function 4 times, with number 0, 5, 10, 11. Your program should print
# # # 0 is out of range 
# # # 5 is in range
# # # 10 is out of range
# # # 11 is out of range

# threshold_num(0)
# threshold_num(5)
# threshold_num(10)
# threshold_num(11)

import math
def power_square(num):
    return math.pow(math.sqrt(num), 2)
power_square(2)

def greeting(name_1, day_of_week_1):
    name = name_1.capitalize[0]
    day_of_week = day_of_week_1.capitalize[0]
    print(f"Hi, {name}! It's {day_of_week}")
#greeting("lee", "monday")

# # # Write a similar function to be called threshold_num_input to take user input 
# # # inside the function rather than as a parameter of the function. Call the function. 
# def threshold_num_input():
#     myNum = int(input("What is the num?"))
#     if (myNum > 0) and (myNum < 10):
#         print("my number is in range ")
#     else:
#         print("num is out of range" )
# threshold_num_input()

# # # Write a similar function called threshold_num_input_return that -returns- true or false boolean
# # # if the number is within range. Call the function and store the result of the function in a variable called next_flag. 
# def threshold_num_input_return():
#     myNum = int(input("What is the num?"))
#     if (myNum > 0) and (myNum < 10):
#         return True
#     else:
#         return False

# next_flag = threshold_num_input_return()

# # # Write a function called number_test that takes one parameter, a boolean.
# # # If the boolean is false,  print the message saying the program cannot proceed
# # # If the boolean is true, prompt the user to enter a number larger than 100. If the 
# # # user enters a number larger that is larger than or equal to 100, print whether the number
# # # is even or odd in a print(f'') string, and return the number.  Do not call the function.
# def number_test(myBool):
#     if not myBool:
#         print("can't proceed")
#     else: 
#         newNum = int(input("enter a number greater than 100"))
#         if newNum >= 100:
#             if newNum%2 == 0: 
#                 print("It is even") 
#             else: 
#                 print("It is odd")
#         else: 
#             print(f"{newNum} is number less than 100")

# # #  Call the function number_test with result of threshold_num_input_return which is stored 
# # # in the variable next_flag. 
# number_test(next_flag)

# # Write a function called type_error_test that raises a type error with an exception 
# def type_error_test():
#     try:
#         myTest = input("Enter a number, I will add it for you!")
#         print(myTest + 5)
#     except TypeError:
#         print("i'm a string and i forgot to convert an int :( ")
# type_error_test()

# # Write a function that raises a value error with an exception 
# def value_error_test():
#     try:
#         myTest = int(input("Enter a letter, but I'll pretend its a number"))
#     except ValueError:
#         print("I said enter a number!!!")

# value_error_test()

# # Outside a function, ask the user to enter a grade (out of 100). Store this
# # in a variable called my_grade. 
# # Create a function called auto_grader that takes one argument (the grade to be 
# # assessed)).
# # if marks for a class are as follows, make an auto grader that assess
# # the grade percentage numerically in a function and prints their 
# # grade as: "Your grade is {letter}"
# # 80 -100	A
# # 70-79 B
# # 60-69 C
# # 50-59 D
# # 0-49 F 
# # If the grade is A, ask the user how long they studied and slept the night 
# # before the test. Print the total sleep + study time. 
# # as "That is because they spent {total time} preparing! 
# # If the user slept less than 8 hours, print "But they should sleep more!"
# # If the user gets a A, B, C, or D, return true. If it is F, return false. 
# # If an invalid grade is entered and an error is raised, 
# # use a try/except to print "Enter a valid grade next time". 
# # Write a docstring for this function. 
# # Call the function and print the return value
# my_grade = int(input("What is my grade?"))
# def auto_grader_letter(grade):
#     """ auto grading students tests
#     Args:
#     grade: the grade entered by the student

#     Return:
#     True if the student passes
#     False fi the student fails
#     """
#     try:
#         if grade >=80: 
#             print("a")
#             sleep_hours = int(input("How many sleep hours?"))
#             study_hours = int(input("How many study hours?"))
#             print(f"it is because they spent {sleep_hours + study_hours} preparing!")
#             if sleep_hours < 8:
#                 print("but they should sleep more")
#             return True
#         elif grade >=70:
#             print("b")
#             return True
#         elif grade >= 60:
#             print("c")
#             return True
#         elif grade >= 50:
#             print("d")
#             return True
#         else:
#             print("fail")
#             return False
#     except TypeError:
#         print("enter a valid grade next time")
# print(auto_grader_letter(my_grade))


# # This runs first, its the top line in the program. 
# print("hello world!")
# #Function definitions are skipped until the function is called 
# def my_function():
#     return True
# print("here we go")
# my_function()
# print("we keep going!")

def last_species( triples, species):
    split = triples.split()
    if split[-1] == species:
        return True
    else:
        return False

triples = "Canidae, Canis, CanisLupus, Felidae, Felis, FelisCatus" 
print(last_species(triples, "FelisCatus"))  # True 
print(last_species(triples, "CanisLupus")) # False

def insert_at_index(triples, i, substring):
    output = triples[:i] + substring + triples[i:]
    print(output)
s = "Canidae, Canis, CanisLupus, Felidae, Felis, FelisCatus" 
new_string = insert_at_index(s, 28, "FELISCATUS, ") 
print(new_string) 
# Output: "Canidae, Canis, CanisLupus, FELISCATUS, Felidae, Felis, FelisCatus"

def numSpecies(triples, species):
    print(triples.count(species))
    if triples.count(species) == 1:
        where = triples.find(species) + len(species)
        newString = triples[:where] + (", " + species.upper())*3 + triples[where:]
        print(newString)
numSpecies(s, "FelisCatus")

def numGenus(string):
    number = len(string.split())/3 
    print(number)

numGenus(s)

sample_string = "This is my string. Can I add something to it?"
index = sample_string.find("string")
print(index)
insert_into_string = "PUT ME IN A STRING"
a_formatted_string = f'The first part of my string is \"{sample_string[:index]}\", followed by my insert \"{insert_into_string}\", and then the last part is \"{sample_string[index:]}\"'
print(a_formatted_string)



sample_string = "This is my string. Can I add something to it?"
string_to_find = "string"
index = sample_string.find(string_to_find)
length_of_word = len(string_to_find)
if len(sample_string) > index+length_of_word: 
    print("its not the last word")
else: 
    print("its the last word")



def a_function(string, num_threshold):
    '''
    determine if string appears more than threshold 
    :param stirng: the string to be analyzed 
    :param num_threshold: how many times the string can appear 
    :return : True if the string has test more than num_threshold times otherwise false 
    '''
    times = string.count("test")
    if times >= num_threshold:
        return True
    else:
        return False

