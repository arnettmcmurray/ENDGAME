import random

def wu_battle_intro(player, enemy):
    print("\n🔥 The fryer roars. The tile floor hums. 🔥")
    print(f"{enemy.name} slides in with the confidence of a burnt brisket.")
    print(f"{player.name} stands tall, aura dripping with vaporized grease.\n")

    player_bars = [
        "“I season pain with rhythm — sauté despair in cast-iron stanzas.”",
        "“I wield spatulas like swords, flip egos like flapjacks.”",
        "“Born from the smoke of a thousand broken timers — I never burn out.”",
        "“Your soul’s undercooked. Step into my skillet.”",
        "“I stir-fry chaos with a pinch of regret.”"
    ]

    enemy_bars = [
        "“I deep-fry futures. You? Just a snack in the system.”",
        "“I was battered in prophecy and served cold to kings.”",
        "“My rage is sous vide — slow-cooked and ready to sear your fate.”",
        "“You smell like ambition. I’ll cure that in bacon fat.”",
        "“I pickle dreams and plate nightmares.”"
    ]

    crowd_noise = [
        "A fryer explodes in the background. It’s not a bug — it’s a prophecy.",
        "Someone lights a napkin on fire and waves it like a torch.",
        "The ghost of a retired line cook nods in silence.",
        "A kid shouts, 'IS THIS THE BURGER RING?' — then gets shushed.",
        "A grease trap overflows. The gods are pleased."
    ]

    print(f"🎤 {player.name.upper()} opens fire:")
    print(random.choice(player_bars), "\n")

    print(f"😈 {enemy.name.upper()} claps back:")
    print(random.choice(enemy_bars), "\n")

    print("👁️  The kitchen holds its breath.")
    print(random.choice(crowd_noise))
    print("⚔️  And just like that... it begins.\n")
