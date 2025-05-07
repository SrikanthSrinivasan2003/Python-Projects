class Flight:
    def __init__(self, flight_no, origin, destination, seats):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.passengers = []

    def book_seat(self, name):
        if len(self.passengers) < self.seats:
            self.passengers.append(name)
            print(f"Booking successful for {name}.")
        else:
            print("No available seats.")

    def cancel_booking(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            print(f"Booking cancelled for {name}.")
        else:
            print("Passenger not found.")

    def show_passengers(self):
        if not self.passengers:
            print("No passengers yet.")
        else:
            print("Passenger List:")
            for p in self.passengers:
                print("-", p)

    def __str__(self):
        return f"{self.flight_no}: {self.origin} -> {self.destination} | Seats: {self.seats - len(self.passengers)} available"


class FlightSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self):
        flight_no = input("Enter flight number: ")
        origin = input("From: ")
        destination = input("To: ")
        seats = int(input("Total seats: "))
        self.flights.append(Flight(flight_no, origin, destination, seats))
        print("Flight added.")

    def show_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            for i, flight in enumerate(self.flights):
                print(f"{i+1}. {flight}")

    def book_ticket(self):
        self.show_flights()
        choice = int(input("Choose flight number: ")) - 1
        if 0 <= choice < len(self.flights):
            name = input("Enter your name: ")
            self.flights[choice].book_seat(name)
        else:
            print("Invalid choice.")

    def cancel_ticket(self):
        self.show_flights()
        choice = int(input("Choose flight number: ")) - 1
        if 0 <= choice < len(self.flights):
            name = input("Enter your name to cancel booking: ")
            self.flights[choice].cancel_booking(name)
        else:
            print("Invalid choice.")

    def show_passenger_list(self):
        self.show_flights()
        choice = int(input("Choose flight number: ")) - 1
        if 0 <= choice < len(self.flights):
            self.flights[choice].show_passengers()
        else:
            print("Invalid choice.")

    def menu(self):
        while True:
            print("\n--- Flight Booking System ---")
            print("1. Add Flight")
            print("2. Show Flights")
            print("3. Book Ticket")
            print("4. Cancel Ticket")
            print("5. Show Passengers")
            print("6. Exit")
            choice = input("Choose option: ")

            if choice == '1':
                self.add_flight()
            elif choice == '2':
                self.show_flights()
            elif choice == '3':
                self.book_ticket()
            elif choice == '4':
                self.cancel_ticket()
            elif choice == '5':
                self.show_passenger_list()
            elif choice == '6':
                print("Exiting system.")
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    system = FlightSystem()
    system.menu()
