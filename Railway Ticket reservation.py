class Train:
    def __init__(self, train_no, name, source, destination, seats):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.total_seats = seats
        self.booked_passengers = {}

    def book_ticket(self, passenger_name):
        if len(self.booked_passengers) < self.total_seats:
            ticket_id = len(self.booked_passengers) + 1
            self.booked_passengers[ticket_id] = passenger_name
            print(f"Ticket booked! Ticket ID: {ticket_id}")
        else:
            print("No seats available.")

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.booked_passengers:
            name = self.booked_passengers.pop(ticket_id)
            print(f"Ticket {ticket_id} for {name} has been cancelled.")
        else:
            print("Invalid Ticket ID.")

    def available_seats(self):
        return self.total_seats - len(self.booked_passengers)

    def show_bookings(self):
        if not self.booked_passengers:
            print("No bookings yet.")
            return
        print("Booking Summary:")
        for tid, name in self.booked_passengers.items():
            print(f"Ticket ID: {tid} | Name: {name}")

    def __str__(self):
        return f"{self.train_no} - {self.name} ({self.source} to {self.destination}) | Available Seats: {self.available_seats()}"


class RailwaySystem:
    def __init__(self):
        self.trains = []

    def add_train(self):
        train_no = input("Train number: ")
        name = input("Train name: ")
        source = input("From: ")
        destination = input("To: ")
        seats = int(input("Total seats: "))
        train = Train(train_no, name, source, destination, seats)
        self.trains.append(train)
        print("Train added successfully.")

    def show_trains(self):
        if not self.trains:
            print("No trains available.")
            return
        for i, train in enumerate(self.trains):
            print(f"{i+1}. {train}")

    def book_ticket(self):
        self.show_trains()
        try:
            choice = int(input("Choose train number: ")) - 1
            if 0 <= choice < len(self.trains):
                name = input("Passenger name: ")
                self.trains[choice].book_ticket(name)
            else:
                print("Invalid train choice.")
        except ValueError:
            print("Invalid input.")

    def cancel_ticket(self):
        self.show_trains()
        try:
            choice = int(input("Choose train number: ")) - 1
            if 0 <= choice < len(self.trains):
                ticket_id = int(input("Enter Ticket ID to cancel: "))
                self.trains[choice].cancel_ticket(ticket_id)
            else:
                print("Invalid train choice.")
        except ValueError:
            print("Invalid input.")

    def show_bookings(self):
        self.show_trains()
        try:
            choice = int(input("Choose train number: ")) - 1
            if 0 <= choice < len(self.trains):
                self.trains[choice].show_bookings()
            else:
                print("Invalid train choice.")
        except ValueError:
            print("Invalid input.")

    def menu(self):
        while True:
            print("\n--- Railway Reservation System ---")
            print("1. Add Train")
            print("2. Show Trains")
            print("3. Book Ticket")
            print("4. Cancel Ticket")
            print("5. Show Bookings")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_train()
            elif choice == '2':
                self.show_trains()
            elif choice == '3':
                self.book_ticket()
            elif choice == '4':
                self.cancel_ticket()
            elif choice == '5':
                self.show_bookings()
            elif choice == '6':
                print("Exiting system.")
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    system = RailwaySystem()
    system.menu()
