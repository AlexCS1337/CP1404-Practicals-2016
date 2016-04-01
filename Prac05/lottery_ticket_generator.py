import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

choice = int(input("How many quick picks? "))
while choice < 0:
    print("That makes no sense!")
    choice = int(input("How many quick picks? "))

for i in range(choice):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
        print(format(number, "2d"), end =" ")
    print()