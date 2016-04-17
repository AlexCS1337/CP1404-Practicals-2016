from car import Car

def main():
    bus = Car(180)
    bus.drive(30)
    print("bus fuel =", bus.fuel)
    print("bus odo =", bus.odometer)
    print(bus)
    limbo = Car(100)
    limbo.fuel += 20
    print("limbo fuel =", limbo.fuel)
    limbo.drive(115)
    print("limbo obo =", limbo.odometer)


main()