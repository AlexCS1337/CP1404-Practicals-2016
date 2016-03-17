items = int(input("Enter how many items: "))
total = 0
while items < 0:
    print("Invalid number of items!")
    items = float(input("Enter how many items: "))
for i in range(0, items):
    shipping = float(input("Enter the shipping cost: $"))
    total += shipping
if total > 100:
    total *= 0.1
print("The total shipping cost is $", total)
