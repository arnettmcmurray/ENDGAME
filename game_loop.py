from player import Player
from enemy import Enemy
from combat import fight
from inventory import Item
from abilities import use_special
from wu_battle import wu_battle_intro
from end_scene import end_scene

def show_intro():
    print(r"""
     ___  ___  __    __  _______  _________  ________     
    |\  \|\  \|\ \  |\  \|\  ___ \|\___   ___\\   __  \    
    \ \  \\\  \ \ \  \ \  \ \   __/\|___ \  \_\ \  \|\  \   
     \ \   __  \ \ \  \ \  \ \  \_|/__  \ \  \ \ \   _  _\  
      \ \  \ \  \ \ \  \ \  \ \  \_|\ \  \ \  \ \ \  \\  \| 
       \ \__\ \__\ \ \__\ \__\ \_______\  \ \__\ \ \__\\ _\ 
        \|__|\|__|  \|__|\|__|\|_______|   \|__|  \|__|\|__|

        Burgertown RPG: Where the grease is eternal
    """)
    input("\nPress Enter to serve justice...\n")

def start_game():
    show_intro()

    print("Welcome to Burgertown.")
    name = input("Name your fighter: ")

    print("\nChoose your class:")
    print("1. Griddle Knight")
    print("2. Fry Cook Mage")
    print("3. Janitor Rogue")
    role_input = input("Pick 1, 2, or 3: ")

    roles = {
        "1": "Griddle Knight",
        "2": "Fry Cook Mage",
        "3": "Janitor Rogue"
    }

    role = roles.get(role_input, "Dishwasher Peasant")

    player = Player(name, role)
    print(f"\nYou chose: {player.role}")
    print(player.info())

    burger = Item("Burger", "heal", 20)
    sauce = Item("Secret Sauce", "boost", 3)
    bomb = Item("Grease Bomb", "damage", 15)
    player.inventory = [burger, sauce, bomb]

    print("\nRound 1: Someone greasy stumbles in...")
    enemy1 = Enemy("Waffle Fiend")
    wu_battle_intro(player, enemy1)
    fight(player, enemy1)

    if player.is_alive():
        print("\nSpecial move time.")
        use_special(player, enemy1)

    if player.is_alive():
        print("\nFinal Round: OTHMANE appears.")
        boss = Enemy("OTHMANE", type="boss")
        wu_battle_intro(player, boss)
        fight(player, boss)

    end_scene(player)

if __name__ == "__main__":
    start_game()
