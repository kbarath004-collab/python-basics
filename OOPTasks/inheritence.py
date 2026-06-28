class Vehicle:
    def __init__(self):
        self.brand = input("Enter the brand name: ")
        self.model = input("Enter the model name: ")
        self.color = input("Enter the vehicle color: ")
        self.year = int(input("Enter the manufacturing year: "))

    def display(self):
        print("\n----- Vehicle Details -----")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Color :", self.color)
        print("Year  :", self.year)


class Car(Vehicle):
    def __init__(self):
        super().__init__()

        self.car_type = input("Is it a Sport Car or Family Car?: ").lower()

        if self.car_type == "sport car":
            self.top_speed = input("Enter the top speed: ")
        elif self.car_type == "family car":
            self.seats = int(input("Enter number of seats: "))
            self.doors = int(input("Enter number of doors: "))

    def display(self):
        super().display()

        print("\n----- Car Details -----")
        print("Car Type :", self.car_type)

        if self.car_type == "sport car":
            print("Top Speed :", self.top_speed)

        elif self.car_type == "family car":
            print("Seats :", self.seats)
            print("Doors :", self.doors)


class Bike(Vehicle):
    def __init__(self):
        super().__init__()

        self.bike_type = input(
            "Is it a Sport Bike or Normal Bike? "
        ).lower()

        if self.bike_type == "sport bike":
            self.top_speed = input("Enter the top speed: ")
        elif self.bike_type == "normal bike":
            self.mileage = input("Enter mileage (km/l): ")

    def display(self):
        super().display()

        print("\n----- Bike Details -----")
        print("Bike Type :", self.bike_type)

        if self.bike_type == "sport bike":
            print("Top Speed :", self.top_speed)

        elif self.bike_type == "normal bike":
            print("Mileage :", self.mileage)


print("1. Car")
print("2. Bike")

choice = input("Choose a vehicle: ")

if choice == "1":
    vehicle = Car()
    vehicle.display()

elif choice == "2":
    vehicle = Bike()
    vehicle.display()

else:
    print("Invalid choice.")