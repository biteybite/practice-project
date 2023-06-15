import random

ac = 14
strength = 4
proficiency = 2
bonus = 1
enemy_hp = 100

def attack_roll():
    die_roll = random.randint(1, 20)
    a_roll_total = die_roll + strength + proficiency + bonus
    if a_roll_total >= ac:
        damage_roll = random.randint(1, 8)
        damage = strength + damage_roll
        global enemy_hp
        enemy_hp -= damage
        print(f"{a_roll_total}! Your swing connects, dealing {damage} damage! The enemy is now at {enemy_hp} hitpoints.")
    else:
        print(f"{a_roll_total}! Unfortunately, your swing misses.")
    print("Next turn:")
    input("> ")
    attack_roll()
    
attack_roll()
