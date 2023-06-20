import random


class Player:
    
    def __init__(self, name):
        self.name = name
        self.ancestry = None
        self.background = None
        self.level = 0
        self.HP_max = None
        self.Class = None
        self.size = None
        self.speed = None
        self.key_ability = None
        self.perception = "Untrained"
        self.languages = []
        self.abilities = []
        self.inventory = []
        self.saving_throws = {
            "Fortitude" : "Untrained",
            "Reflex" : "Untrained",
            "Will" : "Untrained",
        },
        self.attributes = {
            "STR": 10,
            "CON": 10,
            "DEX": 10,
            "CHA": 10,
            "INT": 10,
            "WIS": 10,
        }
        self.skills = {
            "Acrobatics": "Untrained",
            "Arcana": "Untrained",
            "Athletics": "Untrained",
            "Crafting": "Untrained",
            "Deception": "Untrained",
            "Diplomacy": "Untrained",
            "Intimidation": "Untrained",
            "Lore": {
                "Academia": "Untrained",
                "Accounting": "Untrained",
                "Architecture": "Untrained",
                "Art": "Untrained",
                "Cave": "Untrained",
                "Circus": "Untrained",
                "Engineering": "Untrained",
                "Farming": "Untrained",
                "Fishing": "Untrained",
                "Fortune-Telling": "Untrained",
                "Games": "Untrained",
                "Geneaology": "Untrained",
                "Gladiatorial": "Untrained",
                "Guild": "Untrained",
                "Heraldry": "Untrained",
                "Hunting": "Untrained",
                "Labor": "Untrained",
                "Legal": "Untrained",
                "Library": "Untrained",
                "Mercantile": "Untrained",
                "Midwifery": "Untrained",
                "Milling": "Untrained",
                "Mining": "Untrained",
                "Rural": "Untrained",
                "Sailing": "Untrained",
                "Scouting": "Untrained",
                "Scribing": "Untrained",
                "Stabling": "Untrained",
                "Tanning": "Untrained",
                "Theater": "Untrained",
                "Underworld": "Untrained",
                "Urban": "Untrained",
                "Warfare": "Untrained",
            },
            "Medicine": "Untrained",
            "Nature": "Untrained",
            "Occultism": "Untrained",
            "Performance": "Untrained",
            "Religion": "Untrained",
            "Society": "Untrained",
            "Stealth": "Untrained",
            "Survival": "Untrained",
            "Thievery": "Untrained",
        }
        self.feats = []
        self.formulas = []
        self.spells = []
        
    def clear_stats(self):
        self.ancestry = None
        self.attributes = {
            "STR": 10,
            "CON": 10,
            "DEX": 10,
            "CHA": 10,
            "INT": 10,
            "WIS": 10,
        }
        self.HP_max = None
        self.level = 0
        self.saving_throws = {
            "Fortitude" : "Untrained",
            "Reflex" : "Untrained",
            "Will" : "Untrained",
        },
        self.Class = None
        self.size = None
        self.speed = None
        self.languages.clear()
        self.abilities.clear()
        self.inventory.clear()
        self.skills = {
            "Acrobatics": "Untrained",
            "Arcana": "Untrained",
            "Athletics": "Untrained",
            "Crafting": "Untrained",
            "Deception": "Untrained",
            "Diplomacy": "Untrained",
            "Intimidation": "Untrained",
            "Lore": {
                "Academia": "Untrained",
                "Accounting": "Untrained",
                "Architecture": "Untrained",
                "Art": "Untrained",
                "Cave": "Untrained",
                "Circus": "Untrained",
                "Engineering": "Untrained",
                "Farming": "Untrained",
                "Fishing": "Untrained",
                "Fortune-Telling": "Untrained",
                "Games": "Untrained",
                "Geneaology": "Untrained",
                "Gladiatorial": "Untrained",
                "Guild": "Untrained",
                "Heraldry": "Untrained",
                "Hunting": "Untrained",
                "Labor": "Untrained",
                "Legal": "Untrained",
                "Library": "Untrained",
                "Mercantile": "Untrained",
                "Midwifery": "Untrained",
                "Milling": "Untrained",
                "Mining": "Untrained",
                "Rural": "Untrained",
                "Sailing": "Untrained",
                "Scouting": "Untrained",
                "Scribing": "Untrained",
                "Stabling": "Untrained",
                "Tanning": "Untrained",
                "Theater": "Untrained",
                "Underworld": "Untrained",
                "Urban": "Untrained",
                "Warfare": "Untrained",
            },
            "Medicine": "Untrained",
            "Nature": "Untrained",
            "Occultism": "Untrained",
            "Performance": "Untrained",
            "Religion": "Untrained",
            "Society": "Untrained",
            "Stealth": "Untrained",
            "Survival": "Untrained",
            "Thievery": "Untrained",
        }
        self.feats.clear()
            
    
