from room import Room
from user import User
from booking import Booking
from manager import Manager

manager = Manager()

# Add rooms
manager.add_room(Room(101, "Single"))
manager.add_room(Room(102, "Double"))

# User
user = User(1, "Ahmed")

while True:
    print("\n=== Booking System Menu ===")
    print("1. View Rooms")
    print("2. Book a Room")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        manager.view_rooms()

    elif choice == "2":
        room_number = int(input("Enter room number: "))
        selected_room = None

        for room in manager.rooms:
            if room.room_number == room_number:
                selected_room = room
                break

        if selected_room and selected_room.book():
            booking = Booking(user, selected_room)
            manager.add_booking(booking)
            print("Room booked successfully!")
        else:
            print("Room not found or already booked.")

    elif choice == "3":
        manager.view_bookings()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
