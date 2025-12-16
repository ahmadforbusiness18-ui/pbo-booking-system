class Booking:
    def __init__(self, user, room):
        self.user = user
        self.room = room

    def confirm_booking(self):
        if self.room.is_available:
            self.room.book_room()
            return f"Booking confirmed for {self.user.name} in room {self.room.room_number}"
        else:
            return "Room is not available"
