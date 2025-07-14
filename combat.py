import random

def get_damage(attacker, defender):
    base = attacker.attack - (defender.defense // 2)
    return max(1, base)

def player_move(player, enemy):
    print(f"\n🧠 {player.name}'s Move")
    print("1. Attack")
    print("2. Heal")
    choice = input("Pick your move: ")

    if choice == "1":
        damage = get_damage(player, enemy)
        enemy.health -= damage
        print(f"{player.name} smacks {enemy.name} for {damage} damage.")
    elif choice == "2":
        heal = random.randint(8, 15)
        player.health += heal
        print(f"{player.name} eats a burger and heals {heal} HP.")
    else:
        print("You hesitated. You lose your turn.")

def enemy_move(enemy, player):
    print(f"\n😈 {enemy.name}'s Move")
    if enemy.health < 15 and random.random() < 0.5:
        heal = random.randint(5, 12)
        enemy.health += heal
        print(f"{enemy.name} slurps mystery sauce and heals {heal} HP.")
    else:
        damage = get_damage(enemy, player)
        player.health -= damage
        print(f"{enemy.name} claws {player.name} for {damage} damage.")

def check_winner(player, enemy):
    if player.health <= 0:
        print(f"\n💀 {player.name} got dropped by {enemy.name}.")
        return "lose"
    elif enemy.health <= 0:
        print(f"\n🏆 {player.name} wrecked {enemy.name}!")
        return "win"
    return "keep going"

def fight(player, enemy):
    print(f"\n⚔️  FIGHT: {player.name} vs {enemy.name}")
    while True:
        player_move(player, enemy)
        if check_winner(player, enemy) != "keep going":
            break

        enemy_move(enemy, player)
        if check_winner(player, enemy) != "keep going":
            break
