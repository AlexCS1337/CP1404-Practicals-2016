""" Personal Information
"""

# name = input("Your name: ")
# address = input("Your address(city, state and ZIP): ")
# telephone_number = int(input("Your telephone number: "))
# college_major = input("Your college major: ")
# print(name, address, telephone_number, college_major, sep="\n")


""" Sales Prediction
"""

# total_sales = float(input("Enter the total sales: "))
# profit = total_sales * 0.23
# print("The annual profit is $", profit)


""" Land Calculation
"""

total_square_feet = int(input("Enter the total square feet: "))
number_of_acres = total_square_feet // 43560
print(number_of_acres)

""" Total Purchase
"""

item_one = float(input("What is price of item one?: "))
item_two = float(input("What is price of item two?: "))
item_three = float(input("What is price of item three?: "))
item_four = float(input("What is price of item four?: "))
item_five = float(input("What is price of item five?: "))
subtotal = item_one + item_two + item_three + item_four +item_five
sales_tax = subtotal * .7
total = subtotal - sales_tax
print("subtotal: $", subtotal, " sales_tax $", sales_tax, " total: $", total, sep='')

""" Distance Traveled
"""

distance = 70 * 6
print(distance)
distance = 70 * 10
print(distance)
distance = 70 * 15
print(distance)