class Room:


    def __init__(self, description):
        self.description = description
        self.characters = []

    def things_in_room(self):
        print(self.description)
        for character in self.characters:
            print(character.name + " is in the room")

    def add_character(self, character):
        self.characters.append(character)
