lower = 10
upper = 100
print("Enter a number ({0}-{1}):".format(lower, upper))

def get_number(lower, upper):
    number = (input("Enter a number (10-50): "))
    while number.isdecimal() != True:
        print("Enter a valid number!")
        number = (input("Enter a number (10-50): "))

get_number(10, 50)