""" Created by Alex Silva 2 June 2016
"""

#Required constants
MENU = "(D)etermine Grade\n(C)alculate GPA\n(Q)uit"

def main():
    # This is the main menu
    name = input("Enter your name: ")
    print("Hello", name, "Choose: ")
    print(MENU)
    choice = input('>>>').upper()
    while choice != "Q":
        if choice == "D":
            determine_grade()
        elif choice == "C":
            print("Your GPA is ...")
        else:
            print("Invalid option")

        print(MENU)
        choice = input('>>>')


def determine_grade():
    try:
        choice = int(input("What is your total score?"))
        if choice >= 85:
            print("Your grade is: HD")
        elif choice > 75 and choice < 84:
            print("Your grade is: D")
        elif choice > 65 and choice < 74:
            print("Your grade is: C")
        elif choice > 50 and choice < 64:
            print("Your grade is P")
        else:
            print("Your grade is N")
    except ValueError:
        print("That is not a number.")


main()