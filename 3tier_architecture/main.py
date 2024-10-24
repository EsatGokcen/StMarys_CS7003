import presentation_layer as pl
from business_logic_layer import BookingSystem
from database_layer import DataStore

def main():
    data_store = DataStore()
    booking_system = BookingSystem(data_store)

    while True:
        pl.display_menu()
        choice = pl.get_user_choice()

        if choice == '1':
            name, room_type = pl.get_booking_details()
            booking_system.book_room(name, room_type)
            print("Room booked successfully!")
        elif choice == '2':
            bookings = booking_system.get_all_bookings()
            pl.display_bookings(bookings)
        elif choice == '3':
            print("Exiting the sustem. Goodbye!")
            break
        else:
            print("Invalid choice, please try again...")

if __name__ == '__main__':
    main()
