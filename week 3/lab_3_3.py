my_var = 5
# What is the data type of my var?  Print it with type()
print(type(my_var))

my_num = "3"
# Convert my_num to an integer 
my_num = int(my_num)

# print the type of my_num
print(type(my_num))

# Ask the user for input, store it in a variable called num_cookies 
num_cookies = input("How many cookies?")
 
 # Print the type of num_cookies
print(type(num_cookies))

# Convert num_cookies to an int
num_cookies = int(num_cookies)

#print the type of num cookies again 
print(type(num_cookies))

#print num_cookies * 2
print(num_cookies*2)

# Write an if statement. If num_cookies is greater than or equal to 4, print "You have enough cookies"
# Otherwise, print "you need more cookies"
if num_cookies>=4:
    print("you have enough cookies")
else:
    print("You need more cookies")

#Write another if / else statement. If you have an even number of cookies that is
# even, print "your cookies can be paired!" if you have an odd number of cookies
# print "cookies cant be paired"
if num_cookies % 2 == 0:
    print("cookies can be paired")
else: 
    print("Cookies can't be paired")

# Write a function called cookie_calc that asks the user for a the number of cookies they have, 
# and the number of cookies they need. If the number of cookies they have
# is less than the number of cookies they need, tell them how many more they
# need to bake (ex: number of cookies needed - number they have )
# Do. not call the function. 

def cookie_calc():
    cookies_owned = int(input("How many cookies do you have?"))
    cookies_needed = int(input ("How many do you need?"))
    if cookies_owned > cookies_needed:
        print("you have enough cookies")
    else:
        to_be_baked = cookies_needed - cookies_owned
        print(f"you need to make {to_be_baked} cookies")

# Now call the function 
cookie_calc()