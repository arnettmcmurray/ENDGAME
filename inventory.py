# inventory.py

class Item:
    def __init__(self, name, effect_type, power):
        self.name = name
        self.effect_type = effect_type  # 'heal' or 'damage' or 'boost'
        self.power = power

    def use(self, target):
        if self.effect_type == "heal":
            target.health += self.power
            print(f"{target.name} heals {self.power} HP with {self.name}.")
        elif self.effect_type == "damage":
            target.health -= self.power
            print(f"{target.name} takes {self.power} damage from {self.name}.")
        elif self.effect_type == "boost":
            target.attack += self.power
            print(f"{target.name}'s attack increases by {self.power} with {self.name}.")

def list_inventory(player):
    if not player.inventory:
        print("Your pockets are empty.")
        return
    print("Inventory:")
    for idx, item in enumerate(player.inventory, 1):
        print(f"{idx}. {item.name} ({item.effect_type}, {item.power})")

def use_inventory_item(player, enemy=None):
    list_inventory(player)
    choice = input("Pick item number to use (or press Enter to cancel): ")
    if not choice.strip():
        print("No item used.")
        return
    try:
        idx = int(choice) - 1
        item = player.inventory.pop(idx)
        if item.effect_type == "damage" and enemy:
            item.use(enemy)
        else:
            item.use(player)
    except (IndexError, ValueError):
        print("Invalid choice.")
