""" Car Driving Simulator written by Alex 2016
This Car Driving Simulator is yet to be finished..

"""

from car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"

def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")

    print(MENU)
    menu_choice = input("Enter your choice: ").lower()
    while menu_choice != "q":
        if menu_choice == "d":
            print(MENU)
        elif menu_choice == "r":
            print(MENU)
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()