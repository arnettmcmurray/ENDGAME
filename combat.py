# combat.py

import random

def calculate_damage(attacker, defender):
    return max(1, attacker.attack - (defender.defense // 2))

def player_turn(player, enemy):
    print(f"\n{player.name}'s Turn")
    print("1. Attack")
    print("2. Heal")
    choice = input("Choose action: ")

    if choice == "1":
        damage = calculate_damage(player, enemy)
        enemy.health -= damage
        print(f"{player.name} hits {enemy.name} for {damage} damage.")
    elif choice == "2":
        heal = random.randint(8, 15)
        player.health += heal
        print(f"{player.name} heals for {heal} HP.")
    else:
        print("Invalid input. Turn skipped.")

def enemy_turn(enemy, player):
    print(f"\n{enemy.name}'s Turn")
    if enemy.health < 15 and random.random() < 0.5:
        heal = random.randint(5, 12)
        enemy.health += heal
        print(f"{enemy.name} heals for {heal} HP.")
    else:
        damage = calculate_damage(enemy, player)
        player.health -= damage
        print(f"{enemy.name} strikes {player.name} for {damage} damage.")

def check_battle_status(player, enemy):
    if player.health <= 0:
        print(f"\n{player.name} has been defeated by {enemy.name}.")
        return "lose"
    elif enemy.health <= 0:
        print(f"\n{player.name} has defeated {enemy.name}!")
        return "win"
    return "continue"

def run_battle(player, enemy):
    print(f"\nBattle Start: {player.name} vs {enemy.name}")
    while True:
        player_turn(player, enemy)
        if check_battle_status(player, enemy) != "continue":
            break
        enemy_turn(enemy, player)
        if check_battle_status(player, enemy) != "continue":
            break
