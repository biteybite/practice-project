import random

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

def stat_roll():
    stat_result = []
    for _ in range(4):
        roll = random.randint(1, 6)
        stat_result.append(roll)
    stat_result.remove(min(stat_result))
    stat_total = sum(stat_result)
    return stat_total

def ancestry():
    print("From what peoples do you hail?")
    race_choice = str.casefold(input("> "))
    global player_constitution, player_strength, player_dexterity, player_charisma, player_wisdom, player_intelligence, player_race
    
    if (race_choice.__contains__("dwarf" or "dwarves")):
        player_race = "dwarf"
        player_constitution += 2
        player_strength += 2
        player_dexterity -=2
        print(f"You are a {player_race}. Your constitution is now {player_constitution}. Your strength is now {player_strength}. Your dexterity is now {player_dexterity}.")
        print("Press y to confirm your choice. Press n to choose a different origin.")
        choice = input("> ")
        if choice == "y":
            print("Confirmed, you are a dwarf.")
        else:
            player_constitution -= 2
            player_strength -= 2
            player_dexterity +=2
            ancestry()
            
    elif (race_choice.__contains__("elf" or "elves") and not race_choice.__contains__("half")):
        player_race = "elf"
        player_constitution -= 2
        player_dexterity += 2
        player_intelligence += 2
        print(f"You are an {player_race}. Your constitution is now {player_constitution}. Your dexterity is now {player_dexterity}. Your intelliegence is now {player_intelligence}.")
        print("Press y to confirm your choice. Press n to choose a different origin.")
        choice = input("> ")
        if choice == "y":
            print("Confirmed, you are an elf.")
        else:
            player_constitution += 2
            player_dexterity -= 2
            player_intelligence -= 2
            ancestry()
    
    elif (race_choice.__contains__("elf" or "elves") and race_choice.__contains__("half")):
        player_race = "half-elf"
        player_charisma += 2
        print(f"You are a {player_race}. Your charisma is now {player_charisma}.")
        print("Press y to confirm your choice. Press n to choose a different origin.")
        choice = input("> ")
        if choice == "y":
            print("Confirmed, you are a half-elf.")
        else:
            player_charisma -= 2
            ancestry()

    else:
        print("Never heard of them. Try again.")
        player_race = ()
        ancestry()
        


def character_creation():
    print("What is your name?")
    global player_name, player_strength, player_constitution, player_dexterity, player_charisma, player_intelligence, player_wisdom
    player_name = input("> ")
    print(f"{player_name}, huh? Interesting name.")

    print("Let's roll your stats.")
    input("> ")
    player_strength = stat_roll()
    print(f"You have a strength score of {player_strength}")
    player_constitution = stat_roll()
    print(f"You have a constitution score of {player_constitution}")
    player_dexterity = stat_roll()
    print(f"You have a dexterity score of {player_dexterity}")
    player_charisma = stat_roll()
    print(f"You have a charisma score of {player_charisma}")
    player_intelligence = stat_roll()
    print(f"You have a intelligence score of {player_intelligence}")
    player_wisdom = stat_roll()
    print(f"You have a wisdom score of {player_wisdom}")
    
    ancestry()
    
    

character_creation()
