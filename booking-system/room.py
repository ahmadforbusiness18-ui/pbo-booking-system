class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True

    def book_room(self):
        self.is_available = False

    def free_room(self):
        self.is_available = True
