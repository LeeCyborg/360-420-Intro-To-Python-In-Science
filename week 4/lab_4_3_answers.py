# Write a while loop that counts to 10 and prints the counter
i = 1
while i <= 10:
    print(i)
    i += 1

#Write a while loop that begins with "while true" and counts up by 1 every loop.
# It should print the number at every loop
# Make the loop end when the count reaches 10 with break
count = 0
while True:
    count = count+1
    print(count)
    if count >= 10:
        break

#write a while loop that asks the user for 2 numbers. Continue the loop
# until the user enters the same number twice

while True:
    num1 = int(input("num 1 please: "))
    num2 = int(input("num 2 please: "))
    if num1 == num2:
        print("you did it")
        break
    else:
        print("again")


#Write a for loop that prints each number in this list:
my_for_loop_list = [20, 40, 2, 5 ,29]

for item in my_for_loop_list:
    print(item)

# Write a Python program to display only those numbers from a list that satisfy the following conditions
#  - The number must be divisible by five
#  - If the number is greater than 150, then skip it and move to the following number
#  - If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

# Write a function called fruit_mixed that takes one parameter, a list of strings, 
# Write a loop that goes through every item in the list and if the
# item has more than 3 letters, convert every letter A to a B
# print every item as its been altered 

def fruit_mixed(list_to_turn):
    for item in list_to_turn:
        if len(item) > 1:
            item = item.replace("a", "b")
            print(item)
    
# Call the function with this string list
my_string_list = ["apple", "oranges", "bananas"]
fruit_mixed(my_string_list)