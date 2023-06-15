import random

player_ac = 18
player_strength = 4
player_proficiency = 2
player_bonus = 1
player_hp = 50
enemy_ac = 10
enemy_strength = 2
enemy_proficiency = 0
enemy_bonus = 0
enemy_hp = 100


def attack_roll():
    die_roll = random.randint(1, 20)
    a_roll_total = die_roll + player_strength + player_proficiency + player_bonus
    if a_roll_total >= enemy_ac:
        damage_roll = random.randint(1, 8)
        damage = player_strength + damage_roll
        global enemy_hp
        enemy_hp -= damage
        print(f"{a_roll_total}! Your swing connects, dealing {damage} damage! The enemy is now at {enemy_hp} hitpoints.")
    else:
        print(f"{a_roll_total}! Unfortunately, your swing misses.")
    enemy_attack_roll()

def next_turn():
    print("What would you like to do?")
    action = str.casefold(input("> "))
    if action == "attack":
        attack_roll()
    else:
        print("I'm sorry, I'm not sure what that is.")
        next_turn()

def enemy_attack_roll():
    die_roll = random.randint(1, 20)
    a_roll_total = die_roll + enemy_strength + enemy_proficiency + enemy_bonus
    if a_roll_total >= player_ac:
        damage_roll = random.randint(1, 8)
        damage = enemy_strength + damage_roll
        global player_hp
        player_hp -= damage
        print(f"{a_roll_total}! Their swing connects, dealing {damage} damage! You are now at {player_hp} hitpoints.")
    else:
        print(f"{a_roll_total}! Fortunately, their swing misses.")
    next_turn()

next_turn()
