#You will have 1 hour to complete this assignment. You may use notes and moodle 
#but NOT the broader internet (no google, no chat gpt, etc)
# Please note: 
# All functions should have docstrings 
# All variables should be named clearly following proper naming rules
# Partial marks will be given so at least attempt each function 
# Pay attention to formatting, syntax, read the errors clearly. 
# and take your time! 

# Total: 10 points
# Question 1: 3 points
# Question 2: 3 points
# Question 3: 4 points

#Question 1: Vowel or Owl

# Write a function called vowel_or_owl that counts characters in a string
# up to a given threshold. The function should take two parameters: A phrase to
# evaluate and a threshold. 

# Your function should count the number of times each vowel appears in the phrase
# ( Vowels are A, E, I, O and U) and store that number each in a variable inside the function. 

# Convert the phrase to all upper case. 

# For each vowel, if there are more than "threshold" number of that vowel in the phrase, 
# print the phrase " This vowel {vowel} is an owl") ex: This vowel A is an owl

# Only count the vowels if there is a Y in the phrase. If there is no "Y", don't do 
# anything. 

# Hint: .count() can count the number of times a set of characters appears in a string
# Hint: .upper() returns an upper case version of the string
# Hint: Take it one step at a time. Do each step slowly. 


# Check your answer: 
# If you call the function with the parameters "This is a phrase, how will it look?" and 2
# Your function should print:
# This vowel I is an owl
# This vowel O is an owl

# If you call it with "yay, check it ouuuttt" and 1, it should print nothing. 


#Question 2
# Create a function called richter_scale that takes one parameter prints
# the description of an earthquake. 

# The following table contains earthquake magnitude 
# ranges on the Richter scale and their descriptors:  
# 2.5 or less	Usually not felt
# 2.5 to 5.4	Often felt, but only causes minor damage.
# 5.5 to 6.0	Slight damage to buildings and other structures.
# 6.1 to 6.9	May cause a lot of damage 
# 7.0 to 7.9	Major earthquake.
# 8.0 or greater	Great earthquake.

# For example, if function is passed 5.5 then your program should 
# indicate that a magnitude 5.5 earthquake is considered to 
# may cause slight damage to buildings. 
# Do not call the function. 


# Now create a variable called my_quake that holds input from a user prompt 
# "How big of a quake?" Use that variable to call the ricter_scale function
# Hint: make sure the user input is the proper data type


# If I enter 2.2, my program should say "Usually not felt"

#Question 3: check digit
# Write a function to check a number called number_checker that accepts 1 parameter called num, 
# which is a string made up of 4 numbers. 
# The program will print an f string described below and return a 5 digit integer
# Do not call the function. 

# We are going to write a program to generate what is called a check digit.
# Companies use check digits to ensure that customer numbers are valid. Algorithms for creating customer 
# numbers that contain a check digit vary widely.  

# For example, given the 5-digit customer number: 11855  

# The check digit is the final digit in the sequence (i.e., 5). That is what we are making.
# The check digit is determined as the remainder of dividing the 
# sum of the individual digits of a four-digit number by 10, i.e.: 1+1+8+5 = 15. 
# Divide 15 by 10, and the remainder is 5. Therefore 5 is the check digit.  

# Create a Python program that:  
# asks the user for a 4-digit number  
# calculates the check digit as described above (adding all the digits together and dividing by 10 
# to get the final digit)
# Print the final digit number in an f string that says 
# "Your check digit is {check digit} and your final number is {5 digit number}"
#  and then return the 5-digit customer number as an integer.  
# If the user enters a number that is greater than or less than 4 digits 
# display the message "please enter a 4 digit number"
# Use a try / except if the user enters something that isn't a number

#Hint: modulus % is the remainder of division. Ex: 10%2 is 0. 10%3 is 1. 
#Hint: you can get a character in a string by using [] to find the index
#hint: len() can return the length of a string
# Hint: dont forget to make the data types correct. 


#Check your work: 
# Calling the function with "1185" should print "Your check digit is 
# 5 and your final number is 11855" and return "11855"

