import random

def choose_enemy_action(enemy, player):
    if enemy.health < 20 and random.random() < 0.4:
        return "heal"
    return "attack"

def perform_enemy_action(enemy, player):
    action = choose_enemy_action(enemy, player)

    if action == "heal":
        heal = random.randint(6, 12)
        enemy.health += heal
        print(f"{enemy.name} heals themselves for {heal} HP.")
    else:
        damage = max(1, enemy.attack - (player.defense // 2))
        player.health -= damage
        print(f"{enemy.name} attacks {player.name} for {damage} damage.")
