# Assignment 2, Graded Lab
# 
# Write all functions with docstrings and proper function and variable names
# You can talk and use notes but NO INTERNET (outside of Moodle) and do not
# copy each others' code
# if I see duplicate code it will result in 0 for both. 

# Question 1: 2 points 
# Question 2: 2 points
# Question 3: 3 points
# Question 4: 3 points 

# Question 1

# Write a function called packing_list that takes 
# two parameters: a list called items_to_pack and items_packed
# the function should return a list of items_not_packed. 
# In the function, loop through each item in items_to_pack 
# and determine if the item is in items_packed. if the item is not packed, 
# add it to a new list and return it. print "I'll have to pack my (item name)"
# If the item is packed, print "(item name) is packed, and it is at location (location)"
# where location is the index in the packed list. Call the function with the 
# two lists below. 
## Expected output should look like this: 
# shirt is packed and at location 0
# I'll have to pack my paper
# book is packed and at location 2
# I'll have to pack my phone
# I'll have to pack my toothbrush
# pants is packed and at location 5
# I'll have to pack my underwear
# I'll have to pack my socks
# I'll have to pack my towel
# ['paper', 'phone', 'toothbrush', 'underwear', 'socks', 'towel']

pack_list = ["shirt", "paper", "book", "phone", "toothbrush", "pants", "underwear", "socks", "towel"]
already_packed = ["shorts", "book", "pants", "shirt"]

def packing_list(items_to_pack, items_packed):
    to_pack = []
    for i, item in enumerate(items_to_pack):
        if item in items_packed:
            print(f"{item} is packed and at location {i}")
        else: 
            print(f"I'll have to pack my {item}")
            to_pack.append(item)
    return to_pack
print(packing_list(pack_list, already_packed))


# Question 2

# Write a function called list_scrambler. The function should take one parameter, 
# a list of integers called intlist. The function should return another list of integers. 
# Use a loop to check each number in the list. If the square root of that number
# is less than 3, remove it from its current location and insert it at the beginning
# of the list. 
# Call the function with numlist below and print the result. 
# Hints: 
# list.copy() will return a copy of a list 
# You should create a new list, rather than modify the list you are looping through
# Your returned list should look like this: [1, 7, 5, 2, 2, 40, 10, 50]

import math
numlist = [2,40,2,5,7,10,1,50]
def list_scrambler(intlist):
    newlist = intlist.copy()
    for i, num in enumerate(intlist): 
        if math.sqrt(num) < 3:
            newlist.pop(i)
            newlist.insert(0, num)
    return newlist
print(list_scrambler(numlist))

# Question 3
# The functions ord() and chr() are used to encode and decode unicode characters. 
# ord() takes a string with a single character and returns an integer corresponding to it
# chr() takes an integer, and returns a character corresponding to it. 
# Try these lines of code below to see how it works. 
# print(ord("a"))
# print(chr(97))
# Every character has a number code associated with it, even chars not on your keyboard. 
# Write a function called magic_function that takes a list of characters called mychars
# The function should get the integer value of each character in the list using ord()
# and find the average (the average is numbers added together, divided by the number of items)
# Convert the average to an integer, and then return the character associated with that number using (chr)()
# Call the function with charlist below Print the result. It should be a single character "I". 

charlist = ["a", "C", "{", "!", "0"]
def magic_function(decode):
    total = 0
    for item in decode: 
        total = total + ord(item)
    avg = int(total/len(decode))
    return(chr(avg))
print(magic_function(charlist))

# Question 4

# Write an encoder that translates a message into an encoded string. 
# Create a function called encoder that takes two parameters, a string to encode, and an offset. 
# The function should return an encoded string.
# The function should encode your string by replacing each letter with a letter offset by the offset number
# Ex: a is 0, b is 1, c is 2. 
# If I offset a by 1, a becomes b. 
# Replace all spaces with an "!". 
# If there is a symbol or number that is not in the letters list, replace it with an "&".
# You must use a loop. 

#Remember, if a letter is at the end of the alphabet, you'll have to wrap around to tbe beginning fo the list. 
# Hints:
# - You can loop through a string like you can loop through a list. Ex: 
# for ch in string, ch will be each individual character in the string as you loop. 
# - % gives you the remainder of division. 10%10 is 0, 15%10 is 5, 5%10 is 5. 
# list.index gives you the location of the letter you pass through it
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encoder(phrase, offset):
    message = ""
    phrase = phrase.lower()
    for ch in phrase: 
        if ch == " ":
            message = message+"!"
        elif ch not in letters: 
            message = message+"&"
        else: 
            index = letters.index(ch)+offset 
            index = index%(len(letters))
            message = "" +message+str(letters[index])
    return(message)

# I will test your function with:
print(encoder("wax and,haze!", 0)) 
# should print wax!and&haze&
print(encoder("wax and,haze!", 10)) 
# Should print gkh!kxn&rkjo&
print(encoder("out+about zap", 52))
# Should print out&about!zap
print(encoder("out+about zap", 12))
# should print agf&mnagf!lmb

