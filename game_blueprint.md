# Game Blueprint: Defeat the Evil Wizard

## Theme:
- Comedic/dark RPG
- Set in “Burgertown”
- Final boss: OTHMANE

## Core Components

### Player Character
- name (str)
- role (str)
- health (int)
- attack (int)
- defense (int)
- inventory (list)
- special (str or method)

### Enemies
- name (str)
- type (minion, boss)
- health (int)
- attack (int)
- defense (int)
- special (optional)
- intro_text (str)

### Items
- burgers = healing
- grease_bombs = damage
- secret_sauce = boost
- stored in list of dicts

### Combat
- Turn-based
- Actions: Attack, Heal, Use Item
- Enemy: random or logic-based attack
- Damage = attacker.attack - (defender.defense // 2)

### Game Loop
- Intro
- Character select
- Fight minions → boss
- Win/Lose → Replay?

### Input
- player name
- class selection
- action choices
- item usage

## Build Order
1. player.py
2. enemy.py
3. combat_engine.py
4. inventory.py
5. abilities.py
6. ai_logic.py
7. game_loop.py
8. boss_battle.py
9. end_screen.py
