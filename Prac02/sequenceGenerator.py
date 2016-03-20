x = int(input("Type a starting number"))
y = int(input("Type an ending number"))
print("1. Show the even numbers from", x, "to", y)
print("2. Show the odd numbers from", x, "to", y)
print("3. Show the squares from", x, "to", y)
print("4. Exit the program")
choice = input(">>>")
while choice != "4":
    if choice == "1":
        for i in range(x, y, 2):
            print(i, end=' ')
    elif choice == "2":
        break
    elif choice == "3":
        break
    print("1. Show the even numbers from", x, "to", y)
    print("2. Show the odd numbers from", x, "to", y)
    print("3. Show the squares from", x, "to", y)
    print("4. Exit the program")
    choice = input(">>>")
print("Finished")