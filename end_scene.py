def end_scene(player):
    if player.health > 0:
        print(f"\n{player.name} walks away from Burgertown. Scarred. Full of grease. Victorious.")
    else:
        print("\nYou died like a half-eaten drive-thru order. Cold. Forgotten. No refund.")
