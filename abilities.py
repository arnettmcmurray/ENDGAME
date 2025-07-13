import random

def use_special(player, enemy):
    print(f"\n{player.name} uses their special move: {player.special}!")

    if player.special == "Grease Slam":
        damage = player.attack + 5
        enemy.health -= damage
        print(f"Grease Slam crushes {enemy.name} for {damage} damage.")

    elif player.special == "Oil Burst":
        damage = player.attack + random.randint(3, 8)
        enemy.health -= damage
        player.health += 5
        print(f"Oil Burst scorches {enemy.name} for {damage} and heals 5 HP.")

    elif player.special == "Mop Ambush":
        damage = player.attack + 2
        enemy.health -= damage
        player.defense += 3
        print(f"Mop Ambush hits for {damage} and boosts defense by 3.")

    elif player.special == "Slap of Shame":
        damage = 1
        enemy.health -= damage
        print(f"{enemy.name} is mildly inconvenienced for {damage} damage.")

    else:
        print("But nothing happens...")