def print_status(player):
    print(f"{player.name}'s status:\nAncestry: {player.ancestry}, Size: {player.size}, Speed: {player.speed}\n{player.attributes}\nMax HP: {player.HP_max}\nLanguages: {player.languages}\nAbilities: {player.abilities}\nSkills: {player.skills}\nFeats: {player.feats}\nInventory: {player.inventory}")

class Ancestry:
    def __init__(self, name, description, abilities, bonuses, items, languages, speed, size, HP):
        self.name = name
        self.description = description
        self.abilities = abilities
        self.bonuses = bonuses
        self.items = items
        self.languages = languages
        self.speed = speed
        self.size = size
        self.HP = HP

class Background:
    def __init__(self, name, description, boosts, skills, feats):
        self.name = name
        self.description = description
        self.boosts = boosts
        self.skills = skills
        self.feats = feats

class Class:
    def __init__(self, name, description, key_ability, HP, skills, saving_throws, attacks, defenses, class_DC, feats, features):
        self.name = name
        self.description = description
        self.key_ability = key_ability
        self.HP = HP
        self.saving_throws = saving_throws
        self.skills = skills
        self.attacks = attacks
        self.defenses = defenses
        self.class_DC = class_DC
        self.feats = feats
        
    def level_up(self, player, level):
        pass

class Alchemist(Class):
    def __init__(self):
        description = "PLACEHOLDER"
        key_ability = "INT"
        HP = 8
        saving_throws = {
            "Fortitude": "Expert",
            "Reflex": "Expert",
            "Will": "Expert"}
        skills = {
            "Crafting": "Trained"
        }
        attacks = {
            "Simple Weapons": "Trained",
            "Alchemical Bombs": "Trained",
            "Unarmed Attacks": "Trained",
        }
        defenses = {
            "Medium Armor": "Trained",
            "Light Armor": "Trained",
            "Unarmored Defense": "Trained",
        }
        class_DC = {
            "Alchemist" : "Trained"}


    
def apply_ancestry(player, ancestry):
    player.ancestry = ancestry.name
    if ancestry.bonuses is not None:
        for attribute, bonus in ancestry.bonuses.items():
            player.attributes[attribute] += bonus
    player.languages.extend(ancestry.languages)
    if ancestry.abilities is not None:
        player.abilities.extend(ancestry.abilities)
    if ancestry.items is not None:
        player.inventory.extend(ancestry.items)
    player.speed = ancestry.speed
    player.size = ancestry.size
    player.HP_max = ancestry.HP
    
def ancestry_boost(player):
    for index, boost in enumerate(player.attributes.keys()):
        print(f"{index+1}. {boost}")
        
    while True:
        choice = input("Please select an ability score to boost. You may not boost the same ability score twice from the same source.\n> ")
        try:
            index = int(choice) - 1
            if (index < 0 or index >= len(player.attributes)):
                raise ValueError
            ancestry_boost = list(player.attributes.keys())[index]
            if player.attributes[ancestry_boost] in [8, 12]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please try again.")
    player.attributes[ancestry_boost] += 2

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
    print(f"This ancestry will affect the following ability scores:{selected_ancestry.bonuses}")
    apply_ancestry(player, selected_ancestry)

