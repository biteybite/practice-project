import random

<<<<<<< HEAD

class Player:
    
    def __init__(self):
        self.name = input("What is this character's name?\n> ")
        self.race = None
        self.STR = 10
        self.CON = 10
        self.DEX = 10
        self.CHA = 10
        self.INT = 10
        self.WIS = 10
        self.HP_max = None
        self.Class = None
        self.size = None
        self.speed = None
        self.languages = []
        self.abilities = []
        self.inventory = []
        
    def clear_stats(self):
        self.race = None
        self.STR = 10
        self.CON = 10
        self.DEX = 10
        self.CHA = 10
        self.INT = 10
        self.WIS = 10
        self.HP_max = None
        self.Class = None
        self.size = None
        self.speed = None
        self.languages.clear()
        self.abilities.clear()
        self.inventory.clear()
        
    def boost_dwarf(self):            
        print("Input 1 for Ability Boosts based on your Ancestry or 2 for Two Free Ability Boosts\nNOTE: You may not boost any single stat twice at this stage.")
        print("Dwarf Boosts: CON, WIS. Dwarf Flaws: CHA")
        an_boost = input("> ")
            
        if an_boost == "1":
            self.CON += 2
            self.WIS += 2
            self.CHA -= 2
            self.ancestry_boost()
        elif an_boost == "2":
            self.ancestry_boost()
            self.ancestry_boost()
        else:
            print("Try again.")
            self.boost_dwarf()

    def boost_elf(self):            
        print("Input 1 for Ability Boosts based on your Ancestry or 2 for Two Free Ability Boosts\nNOTE: You may not boost any single stat twice at this stage.")
        print("Elf Boosts: DEX, INT. Elf Flaws: CON")
        an_boost = input("> ")
            
        if an_boost == "1":
            self.DEX += 2
            self.INT += 2
            self.CON -= 2
            self.ancestry_boost()
        elif an_boost == "2":
            self.ancestry_boost()
            self.ancestry_boost()
        else:
            print("Try again.")
            self.boost_elf()
        
    def boost_gnome(self):            
        print("Input 1 for Ability Boosts based on your Ancestry or 2 for Two Free Ability Boosts\nNOTE: You may not boost any single stat twice at this stage.")
        print("Gnome Boosts: CON, CHA. Gnome Flaws: STR")
        an_boost = input("> ")
            
        if an_boost == "1":
            self.CON += 2
            self.CHA += 2
            self.STR -= 2
            self.ancestry_boost()
        elif an_boost == "2":
            self.ancestry_boost()
            self.ancestry_boost()
        else:
            print("Try again.")
            self.boost_gnome()

    def boost_goblin(self):            
        print("Input 1 for Ability Boosts based on your Ancestry or 2 for Two Free Ability Boosts\nNOTE: You may not boost any single stat twice at this stage.")
        print("
        an_boost = input("> ")
            
        if an_boost == "1":
            self.DEX += 2
            self.CHA += 2
            self.WIS -= 2
            self.ancestry_boost()
        elif an_boost == "2":
            self.ancestry_boost()
            self.ancestry_boost()
        else:
            print("Try again.")
            self.boost_goblin()

    def boost_halfling(self):            
        print("Input 1 for Ability Boosts based on your Ancestry or 2 for Two Free Ability Boosts\nNOTE: You may not boost any single stat twice at this stage.")
        an_boost = input("> ")
            
        if an_boost == "1":
            self.DEX += 2
            self.WIS += 2
            self.STR -= 2
            self.ancestry_boost()
        elif an_boost == "2":
            self.ancestry_boost()
            self.ancestry_boost()
        else:
            print("Try again.")
            self.boost_halfling()


    def print_status(self):
        print(f"{self.name}'s status:\nAncestry: {self.race}, Size: {self.size}, Speed: {self.speed}\nSTR: {self.STR}, CON: {self.CON}, DEX: {self.DEX}, CHA: {self.CHA}, INT: {self.INT}, WIS: {self.WIS}\nMax HP: {self.HP_max}\nLanguages: {self.languages}\nAbilities: {self.abilities}\nInventory: {self.inventory}")
    
    def ancestry_boost(self):
        boost_choice = str.casefold(input("Choose another ability score to boost.\n> "))
        if (boost_choice.__contains__("str" or "strength") and not (self.STR == (8 or 12))):
            self.STR += 2
        elif (boost_choice.__contains__("con" or "constitution") and not (self.CON == (8 or 12))):
            self.CON += 2
        elif (boost_choice.__contains__("dex" or "dexterity") and not (self.DEX == (8 or 12))):
            self.DEX += 2
        elif (boost_choice.__contains__("cha" or "charisma") and not (self.CHA == (8 or 12))):
            self.CHA += 2
        elif (boost_choice.__contains__("int" or "intelligence") and not (self.INT == (8 or 12))):
            self.INT += 2
        elif (boost_choice.__contains__("wis" or "wisdom") and not (self.WIS == (8 or 12))):
            self.WIS += 2
        else: 
            print("Sorry, that's not a valid option. Try again.")
            self.ancestry_boost()

    def ancestry(self):
        print(f"From what peoples does {self.name} hail?\nYou may choose between: Dwarf, Elf, Gnome, Goblin, Halfling, Human.")
        race_choice = str.casefold(input("> "))
        global boost_choice
        
        if (race_choice.__contains__("dwarf" or "dwarves")):
            self.race = "dwarf"
            self.HP_max = 10
            self.boost_dwarf()
            self.size = "Medium"
            self.speed = 20
            self.languages.append("Common")
            self.languages.append("Dwarven")
            self.abilities.append("Darkvision")
            self.inventory.append("Clan Dagger")
            self.print_status()
            
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            
            if choice == "y":
                print("Confirmed.")
            else:
                self.clear_stats()
                self.ancestry()

            
        elif (race_choice.__contains__("elf" or "elves")):
            self.race = "elf"
            self.HP_max = 6
            self.size = "Medium"
            self.speed = 30
            self.boost_elf()
            self.languages.append("Common")
            self.languages.append("Elven")
            self.abilities.append("Low-Light Vision")
            self.print_status()
            self.ancestry_boost()
            self.print_status()
            
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print("Confirmed")
            else:
                self.clear_stats()
                self.ancestry()

        elif (race_choice.__contains__("gnome")):
            self.race = "gnome"
            self.HP_max = 8
            self.boost_gnome()
            self.size = "Small"
            self.speed = 25
            self.languages.append("Common")
            self.languages.append("Gnomish")
            self.abilities.append("Low-Light Vision")
            self.print_status()
            self.ancestry_boost()
            self.print_status()

            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print("Confirmed.")
            else:
                self.clear_stats()
                self.ancestry()

        elif (race_choice.__contains__("goblin")):
            self.race = "goblin"
            self.HP_max = 6
            self.boost_goblin()
            self.size = "Small"
            self.speed = 25
            self.languages.append("Common")
            self.languages.append("Goblin")
            self.print_status()
            self.ancestry_boost()
            self.print_status()

            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print("Confirmed.")
            else:
                self.clear_stats()
                self.ancestry()

        elif (race_choice.__contains__("halfling")):
            self.race = "halfling"
            self.HP_max = 6
            self.boost_halfling()
            self.size = "Small"
            self.speed = 25
            self.languages.append("Common")
            self.languages.append("Halfling")
            self.abilities.append("Keen Eyes")
            self.print_status()
            self.ancestry_boost()
            self.print_status()
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print("Confirmed.")
            else:
                self.clear_stats()
                self.ancestry()

        elif (race_choice.__contains__("human")):
            self.race = "human"
            self.HP_max = 8
            self.size = "Medium"
            self.speed = 25
            self.languages.append("Common")
            print("You may choose two free Ability boosts.")
            self.ancestry_boost()
            self.ancestry_boost()
            self.print_status()            
            print("Press y to confirm your choice. Press n to choose a different origin.")
            choice = input("> ")
            if choice == "y":
                print("Confirmed.")
            else:
                self.clear_stats()
                self.ancestry()
                
=======
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
>>>>>>> bf17b9554dd5c341ab2506039dd98905ab59c8dd

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
<<<<<<< HEAD

p1.print_status()

p1.ancestry()
=======
p2 = Player()
p3 = Player()
p4 = Player()
>>>>>>> bf17b9554dd5c341ab2506039dd98905ab59c8dd

p1.print_attributes()
p2.print_attributes()
p3.print_attributes()
p4.print_attributes()

<<<<<<< HEAD
def party_stats():
    p1.print_status()
    p2.print_status()
    p3.print_status()
    p4.print_status()


=======
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

>>>>>>> bf17b9554dd5c341ab2506039dd98905ab59c8dd
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
