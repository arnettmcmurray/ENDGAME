# player.py

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100
        self.inventory = []

        if role == "Griddle Knight":
            self.attack = 15
            self.defense = 10
            self.special = "Grease Slam"
        elif role == "Fry Cook Mage":
            self.attack = 12
            self.defense = 8
            self.special = "Oil Burst"
        elif role == "Janitor Rogue":
            self.attack = 10
            self.defense = 12
            self.special = "Mop Ambush"
        else:
            self.attack = 8
            self.defense = 8
            self.special = "Slap of Shame"

    def info(self):
        return f"{self.name} the {self.role} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | Special: {self.special}"

    def is_alive(self):
        return self.health > 0
