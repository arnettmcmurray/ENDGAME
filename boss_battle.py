from combat import fight
from enemy import Enemy
from abilities import use_special
from wu_battle import wu_battle_intro

def fight_boss(player):
    print("\nOTHMANE steps out from the smoke...")
    print("He smells like printer ink and unpaid internships.")

    boss = Enemy("OTHMANE", type="boss")

    wu_battle_intro(player, boss)

    use_special(player, boss)
    fight(player, boss)

    if player.health > 0:
        print(f"{player.name} stands over the fallen corpse of OTHMANE.")
    else:
        print("OTHMANE laughs. You were never worthy.")
