""" Loop 1
"""
MENU = "Please choose an options.\n(G)et name\n(U)ppercase\n(L)owercase\n(Q)uit"

name = input("What is your name?")
print(MENU)
choice = input(">>>")
while choice != 'Q':
    if choice == 'G':
        name = input("What is your new name?")
    elif choice == 'U':
        print(name.upper())
    elif choice == 'L':
        print(name.lower())
    else:
        print("Invalid choice.")

    print(MENU)
    choice == input(">>>")

""" Loop 2
    """
lower = int(input("What is the lower number?"))
higher = int(input("What is the higher number?"))
for i in range(lower, higher):
    print('test')