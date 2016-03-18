# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denomiator: "))
#     fraction = numerator / denominator
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished")

finished = False
result = 0
while not finished:
    try:
        result = int(input("What is your result?: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("valid result is", result)