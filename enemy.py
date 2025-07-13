# enemy.py

class Enemy:
    def __init__(self, name, type="minion"):
        self.name = name
        self.type = type
        self.health = 80 if type == "minion" else 150
        self.attack = 10 if type == "minion" else 20
        self.defense = 5 if type == "minion" else 12
        self.intro_text = self.set_intro()

    def set_intro(self):
        if self.type == "boss":
            return f"{self.name} looms in a haze of smoke and unpaid internships..."
        else:
            return f"{self.name} stumbles in, dripping grease and attitude."

    def is_alive(self):
        return self.health > 0