def background_boost(player, background):
    print("Choose one ability score to boost:")
    for index, boost in enumerate(background.boosts.keys()):
        print(f"{index+1}. {boost}")
        
    while True:
        choice = input("> ")
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(background.boosts):
                raise ValueError
            selected_boost = list(background.boosts.keys())[index]
            break
        except ValueError:
            print("Invalid input. Please enter the number corresponding to your chosen ability score.")
    player.attributes[selected_boost] += 2
    
    print("Choose one more ability score to boost:\n(NOTE: It cannot be identical to the ability score you just boosted.)")
    for index, boost in enumerate(player.attributes.keys()):
        print(f"{index+1}. {boost}")
        
    while True:
        choice2 = input("> ")
        try:
            index = int(choice2) - 1
            if (index < 0 or index >= len(player.attributes)):
                raise ValueError
            second_boost = list(player.attributes.keys())[index]
            if second_boost == selected_boost:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please try again.")
    player.attributes[second_boost] += 2

def apply_background(player, background):
    player.background = background.name
    for skill, bonus in background.skills.items():
        if isinstance(bonus, int):
            if skill in player.skills:
                player.skills[skill] = "Proficient"
        elif isinstance(bonus, dict):
            for sub_skill, sub_bonus in bonus.items():
                if sub_skill in player.skills[skill]:
                    player.skills[skill][sub_skill] = "Proficient"
    background_boost(player, background)
    player.feats.extend(background.feats)
    

def select_background(player, backgrounds):
    print("Select a background:")
    for index, background in enumerate(backgrounds):
        print(f"{index + 1}. {background.name}")
    while True:
        selection = input("Enter the number corresponding to your chosen background.\n> ")
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(backgrounds):
                raise ValueError
            selected_background = backgrounds[index]
            break
        except ValueError:
            print("Invalid input. Please Enter the number corresponding to your chosen background.\n> ")
    print(f"You have selected {selected_background.name}.")
    print(f"{selected_background.description}")
    apply_background(player, selected_background)

def create_player():
    name = input("What is this character's name?\n").strip()
    return Player(name)

def chargen(player):
    select_ancestry(player, ancestries)
    if player.ancestry == "Human":
        ancestry_boost(player)
        ancestry_boost(player)
    else:
        ancestry_boost(player)
    select_background(player, backgrounds)
    print_status(player)
    
    
#ANCESTRIES GO HERE        
ancestries = [
    Ancestry(
        name = "Dwarf",
        description = "PLACEHOLDER",
        bonuses = {
            "CON": 2,
            "WIS": 2,
            "CHA": -2
        },
        abilities = ["Darkvision"],
        languages = ["Common", "Dwarven"],
        items = ["Clan Dagger"],
        speed = 20,
        size = "Medium",
        HP = 10),

    Ancestry(
        name = "Elf",
        description = "PLACEHOLDER",
        bonuses = {
            "DEX": 2,
            "INT": 2,
            "CON": -2
        },
        abilities = ["Low-Light Vision"],
        languages = ["Common", "Elven"],
        items = None,
        speed = 30,
        size = "Medium",
        HP = 6),

    Ancestry(
        name = "Gnome",
        description = "PLACEHOLDER",
        bonuses = {
            "CON": 2,
            "CHA": 2,
            "STR": -2
        },
        abilities = ["Low-Light Vision"],
        languages = ["Common", "Gnomish", "Sylvan"],
        items = None,
        speed = 25,
        size = "Small",
        HP = 8),


    Ancestry(
        name = "Goblin",
        description = "PLACEHOLDER",
        bonuses = {
            "DEX": 2,
            "CHA": 2,
            "WIS": -2
        },
        abilities = ["Darkvision"],
        languages = ["Common", "Goblin"],
        items = None,
        speed = 25,
        size = "Small",
        HP = 6),

    Ancestry(
        name = "Halfling",
        description = "PLACEHOLDER",
        bonuses = {
            "DEX": 2,
            "WIS": 2,
            "STR": -2
        },
        abilities = ["Keen Eyes"],
        languages = ["Common", "Halfling"],
        items = None,
        speed = 25,
        size = "Small",
        HP = 6),

    Ancestry(
        name = "Human",
        description = "PLACEHOLDER",
        bonuses = None,
        abilities = None,
        languages = ["Common"],
        items = None,
        speed = 25,
        size = "Medium",
        HP = 8),
]
    
