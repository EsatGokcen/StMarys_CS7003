class DataStore:

    def __init__(self):
        self.bookings = []

    def save_booking(self, booking):
        self.bookings.append(booking)

    def load_bookings(self):
        return self.bookings