import random

class Player:
    def __init__(self):
        self.name = input('What is your name?\n> ')
        self.race = None
        self.STR = stat_roll()
        self.CON = stat_roll()
        self.DEX = stat_roll()
        self.CHA = stat_roll()
        self.INT = stat_roll()
        self.WIS = stat_roll()

    def print_attributes(self):
        print(f"{self.name}'s attributes are:\nSTR: {self.STR}, CON: {self.CON}, DEX: {self.DEX}, CHA: {self.CHA}, INT: {self.INT}, WIS: {self.WIS}")
    
    def ancestry(self):
        print(f"From what peoples does {self.name} hail?")
        race_choice = str.casefold(input("> "))
    
        if (race_choice.__contains__("dwarf" or "dwarves")):
            self.race = "dwarf"
            self.CON += 2
            self.STR += 2
            self.DEX -=2
            print(f"{self.name} is a {self.race}.")
            self.print_attributes()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print(f"Confirmed, {self.name} is a {self.race}.")
            else:
                self.CON -= 2
                self.STR -= 2
                self.DEX +=2
                self.ancestry()
            
        elif (race_choice.__contains__("elf" or "elves") and not race_choice.__contains__("half")):
            self.race = "elf"
            self.CON -= 2
            self.DEX += 2
            self.INT += 2
            print(f"{self.name} is a {self.race}.")
            self.print_attributes()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print(f"Confirmed, {self.name} is a {self.race}.")
            else:
                self.CON += 2
                self.DEX -= 2
                self.INT -= 2
                self.ancestry()
    
        elif (race_choice.__contains__("elf" or "elves") and race_choice.__contains__("half")):
            self.race = "half-elf"
            self.CHA += 2
            print(f"{self.name} is a {self.race}.")
            self.print_attributes()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print(f"Confirmed, {self.name} is a {self.race}.")
            else:
                self.CHA -= 2
                self.ancestry()
            
        elif race_choice.__contains__("halfling"):
            self.race = "halfling"
            self.DEX += 2
            self.STR -= 2
            self.WIS += 2
            print(f"{self.name} is a {self.race}.")
            self.print_attributes()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print(f"Confirmed, {self.name} is a {self.race}.")
            else:
                self.DEX -= 2
                self.STR += 2
                self.WIS -= 2
                self.ancestry()
    
        elif race_choice.__contains__("human"):
            self.race = "human"
            self.DEX += 1
            self.STR += 1
            self.WIS += 1
            self.CHA += 1
            self.INT += 1
            self.CON += 1
            print(f"{self.name} is a {self.race}.")
            self.print_attributes()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print(f"Confirmed, {self.name} is a {self.race}.")
            else:
                self.DEX -= 2
                self.STR += 2
                self.WIS -= 2
                self.ancestry()

        else:
            print("Never heard of them. Try again.")
            self.race = ()
            self.ancestry()


def stat_roll():
    stat_result = []
    for _ in range(4):
        roll = random.randint(1, 6)
        stat_result.append(roll)
    stat_result.remove(min(stat_result))
    stat_total = sum(stat_result)
    return stat_total


        
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

p1.print_attributes()
p2.print_attributes()
p3.print_attributes()
p4.print_attributes()

p1.ancestry()
p2.ancestry()
p3.ancestry()
p4.ancestry()

def party_stats():
    p1.print_attributes()
    p2.print_attributes()
    p3.print_attributes()
    p4.print_attributes()

party_stats()

# def attack_roll():
#     die_roll = random.randint(1, 20)
#     a_roll_total = die_roll + self.STR + player_proficiency + player_bonus
#     if a_roll_total >= enemy_ac:
#         damage_roll = random.randint(1, 8)
#         damage = self.STR + damage_roll
#         global enemy_hp
#         enemy_hp -= damage
#         print(f"{a_roll_total}! Your swing connects, dealing {damage} damage! The enemy is now at {enemy_hp} hitpoints.")
#     else:
#         print(f"{a_roll_total}! Unfortunately, your swing misses.")
#     enemy_attack_roll()
# 
# def next_turn():
#     print("What would you like to do?")
#     action = str.casefold(input("> "))
#     if action == "attack":
#         attack_roll()
#     else:
#         print("I'm sorry, I'm not sure what that is.")
#         next_turn()
# 
# def enemy_attack_roll():
#     die_roll = random.randint(1, 20)
#     a_roll_total = die_roll + enemy_strength + enemy_proficiency + enemy_bonus
#     if a_roll_total >= player_ac:
#         damage_roll = random.randint(1, 8)
#         damage = enemy_strength + damage_roll
#         global player_hp
#         player_hp -= damage
#         print(f"{a_roll_total}! Their swing connects, dealing {damage} damage! You are now at {player_hp} hitpoints.")
#     else:
#         print(f"{a_roll_total}! Fortunately, their swing misses.")
#     next_turn()
