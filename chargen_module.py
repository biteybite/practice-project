import random








class Character(object):
    pass

class Player(Character):
    
    def __init__(self, name):
        self.name = name
        self.ancestry = None
        self.background = None
        self.xp = 0
        self.awakened = None
        self.HP_max = None
        self.size = None
        self.speed = None
        self.languages = []
        self.abilities = []
        self.inventory = {}
        self.attributes = {
            "STR": 2,
            "CON": 2,
            "SPD": 2,
            "REF": 2,
            "CHA": 2,
            "INT": 2,
            "LOG": 2,
            "WIL": 2,
            "MAG": None,
        }
        self.skills = {
            #Combat
            "Melee": 0,
            "Archery": 0,
            "Thrown": 0,
            "Unarmed Combat": 0,
            "Riding": 0,
            #Survival
            "Hunting and Trapping": 0,
            "Navigation": 0,
            "Foraging and Herbalism": 0,
            "Shelter Construction": 0,
            "Cooking": 0,
            #Social
            "Persuasion": 0,
            "Intimidation": 0,
            "Deception": 0,
            "Bargaining": 0,
            "Animal Handling": 0,
            #Physical
            "Athletics": 0,
            "Acrobatics": 0,
            "Hauling": 0,
            "Sneaking": 0,
            "Perception": 0,
            #Magic
            "Numinous Perception": None,
            "Spellcasting": None,
            "Summoning": None,
            "Astral Combat": None,
            "Enchanting": None,
            "Arcana": None,
            "Alchemy": None,
        }
        self.feats = []
        self.formulas = []
        self.spells = []
        self.used_boosts = []
        self.actions = []
        
            
    
def print_status(player):
    print(f"{player.name}'s status:\nAncestry: {player.ancestry}, Size: {player.size}, Speed: {player.speed}\n{player.attributes}\nMax HP: {player.HP_max}\nLanguages: {player.languages}\nAbilities: {player.abilities}\nSkills: {player.skills}\nFeats: {player.feats}\nInventory: {player.inventory}")















class Ancestry:
    def __init__(self, name, description, attributes, abilities, skills, items, languages):
        self.name = name
        self.description = description
        self.abilities = abilities
        self.skills = skills
        self.attributes = attributes
        self.items = items
        self.languages = languages

    
#ANCESTRIES GO HERE        

khevidun = Ancestry("Khevidun", "Hailing from the verdant coastline, fertile valleys and rolling foothills of the Kazbari Mountains, the Khevidun live scattered among a dozen petty kingdoms and principalities. The Khevidun are slightly shorter than the average person, and most prevalently, possess brown hair in loose curls, amber eyes, and an olive-skinned complexion. The Kazbari Mountains are home to vinyards and shepherds, terraced fields, and expansive mountain-fortresses. The predominant religion of the Khevidun is ancestor worship, although there still exist cults to their old gods, the most common of which is Mzisara, the Khevidun goddess of the Sun.",{"CON": 1, "WIL": 1}, ["Enhanced Endurance"], {"Melee": 1, "Shelter Construction": 1, "Hauling": 1, "Athletics": 1, "Persuasion": 1, "Cooking": 1}, {"Clan Dagger": 1}, ["Common", "Khevidun"])

danayra = Ancestry("Danayra", "Known in the common tongue as 'Amazons,' the Danayra are a loose confederation of tribes and clans whose territory stretches across the vast Dahātrus steppe. Their society is matriarchal in nature; every settlement is lead by a clan elder. The Danayra are masters of the horse, and it is said they were the first to domesticate them. They live, for the most part, in semi-nomadic tent cities, and thrive on fishing, trade, hunting, and of course, animal husbandry. They are fair-skinned, with hair that ranges from blond to black. They are of above-average height, and their women tend to be even taller than their men.",{"SPD": 1, "INT": 1}, ["Savvy Outdoorsman"], {"Archery": 1, "Riding": 1, "Bargaining": 1, "Navigation": 1, "Hunting and Trapping": 1, "Animal Handling": 1}, {"Recurve Bow": 1, "Arrow": 10}, ["Common", "Danayra"])


ancestries = [khevidun, danayra]

def apply_ancestry(player, ancestry):
    player.ancestry = ancestry.name
    for attribute, bonus in ancestry.attributes.items():
        player.attributes[attribute] += bonus
    player.languages.extend(ancestry.languages)
    if ancestry.abilities is not None:
        player.abilities.extend(ancestry.abilities)
    if ancestry.items is not None:
        player.inventory.update(ancestry.items)
    for skill, bonus in ancestry.skills.items():
        player.skills[skill] += bonus

def select_ancestry(player, ancestries):
    print("Select an ancestry:")    

    for index, ancestry in enumerate(ancestries):
        print(f"{index + 1}. {ancestry.name}")
    while True:
        selection = input("Enter the number corresponding to your chosen ancestry:\n> ")
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(ancestries):
                raise ValueError
            selected_ancestry = ancestries[index]
            break
        except ValueError:
            print("Invalid Input. Please Enter the number corresponding to your chosen ancestry.")
    print(f"You have selected {selected_ancestry.name}.")
    print(f"{selected_ancestry.description}")
    print(f"This ancestry will affect the following ability scores:{selected_ancestry.attributes}")
    apply_ancestry(player, selected_ancestry)









            
class Item(object):
    pass

class Consumable(Item):
    pass
    

class Background:
    def __init__(self, name, description, attributes, skills, items, awakened):
        self.name = name
        self.description = description
        self.attributes = attributes
        self.skills = skills
        self.items = items
        self.awakened = awakened
    

