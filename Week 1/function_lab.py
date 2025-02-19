def my_function_param(my_string):
    print(my_string)

my_function_param("this is a string")
my_function_param("I can print anything here")
my_function_param("This function is so useful!")

def calculate_square_area(width, height):
    area = width * height
    print(f'The area of a square with the width of {width} inches ad the height of {height} inches is {area} inches^2')

def return_calculate_square_area(width, height):
    area = width * height
    return(area)
print(return_calculate_square_area(2,4))

# NameError: name 'area' is not defined