class Manager:
    def __init__(self):
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def view_rooms(self):
        print("\nAvailable Rooms:")
        for room in self.rooms:
            status = "Available" if room.is_available else "Booked"
            print(f"Room {room.room_number} - {room.room_type} - {status}")

    def add_booking(self, booking):
        self.bookings.append(booking)

    def view_bookings(self):
        print("\nBookings:")
        for booking in self.bookings:
            print(booking)