#BACKGROUNDS GO HERE
backgrounds = [
    Background(
        name = "Acolyte",
        description = "You spent your early days in a religious monastery or cloister. You may have traveled out into the world to spread the message of your religion or because you cast away the teachings of your faith, but deep down you’ll always carry within you the lessons you learned.",
        boosts = {
            "INT": 2, 
            "WIS": 2
        },
        skills = {
            "Religion": 2,
            "Lore": {
                "Scribing": 2,
            },
        },
        feats = ["Student of the Canon"]),

    Background(
        name = "Acrobat",
        description = "In a circus or on the streets, you earned your pay by performing as an acrobat. You might have turned to adventuring when the money dried up, or simply decided to put your skills to better use.",
        boosts = {
            "STR": 2, 
            "DEX": 2
        },
        skills = {
            "Acrobatics": 2,
            "Lore": {
                "Circus": 2,
            },
        },
        feats = ["Steady Balance"]),

    Background(
        name = "Animal Whisperer",
        description = "PLACEHOLDER.",
        boosts = {
            "WIS": 2,
            "CHA": 2,
        },
        skills = {
            "Acrobatics": 2,
            "Lore": {
                "Circus": 2,
            },
        },
        feats = ["Steady Balance"]),

    Background(
        name = "Artisan",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2, 
            "INT": 2,
        },
        skills = {
            "Acrobatics": 2,
            "Lore": {
                "Circus": 2,
            },
        },
        feats = ["Steady Balance"]),

    Background(
        name = "Artist",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "CHA": 2,
        },
        skills = {
            "Crafting": 2,
            "Lore": {
                "Art": 2,
            },
        },
        feats = ["Specialty Crafting"]),

    Background(
        name = "Barkeep",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "CHA": 2,
        },
        skills = {
            "Diplomacy": 2,
            "Lore": {
                "Alcohol": 2,
            },
        },
        feats = ["Hobnobber"]),

    Background(
        name = "Barrister",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "CHA": 2,
        },
        skills = {
            "Diplomacy": 2,
            "Lore": {
                "Alcohol": 2,
            },
        },
        feats = ["Hobnobber"]),

    Background(
        name = "Bounty Hunter",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "WIS": 2,
        },
        skills = {
            "Survival": 2,
            "Lore": {
                "Legal": 2,
            },
        },
        feats = ["Experienced Tracker"]),

    Background(
        name = "Charlatan",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "CHA": 2,
        },
        skills = {
            "Deception": 2,
            "Lore": {
                "Underworld": 2,
            },
        },
        feats = ["Charming Liar"]),
            
    Background(
        name = "Criminal",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "INT": 2,
        },
        skills = {
            "Stealth": 2,
            "Lore": {
                "Underworld": 2,
            },
        },
        feats = ["Experienced Smuggler"]),

    Background(
        name = "Detective",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "WIS": 2,
        },
        skills = {
            "Society": 2,
            "Lore": {
                "Underworld": 2,
            },
        },
        feats = ["Streetwise"]),

    Background(
        name = "Emissary",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "CHA": 2,
        },
        skills = {
            "Society": 2,
            "Lore": {
                "Urban": 2,
            },
        },
        feats = ["Multilingual"]),

    Background(
        name = "Entertainer",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "CHA": 2,
        },
        skills = {
            "Performance": 2,
            "Lore": {
                "Theater": 2,
            },
        },
        feats = ["Fascinating Performance"]),

    Background(
        name = "Farmhand",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "WIS": 2,
        },
        skills = {
            "Athletics": 2,
            "Lore": {
                "Farming": 2,
            },
        },
        feats = ["Assurance"]),

    Background(
        name = "Field Medic",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "WIS": 2,
        },        skills = {
            "Medicine": 2,
            "Lore": {
                "Warfare": 2,
            },
        },
        feats = ["Battle Medicine"]),
            
    Background(
        name = "Fortune Teller",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "CHA": 2,
        },
        skills = {
            "Occultism": 2,
            "Lore": {
                "Fortune-Telling": 2,
            },
        },
        feats = ["Oddity Identification"]),

    Background(
        name = "Gambler",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "CHA": 2,
        },
        skills = {
            "Deception": 2,
            "Lore": {
                "Games": 2,
            },
        },
        feats = ["Lie to Me"]),

    Background(
        name = "Gladiator",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "CHA": 2,
        },
        skills = {
            "Performance": 2,
            "Lore": {
                "Gladiatorial": 2,
            },
        },
        feats = ["Impressive Performance"]),

    Background(
        name = "Guard",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "CHA": 2,
        },
        skills = {
            "Intimidation": 2,
            "Lore": {
                "Legal": 2,
            },
        },
        feats = ["Quick Coercion"]),

    Background(
        name = "Herbalist",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "WIS": 2,
        },
        skills = {
            "Nature": 2,
            "Lore": {
                "Herbalism": 2,
            },
        },
        feats = ["Natural Medicine"]),

    Background(
        name = "Hermit",
        description = "PLACEHOLDER.",
        boosts = {
            "CON": 2,
            "WIS": 2,
        },
        skills = {
            "Nature": 2,
            "Lore": {
                "Cave": 2,
            },
        },
        feats = ["Dubious Knowledge"]),

    Background(
        name = "Hunter",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "WIS": 2,
        },
        skills = {
            "Society": 2,
            "Lore": {
                "Urban": 2,
            },
        },
        feats = ["Survey Wildlife"]),

    Background(
        name = "Laborer",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "CON": 2,
        },
        skills = {
            "Athletics": 2,
            "Lore": {
                "Labor": 2,
            },
        },
        feats = ["Hefty Hauler"]),

    Background(
        name = "Martial Disciple",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "DEX": 2,
        },
        skills = {
            "Athletics": 2,
            "Lore": {
                "Warfare": 2,
            },
        },
        feats = ["Quick Jump"]),

    Background(
        name = "Merchant",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "CHA": 2,
        },
        skills = {
            "Diplomacy": 2,
            "Lore": {
                "Mercantile": 2,
            },
        },
        feats = ["Bargain Hunter"]),

    Background(
        name = "Miner",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "WIS": 2,
        },
        skills = {
            "Survival": 2,
            "Lore": {
                "Mining": 2,
            },
        },
        feats = ["Terrain Expertise"]),

    Background(
        name = "Noble",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "CHA": 2,
        },
        skills = {
            "Society": 2,
            "Lore": {
                "Heraldry": 2,
            },
        },
        feats = ["Courtly Graces"]),

    Background(
        name = "Prisoner",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "CON": 2,
        },
        skills = {
            "Stealth": 2,
            "Lore": {
                "Underworld": 2,
            },
        },
        feats = ["Experienced Smuggler"]),

    Background(
        name = "Sailor",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "DEX": 2,
        },
        skills = {
            "Athletics": 2,
            "Lore": {
                "Sailing": 2,
            },
        },
        feats = ["Underwater Marauder"]),

    Background(
        name = "Scout",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "WIS": 2,
        },
        skills = {
            "Survival": 2,
            "Lore": {
                "Rural": 2,
            },
        },
        feats = ["Forager"]),

    Background(
        name = "Street Urchin",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "CON": 2,
        },
        skills = {
            "Thievery": 2,
            "Lore": {
                "Urban": 2,
            },
        },
        feats = ["Pickpocket"]),

    Background(
        name = "Tinker",
        description = "PLACEHOLDER.",
        boosts = {
            "DEX": 2,
            "INT": 2,
        },
        skills = {
            "Crafting": 2,
            "Lore": {
                "Engineering": 2,
            },
        },
        feats = ["Specialty Crafting"]),

    Background(
        name = "Warrior",
        description = "PLACEHOLDER.",
        boosts = {
            "STR": 2,
            "CON": 2,
        },
        skills = {
            "Intimidation": 2,
            "Lore": {
                "Warfare": 2,
            },
        },
        feats = ["Intimidating Glare"]),

    Background(
        name = "Scholar",
        description = "PLACEHOLDER.",
        boosts = {
            "INT": 2,
            "WIS": 2,
        },
        skills = {
            "Society": 2,
            "Lore": {
                "Academia": 2,
            },
        },
        feats = ["Assurance"]),
]

p1 = create_player()
chargen(p1)