hunter = Background("Hunter", "PLACEHOLDER", {"INT": 1, "REF": 1, "SPD": 1}, {"Archery": 2, "Hunting and Trapping": 2, "Navigation": 2, "Foraging and Herbalism": 2, "Shelter Construction": 2, "Perception": 2}, {"Tent": 1, "Backpack": 1, "Flint and Steel": 1, "Hunting Knife": 1, "Hatchet": 1, "Rope": 1, "Bow": 1, "Arrow": 10, "Wool Pants": 1, "Leather Boots": 1, "Wool Shirt": 3}, False)

acolyte = Background("Acolyte", "PLACEHOLDER", {"MAG": 1, "WIL": 1, "LOG": 1}, {"Numinous Perception": 2, "Spellcasting": 2, "Summoning": 2, "Arcana": 2, "Persuasion": 2, "Intimidation": 2}, {"Ceremonial Dagger": 1, "Block of Incense": 1, "Candles": 5, "Ceremonial Robes": 1, "Shoes": 1, "Rope": 1, "Simple Sack": 1}, True)


backgrounds = [hunter, acolyte]




def free_boost(player):
    print("Choose one ability score to boost:")
    valid_boosts = [boost for boost, value in player.attributes.items() if value is not None and boost not in player.used_boosts]
    for index, boost in enumerate(valid_boosts):
        print(f"{index+1}. {boost}")
        
    while True:
        choice = input("> ")
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(valid_boosts):
                raise ValueError
            selected_boost = valid_boosts[index]
            break
        except ValueError:
            print("Invalid input. Please enter the number corresponding to your chosen ability score.")
    player.attributes[selected_boost] += 1
    player.used_boosts.append(selected_boost)

    
def select_awakened(player):
    print("There are some who are born with the gift to commune with the divine, to see beyond the mortal veil, to manipulate the very fabric of the universe, and summon beings from the worlds beyond. There are others who consider it a curse.")
    while True:
        choice_awakened = input("Have you been blessed with this curse?\n> ").casefold()
        try:
            if choice_awakened not in ["y", "yes", "no", "n"]:
                raise ValueError
            if choice_awakened in ["y" or "yes"]:
                player.awakened = True
                player.attributes["MAG"] = 3
                magical_skills = ["Numinous Perception", "Spellcasting", "Summoning", "Astral Combat", "Enchanting", "Arcana", "Alchemy"]
                for skill in magical_skills:
                    player.skills[skill] = 0
            elif choice_awakened in ["n" or "no"]:
                player.awakened = False
                print("Choose three ability scores to boost:")
                free_boost(player)
                free_boost(player)
                free_boost(player)
                player.used_boosts = []
            break
        except ValueError:
            print("Please enter a valid input:")
        

def select_background(player, backgrounds):
    print("Select a background:")
    filtered_backgrounds = []
    for index, background in enumerate(backgrounds):
        if not player.awakened and background.awakened:
            continue
        filtered_backgrounds.append(background)
        print(f"{len(filtered_backgrounds)}. {background.name}")

    while True:
        selection = input("Enter the number corresponding to your chosen background.\n> ")
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(filtered_backgrounds):
                raise ValueError
            selected_background = filtered_backgrounds[index]
            break
        except ValueError:
            print("Invalid input. Please enter the number corresponding to your chosen background.\n> ")
        except:
            print("An error occurred. Please try again.")

    print(f"You have selected {selected_background.name}.")
    print(f"{selected_background.description}")
    apply_background(player, selected_background)
    
    
    
def apply_background(player, background):
    player.background = background.name
    for attribute, bonus in background.attributes.items():
        player.attributes[attribute] += bonus
    player.inventory.update(background.items)
    for skill, bonus in background.skills.items():
        player.skills[skill] += bonus

    


def create_player():
    name = input("What is this character's name?\n").strip()
    return Player(name)

def chargen(player):
    select_ancestry(player, ancestries)
    select_awakened(player)
    select_background(player, backgrounds)
    print_status(player)

p1 = create_player()
chargen(p1)













# 
# 
# def background_boost(player, background):
#     print("Choose one ability score to boost:")
#     for index, boost in enumerate(background.boosts.keys()):
#         print(f"{index+1}. {boost}")
#         
#     while True:
#         choice = input("> ")
#         try:
#             index = int(choice) - 1
#             if index < 0 or index >= len(background.boosts):
#                 raise ValueError
#             selected_boost = list(background.boosts.keys())[index]
#             break
#         except ValueError:
#             print("Invalid input. Please enter the number corresponding to your chosen ability score.")
#     player.attributes[selected_boost] += 2
#     
#     print("Choose one more ability score to boost:\n(NOTE: It cannot be identical to the ability score you just boosted.)")
#     for index, boost in enumerate(player.attributes.keys()):
#         print(f"{index+1}. {boost}")
#         
#     while True:
#         choice2 = input("> ")
#         try:
#             index = int(choice2) - 1
#             if (index < 0 or index >= len(player.attributes)):
#                 raise ValueError
#             second_boost = list(player.attributes.keys())[index]
#             if second_boost == selected_boost:
#                 raise ValueError
#             break
#         except ValueError:
#             print("Invalid input. Please try again.")
#     player.attributes[second_boost] += 2
# 




# def ancestry_boost(player):
#     for index, boost in enumerate(player.attributes.keys()):
#         print(f"{index+1}. {boost}")
#         
#     while True:
#         choice = input("Please select an ability score to boost. You may not boost the same ability score twice from the same source.\n> ")
#         try:
#             index = int(choice) - 1
#             if (index < 0 or index >= len(player.attributes)):
#                 raise ValueError
#             ancestry_boost = list(player.attributes.keys())[index]
#             if player.attributes[ancestry_boost] in [8, 12]:
#                 raise ValueError
#             break
#         except ValueError:
#             print("Invalid input. Please try again.")
#     player.attributes[ancestry_boost] += 2
