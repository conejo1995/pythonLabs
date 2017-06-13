class Character:
    def __init__(self, name = 'Player', attack = 5, health = 10):
        self.name = name
        self.talk = 'Hey there.'
        self.attack = attack
        self. health = health
        # self.inventory = Inventory()

    def take_damage(self, damage):
        self.health = self.health - damage

    def speak(self):
        print(self.name + ": " + self.talk)
