class Vehicle:
    def __init__(self, vehicle_no, vehicle_type):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.toll_amount = self.calculate_toll()

    def calculate_toll(self):
        rates = {
            "car": 50,
            "truck": 100,
            "bus": 80,
            "bike": 20
        }
        return rates.get(self.vehicle_type.lower(), 0)


class TollBooth:
    def __init__(self):
        self.records = []

    def process_vehicle(self):
        vehicle_no = input("Enter vehicle number: ")
        vehicle_type = input("Enter vehicle type (car/truck/bus/bike): ").lower()
        vehicle = Vehicle(vehicle_no, vehicle_type)

        if vehicle.toll_amount == 0:
            print("Invalid vehicle type.")
            return

        print(f"Toll for {vehicle.vehicle_type.title()}: ₹{vehicle.toll_amount}")
        pay = input(f"Pay ₹{vehicle.toll_amount}? (yes/no): ").lower()

        if pay == 'yes':
            self.records.append(vehicle)
            print("Payment successful. Receipt generated.")
        else:
            print("Payment cancelled.")

    def show_records(self):
        if not self.records:
            print("No toll payments recorded.")
            return

        print("\n--- Toll Payment Records ---")
        for v in self.records:
            print(f"{v.vehicle_no} - {v.vehicle_type.title()} - ₹{v.toll_amount}")
        print(f"Total Collection: ₹{self.total_collection()}")

    def total_collection(self):
        return sum(v.toll_amount for v in self.records)

    def menu(self):
        while True:
            print("\n--- Toll Booth System ---")
            print("1. Process Vehicle")
            print("2. View Records")
            print("3. Exit")
            choice = input("Choose option: ")

            if choice == '1':
                self.process_vehicle()
            elif choice == '2':
                self.show_records()
            elif choice == '3':
                print("Exiting system.")
                break
            else:
                print("Invalid option.")
                

if __name__ == "__main__":
    booth = TollBooth()
    booth.menu()
