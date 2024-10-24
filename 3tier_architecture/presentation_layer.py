def display_menu():
    print("Welcome to the Hotel Booking System")
    print("1. Book a Room")
    print("2. View Bookings")
    print("3. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def get_booking_details():
    name = input("Enter your name: ")
    room_type = input("Enter room type: (Single/Double)")
    return name, room_type

def display_bookings(bookings):
    if not bookings:
        print("No bookings found.")
    else:
        for booking in bookings:
            print(f"Name: {booking['name']}, Room Type: {booking['room type']}")


