class Taxi:
    def __init__(self, taxi_id):
        self.id = taxi_id
        self.current_point = 'A'
        self.available_time = 0  # in hours
        self.total_earning = 0
        self.trips = []

    def __repr__(self):
        return f"Taxi{self.id} at {self.current_point}, Free at {self.available_time}hrs, Earnings: {self.total_earning}"
class Booking:
    def __init__(self, customer_id, pickup, drop, pickup_time, taxi_id, amount):
        self.customer_id = customer_id
        self.pickup = pickup
        self.drop = drop
        self.pickup_time = pickup_time
        self.taxi_id = taxi_id
        self.amount = amount
class TaxiManager:
    def __init__(self, num_taxis=4):
        self.taxis = [Taxi(i+1) for i in range(num_taxis)]
        self.points = ['A', 'B', 'C', 'D', 'E', 'F']

    def find_nearest_free_taxi(self, pickup_point, pickup_time):
        pickup_index = self.points.index(pickup_point)
        sorted_taxis = sorted(self.taxis, key=lambda x: (abs(self.points.index(x.current_point) - pickup_index), x.total_earning, x.id))

        for taxi in sorted_taxis:
            distance = abs(self.points.index(taxi.current_point) - pickup_index)
            time_to_reach = distance * 1  # 1 hr per 15 km
            if taxi.available_time <= pickup_time - time_to_reach:
                return taxi
        return None

    def calculate_fare(self, from_point, to_point):
        distance_km = abs(self.points.index(to_point) - self.points.index(from_point)) * 15
        if distance_km <= 5:
            return 100
        return 100 + (distance_km - 5) * 10

    def book_taxi(self, customer_id, pickup, drop, pickup_time):
        taxi = self.find_nearest_free_taxi(pickup, pickup_time)
        if not taxi:
            return f"No taxi available for Booking {customer_id}"

        fare = self.calculate_fare(pickup, drop)
        distance_points = abs(self.points.index(drop) - self.points.index(pickup))
        duration = distance_points * 1  # 1 hr per 15 km

        taxi.current_point = drop
        taxi.available_time = pickup_time + duration
        taxi.total_earning += fare
        booking = Booking(customer_id, pickup, drop, pickup_time, taxi.id, fare)
        taxi.trips.append(booking)

        return f"Booking {customer_id} --> Taxi{taxi.id} allocated. Fare: Rs.{fare}"
class BookingManager:
    def __init__(self, num_taxis=4):
        self.taxi_manager = TaxiManager(num_taxis)
        self.booking_id = 1

    def request_booking(self, pickup, drop, pickup_time):
        result = self.taxi_manager.book_taxi(self.booking_id, pickup, drop, pickup_time)
        print(result)
        self.booking_id += 1

    def show_taxi_details(self):
        for taxi in self.taxi_manager.taxis:
            print(taxi)
            for trip in taxi.trips:
                print(f"  Trip -> Customer {trip.customer_id}: {trip.pickup} to {trip.drop} at {trip.pickup_time}hrs, Rs.{trip.amount}")
            print()
if __name__ == "__main__":
    manager = BookingManager(num_taxis=4)

    manager.request_booking('A', 'B', 9)
    manager.request_booking('A', 'C', 9)
    manager.request_booking('A', 'D', 10)
    manager.request_booking('B', 'E', 11)
    manager.request_booking('C', 'F', 12)

    manager.show_taxi_details()
