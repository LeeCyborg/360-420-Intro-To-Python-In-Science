# Write a function called find_animal that contains a var with the list below. 
# The function should take 1 parameter, a string that should be the name of an animal
# If the name is on the list, print "we hav that animal", f the name is not on th elist
# print "no such luck"
# 
#  my_list = "dog, cat, pig, bird, snail, duck, fish, goose"


# Write a function called keyword_finder that takes two parameters, a phrase and a keyword
# If the keyword appears in the phrase, determine how many times it appears 
# in the phrase and the index of when it first appears. Print
# f"{Keyword} is in the phrase, it appears {times} times , first at index {index}
# If the word does not appear in the phrase, display how many characters are in 
# both the phrase and the keyword in a f'' string 
#Make sure this works regardless of the UPPER CASE or lower case letters
# Do not call the function. 




# Now call the function with the keyword "TEST" and the phrase "This is a test"


# Your output should be: 
# test is in the phrase, it appears 1, first at 10

#Now call the function again but with user input as parameters 


# Write a function called fun_phrase that takes two strings, one is a phrase and the other is a exclamation. 
# Return a string that replaces all spaces in the phrase with the exclamation in all capital letters. 
# If there are no spaces, print ("no fun :()")
# hint .replace() takes two parameters, the phrase you're looking for and one one to replace it with


# Print the result of the function with the phrase "This is my phrase" and the exclamation "pizza"


#Your result should be ThisPIZZAisPIZZAmyPIZZAphrase

#Call it again with user input and print the answer

# Write a snippet of code that adds "ADD THIS STRING" into after the word "tasks"
# in the string "String tasks can be annoying, but its important to learn"
# use find() and string indexes 


# Write a function called easter_date that takes 1 parameter, the year deisred. 
# Implement the calculator for the date of Easter.
# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.🔗
# Ask the user to enter a year. Compute the following:
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateofeaster = 22 + d + e
# 
# Special note: The algorithm can give a date in April. Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.🔗
# Your program should print an error message if the user provides a date that is out of range.
# If the user enters something that isn't a number raise an error an exception 
