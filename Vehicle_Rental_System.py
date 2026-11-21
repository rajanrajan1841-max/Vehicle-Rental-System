class Vehicle:
    def __init__(self, vehicle_id, name, vehicle_type, rent_per_day):
        self.vehicle_id = vehicle_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day
        self.available = True


class Rental:
    def __init__(self):
        self.rented_vehicles = {}

    def calculate_rent(self, vehicle, days):
        return vehicle.rent_per_day * days

    def rent_vehicle(self, vehicle, days):
        if vehicle.available:
            vehicle.available = False
            self.rented_vehicles[vehicle.vehicle_id] = (vehicle, days)
            cost = self.calculate_rent(vehicle, days)
            print("\nVehicle rented successfully!")
            print("Vehicle:", vehicle.name)
            print("Rental Days:", days)
            print("Total Rent: Rs.", cost)
        else:
            print("Vehicle is not available!")

    def return_vehicle(self, vehicle_id):
        if vehicle_id in self.rented_vehicles:
            vehicle, days = self.rented_vehicles.pop(vehicle_id)
            vehicle.available = True
            print("\nVehicle returned successfully!")
            print("Vehicle:", vehicle.name)
            print("Total Rent: Rs.", self.calculate_rent(vehicle, days))
        else:
            print("Invalid Vehicle ID!")


vehicles = [
    Vehicle(1, "Maruti Swift", "Car", 1500),
    Vehicle(2, "Hyundai Creta", "Car", 2500),
    Vehicle(3, "Royal Enfield", "Bike", 800),
    Vehicle(4, "Honda Activa", "Bike", 400)
]

rental = Rental()

while True:
    print("\n===== VEHICLE RENTAL SYSTEM =====")
    print("1. Show Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a Vehicle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Vehicles:")
        for v in vehicles:
            if v.available:
                print(v.vehicle_id, v.name, v.vehicle_type,
                      "Rent/Day: Rs.", v.rent_per_day)

    elif choice == "2":
        vehicle_id = int(input("Enter Vehicle ID: "))
        days = int(input("Enter rental days: "))
        vehicle = next(
            (v for v in vehicles if v.vehicle_id == vehicle_id), None
        )
        if vehicle and days > 0:
            rental.rent_vehicle(vehicle, days)
        else:
            print("Invalid Vehicle ID or rental days!")

    elif choice == "3":
        vehicle_id = int(input("Enter Vehicle ID to return: "))
        rental.return_vehicle(vehicle_id)

    elif choice == "4":
        print("Thank you for using Vehicle Rental System!")
        break

    else:
        print("Invalid choice! Please try again.")
