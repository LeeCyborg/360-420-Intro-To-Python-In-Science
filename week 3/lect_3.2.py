# my_boolean = True; 

# print(my_boolean)

# if my_boolean: my_boolean = False

# print(my_boolean)

# myNum = int(input("Enter a number: "))
# myNum2 = int(input("Enter another number: "))

# my_boolean = myNum > myNum2

# print(my_boolean)

# def animal_limits():
#     number_of_birds = 10
#     number_of_cats = 30
#     number_of_hamsters = 20
#     animal_threshold = 15
#     if number_of_birds > animal_threshold:
#         print("you have too many birds")
#     if number_of_cats > animal_threshold:
#         print("you have too many cats")
#     if number_of_hamsters > animal_threshold:
#         print("you have too many hamsters")
# animal_limits()
import math 
def making_errors():
    try:
        myVar = math.sqrt(-4)
        # geek = "Geeks"
        # num = 4
        # print(geek + num + geek)
    except ValueError:
        print("gotta be the right data type")

making_errors()



def student_cookies():
    try:
        num_students = int(input("How many students?"))
        num_cookies = int(input("how many cookies?"))
        students_are_good = input("Are the students good? y/n")
        if num_cookies >= num_students: 
            print("there is enough cookies")
            if "y" in students_are_good.lower():
                print("and they are good, so they get cookies")
            else:
                print("but the students aren\'t good, so no cookies!")
        else: 
            print("there are not enough cookies :(")
    except ValueError:
        print("gotta be the right data type")

student_cookies()


# number_of_students = 35
# number_of_cookies = 50
# students_are_good = true;
# if number_of_students > number_of_cookies: 



# my_bool = False
# my_int = 4
# if my_int > 2 and my_bool == True :
#     print("Both ARE true")
# else:
#     print("Both are NOT")

# if my_int > 2 or my_bool == True :
#     print("only one has to be true for this to happen")
# else:
#     print("Neither are true")