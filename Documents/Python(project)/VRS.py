from datetime import datetime, timedelta


class Vehicle:
    def __init__(self, vehicle_id, brand, model, price_per_hour):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price_per_hour = price_per_hour
        self.is_available = True
        self.rented_by = None
        self.rented_until = None

    def show_details(self):
        status = "Available" if self.is_available else f"Rented by {self.rented_by} until {self.rented_until}"
        return f"{self.vehicle_id} | {self.brand} {self.model} | ₹{self.price_per_hour}/hr | {status}"



class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, price_per_hour):
        super().__init__(vehicle_id, brand, model, price_per_hour)
        self.type = "Car"


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, price_per_hour):
        super().__init__(vehicle_id, brand, model, price_per_hour)
        self.type = "Bike"



class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.load_sample_data()

    def load_sample_data(self):
        self.vehicles = [
            Car("C001", "Hyundai", "i10", 50),
            Car("C002", "Maruti", "Swift", 70),
            Bike("B001", "Honda", "CB Shine", 20),
            Bike("B002", "TVS", "Apache", 30),
        ]

    def list_vehicles(self, only_available=False):
        for v in self.vehicles:
            if only_available and v.is_available is False:
                continue
            print(v.show_details())

    def find_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def rent_vehicle(self, vehicle_id, customer_name, hours):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if not vehicle.is_available:
            print("Vehicle is already rented.")
            return

        end_time = datetime.now() + timedelta(hours=hours)
        vehicle.is_available = False
        vehicle.rented_by = customer_name
        vehicle.rented_until = end_time.strftime("%Y-%m-%d %H:%M")

        cost = hours * vehicle.price_per_hour

        print(f"\nVehicle Rented Successfully!")
        print(f"Customer: {customer_name}")
        print(f"Total Cost: ₹{cost}")
        print(f"Return Before: {vehicle.rented_until}")

    def return_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle.is_available:
            print("This vehicle is already available.")
            return

        vehicle.is_available = True
        vehicle.rented_by = None
        vehicle.rented_until = None

        print(f"Vehicle {vehicle_id} has been returned successfully!")

    def add_vehicle(self, v):
        self.vehicles.append(v)
        print("Vehicle added successfully!")

    def remove_vehicle(self, vehicle_id):
        v = self.find_vehicle(vehicle_id)
        if v:
            self.vehicles.remove(v)
            print("Vehicle removed!")
        else:
            print("Vehicle ID not found.")


def show_menu():
    print("\n    Vehicle Rental System     ")
    print("1. Show all vehicles")
    print("2. Show available vehicles")
    print("3. Rent a vehicle")
    print("4. Return a vehicle")
    print("5. Add vehicle (admin)")
    print("6. Remove vehicle (admin)")
    print("7. Exit")


def main():
    system = RentalSystem()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            system.list_vehicles()

        elif choice == "2":
            system.list_vehicles(only_available=True)

        elif choice == "3":
            vid = input("Enter Vehicle ID: ")
            name = input("Enter your name: ")
            hours = int(input("Hours to rent: "))
            system.rent_vehicle(vid, name, hours)

        elif choice == "4":
            vid = input("Enter Vehicle ID: ")
            system.return_vehicle(vid)

        elif choice == "5":
            vid = input("Vehicle ID: ")
            brand = input("Brand: ")
            model = input("Model: ")
            price = int(input("Price per hour: "))
            type_choice = input("Type (car/bike): ").lower()

            if type_choice == "car":
                system.add_vehicle(Car(vid, brand, model, price))
            else:
                system.add_vehicle(Bike(vid, brand, model, price))

        elif choice == "6":
            vid = input("Enter Vehicle ID: ")
            system.remove_vehicle(vid)

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == "__main__":
    main()
