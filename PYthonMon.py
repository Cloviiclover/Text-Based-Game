import sys,os,time,random

p_id_1 = 1
p_id_2 = 1
p_id_3 = 1

def print_slow(str): #Prints out text slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def clear(): #Clears all text on screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_sprite(filename): #Loads sprite/sprite text file
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def print_sprite(filename): #Prints out a sprite/sprite text file
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

def normal(): #Normal difficulty
    global p_id_1, p_id_2, p_id_3
    p_id_1 = random.randint(1,6) #ID randomiser for 1st PYthonMon
    p_id_2 = random.randint(1,6) #ID randomiser for 2nd PYthonMon
    p_id_3 = random.randint(1,6) #ID randomiser for 3rd PYthonMon

def hard(): #Hard difficulty
    global p_id_1, p_id_2, p_id_3
    p_id_1 = random.randint(7,12) #ID randomiser for 1st PYthonMon
    p_id_2 = random.randint(7,12) #ID randomiser for 2nd PYthonMon
    p_id_3 = random.randint(7,12) #ID randomiser for 3rd PYthonMon

def player_starters(): #Complete Stat transfer for Player's PYthonMon when getting the 3 starters
    
    #1st PYthonMon info transfer
    player["py_1"]["name"] = pythonmon[(p_id_1)]["name"]
    player["py_1"]["base_hp"] = pythonmon[(p_id_1)]["base_hp"]
    player["py_1"]["base_atk"] = pythonmon[(p_id_1)]["base_atk"]
    player["py_1"]["base_def"] = pythonmon[(p_id_1)]["base_def"]
    player["py_1"]["base_spd"] = pythonmon[(p_id_1)]["base_spd"]
    player["py_1"]["base_spec"] = pythonmon[(p_id_1)]["base_spec"]
    player["py_1"]["move_1"] = pythonmon[(p_id_1)]["move_1"]
    player["py_1"]["move_2"] = pythonmon[(p_id_1)]["move_2"]
    player["py_1"]["move_3"] = pythonmon[(p_id_1)]["move_3"]
    player["py_1"]["move_4"] = pythonmon[(p_id_1)]["move_4"]
    player["py_1"]["f_sprite"] = pythonmon[(p_id_1)]["f_sprite"]
    player["py_1"]["b_sprite"] = pythonmon[(p_id_1)]["b_sprite"]
    player["py_1"]["hp_bar"] = "████████████████████"

    #2nd PYthonMon info transfer
    player["py_2"]["name"] = pythonmon[(p_id_2)]["name"]
    player["py_2"]["base_hp"] = pythonmon[(p_id_2)]["base_hp"]
    player["py_2"]["base_atk"] = pythonmon[(p_id_2)]["base_atk"]
    player["py_2"]["base_def"] = pythonmon[(p_id_2)]["base_def"]
    player["py_2"]["base_spd"] = pythonmon[(p_id_2)]["base_spd"]
    player["py_2"]["base_spec"] = pythonmon[(p_id_2)]["base_spec"]
    player["py_2"]["move_1"] = pythonmon[(p_id_2)]["move_1"]
    player["py_2"]["move_2"] = pythonmon[(p_id_2)]["move_2"]
    player["py_2"]["move_3"] = pythonmon[(p_id_2)]["move_3"]
    player["py_2"]["move_4"] = pythonmon[(p_id_2)]["move_4"]
    player["py_2"]["f_sprite"] = pythonmon[(p_id_2)]["f_sprite"]
    player["py_2"]["b_sprite"] = pythonmon[(p_id_2)]["b_sprite"]
    player["py_2"]["hp_bar"] = "████████████████████"

    #3rd PYthonMon info transfer
    player["py_3"]["name"] = pythonmon[(p_id_3)]["name"]
    player["py_3"]["base_hp"] = pythonmon[(p_id_3)]["base_hp"]
    player["py_3"]["base_atk"] = pythonmon[(p_id_3)]["base_atk"]
    player["py_3"]["base_def"] = pythonmon[(p_id_3)]["base_def"]
    player["py_3"]["base_spd"] = pythonmon[(p_id_3)]["base_spd"]
    player["py_3"]["base_spec"] = pythonmon[(p_id_3)]["base_spec"]
    player["py_3"]["move_1"] = pythonmon[(p_id_3)]["move_1"]
    player["py_3"]["move_2"] = pythonmon[(p_id_3)]["move_2"]
    player["py_3"]["move_3"] = pythonmon[(p_id_3)]["move_3"]
    player["py_3"]["move_4"] = pythonmon[(p_id_3)]["move_4"]
    player["py_3"]["f_sprite"] = pythonmon[(p_id_3)]["f_sprite"]
    player["py_3"]["b_sprite"] = pythonmon[(p_id_3)]["b_sprite"]
    player["py_3"]["hp_bar"] = "████████████████████"

def enemy_team(): #Complete Stat transfer for Enemy's PYthonMon when starting battle
    #1st PYthonMon info transfer
    enemy["py_1"]["name"] = pythonmon[(p_id_1)]["name"]
    enemy["py_1"]["base_hp"] = pythonmon[(p_id_1)]["base_hp"]
    enemy["py_1"]["base_atk"] = pythonmon[(p_id_1)]["base_atk"]
    enemy["py_1"]["base_def"] = pythonmon[(p_id_1)]["base_def"]
    enemy["py_1"]["base_spd"] = pythonmon[(p_id_1)]["base_spd"]
    enemy["py_1"]["base_spec"] = pythonmon[(p_id_1)]["base_spec"]
    enemy["py_1"]["move_1"] = pythonmon[(p_id_1)]["move_1"]
    enemy["py_1"]["move_2"] = pythonmon[(p_id_1)]["move_2"]
    enemy["py_1"]["move_3"] = pythonmon[(p_id_1)]["move_3"]
    enemy["py_1"]["move_4"] = pythonmon[(p_id_1)]["move_4"]
    enemy["py_1"]["f_sprite"] = pythonmon[(p_id_1)]["f_sprite"]
    enemy["py_1"]["b_sprite"] = pythonmon[(p_id_1)]["b_sprite"]
    enemy["py_1"]["hp_bar"] = "████████████████████"

    #2nd PYthonMon info transfer
    enemy["py_2"]["name"] = pythonmon[(p_id_2)]["name"]
    enemy["py_2"]["base_hp"] = pythonmon[(p_id_2)]["base_hp"]
    enemy["py_2"]["base_atk"] = pythonmon[(p_id_2)]["base_atk"]
    enemy["py_2"]["base_def"] = pythonmon[(p_id_2)]["base_def"]
    enemy["py_2"]["base_spd"] = pythonmon[(p_id_2)]["base_spd"]
    enemy["py_2"]["base_spec"] = pythonmon[(p_id_2)]["base_spec"]
    enemy["py_2"]["move_1"] = pythonmon[(p_id_2)]["move_1"]
    enemy["py_2"]["move_2"] = pythonmon[(p_id_2)]["move_2"]
    enemy["py_2"]["move_3"] = pythonmon[(p_id_2)]["move_3"]
    enemy["py_2"]["move_4"] = pythonmon[(p_id_2)]["move_4"]
    enemy["py_2"]["f_sprite"] = pythonmon[(p_id_2)]["f_sprite"]
    enemy["py_2"]["b_sprite"] = pythonmon[(p_id_2)]["b_sprite"]
    enemy["py_2"]["hp_bar"] = "████████████████████"

    #3rd PYthonMon info transfer
    enemy["py_3"]["name"] = pythonmon[(p_id_3)]["name"]
    enemy["py_3"]["base_hp"] = pythonmon[(p_id_3)]["base_hp"]
    enemy["py_3"]["base_atk"] = pythonmon[(p_id_3)]["base_atk"]
    enemy["py_3"]["base_def"] = pythonmon[(p_id_3)]["base_def"]
    enemy["py_3"]["base_spd"] = pythonmon[(p_id_3)]["base_spd"]
    enemy["py_3"]["base_spec"] = pythonmon[(p_id_3)]["base_spec"]
    enemy["py_3"]["move_1"] = pythonmon[(p_id_3)]["move_1"]
    enemy["py_3"]["move_2"] = pythonmon[(p_id_3)]["move_2"]
    enemy["py_3"]["move_3"] = pythonmon[(p_id_3)]["move_3"]
    enemy["py_3"]["move_4"] = pythonmon[(p_id_3)]["move_4"]
    enemy["py_3"]["f_sprite"] = pythonmon[(p_id_3)]["f_sprite"]
    enemy["py_3"]["b_sprite"] = pythonmon[(p_id_3)]["b_sprite"]
    enemy["py_3"]["hp_bar"] = "████████████████████"

def enemy_py_1_active(): #Makes the Enemy's 1st PYthonMon the Active PYthonMon for the Enemy
    enemy["py_active"]["name"] = enemy["py_1"]["name"]
    enemy["py_active"]["base_hp"] = enemy["py_1"]["base_hp"]
    enemy["py_active"]["base_atk"] = enemy["py_1"]["base_atk"]
    enemy["py_active"]["base_def"] = enemy["py_1"]["base_def"]
    enemy["py_active"]["base_spd"] = enemy["py_1"]["base_spd"]
    enemy["py_active"]["base_spec"] = enemy["py_1"]["base_spec"]
    enemy["py_active"]["move_1"] = enemy["py_1"]["move_1"]
    enemy["py_active"]["move_2"] = enemy["py_1"]["move_2"]
    enemy["py_active"]["move_3"] = enemy["py_1"]["move_3"]
    enemy["py_active"]["move_4"] = enemy["py_1"]["move_4"]
    enemy["py_active"]["f_sprite"] = enemy["py_1"]["f_sprite"]
    enemy["py_active"]["b_sprite"] = enemy["py_1"]["b_sprite"]
    enemy["py_active"]["hp_bar"] = enemy["py_1"]["hp_bar"]
    
def battle(): #The entire battle system
    clear()
    if difficulty.lower() == "normal":
        normal()
    else:
        hard()
    enemy_team()
    enemy_py_1_active()
    while True:
        action = input(f"{enemy["py_active"]["name"]}")

pythonmon = { #All Pythonmon info
    1: { #All Onion Frog info
        "name":
            "Onion Frog",
        "base_hp":
            45,
        "base_atk":
            49,
        "base_def":
            49,
        "base_spd":
            45,
        "base_spec":
            65,
        "type_1":
            "Grass",
        "type_2":
            "Poison",
        "weaknesses": {
            "Fire", "Ice", "Flying", "Psychic"},
        "resistances": {
            "Water", "Electric", "Grass", "Fighting"},
        "Immunities":
            "None",
        "move_1":
            "Vine Whip",
        "move_2":
            "Tackle",
        "move_3":
            "Sleep Powder",
        "move_4":
            "Poison Powder",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    2: { #All Fire Lizard info
        "name":
            "Fire Lizard",
        "base_hp":
            39,
        "base_atk":
            52,
        "base_def":
            43,
        "base_spd":
            65,
        "base_spec":
            50,
        "weaknesses": {
            "Water", "Ground", "Rock"},
        "resistances": {
            "Fire", "Grass", "Ice", "Bug"},
        "Immunities":
            "None",
        "move_1":
            "Ember",
        "move_2":
            "Scratch",
        "move_3":
            "Leer",
        "move_4":
            "Growl",
        "f_sprite":
            load_sprite("Sprites/f_2.txt"),
        "b_sprite":
            load_sprite("Sprites/b_2.txt")
    },
    3: { #All Tutel info
        "name":
            "Tutle",
        "base_hp":
            44,
        "base_atk":
            48,
        "base_def":
            65,
        "base_spd":
            43,
        "base_spec":
            50,
        "weaknesses": {
            "Electric", "Grass"},
        "resistances": {
            "Fire", "Water", "Ice"},
        "Immunities":
            "None",
        "move_1":
            "Water Gun",
        "move_2":
            "Tackle",
        "move_3":
            "Withdraw",
        "move_4":
            "Tail Whip",
        "f_sprite":
            load_sprite("Sprites/f_3.txt"),
        "b_sprite":
            load_sprite("Sprites/b_3.txt")
    },
    4: { #All Rat info
        "name":
            "Rat",
        "base_hp":
            30,
        "base_atk":
            56,
        "base_def":
            35,
        "base_spd":
            72,
        "base_spec":
            25,
        "weaknesses":
            "Fighting",
        "resistances":
            "None",
        "Immunities":
            "Ghost",
        "move_1":
            "Quick Attack",
        "move_2":
            "Super Fang",
        "move_3":
            "Focus Energy",
        "move_4":
            "Tail Whip",
        "f_sprite":
            load_sprite("Sprites/f_4.txt"),
        "b_sprite":
            load_sprite("Sprites/b_4.txt")
    },
    5: { #All Lightning Mouse info
        "name":
            "Lightning Mouse",
        "base_hp":
            35,
        "base_atk":
            55,
        "base_def":
            30,
        "base_spd":
            90,
        "base_spec":
            50,
        "weaknesses":
            "Ground",
        "resistances": {
            "Electric", "Flying"},
        "Immunities":
            "None",
        "move_1":
            "Thunder Shock",
        "move_2":
            "Quick Attack",
        "move_3":
            "Growl",
        "move_4":
            "Thunder Wave",
        "f_sprite":
            load_sprite("Sprites/f_5.txt"),
        "b_sprite":
            load_sprite("Sprites/b_5.txt")
    },
    6: { #All Birb info
        "name":
            "Birb",
        "base_hp":
            40,
        "base_atk":
            45,
        "base_def":
            40,
        "base_spd":
            56,
        "base_spec":
            35,
        "weaknesses": {
            "Electric", "Ice", "Rock"},
        "resistances": {
            "Grass", "Bug"},
        "Immunities": {
            "Ground", "Ghost"},
        "move_1":
            "Wing Attack",
        "move_2":
            "Quick Attack",
        "move_3":
            "Sand-Attack",
        "move_4":
            "Agility",
        "f_sprite":
            load_sprite("Sprites/f_6.txt"),
        "b_sprite":
            load_sprite("Sprites/b_6.txt")
    }
}

player = { #All Player & their PYthonMon info
    "py_1": { #All 1st PYthonMon info (Player)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_2": { #All 2nd PYthonMon info (Player)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_3": { #All 3rd PYthonMon info (Player)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_active": { #All PYthonMon (currently in battle) info (Player)
        "name":
            "---",
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "inv": { #Inventory slot names & quantity
        "slot_1":
            "---",
        "slot_num":
            0,
        "slot_2":
            "---",
        "slot_num":
            0,
        "slot_3":
            "---",
        "slot_num":
            0,
        "slot_4":
            "---",
        "slot_4_num":
            0,
        "slot_5":
            "---",
        "slot_5_num":
            0,
        "slot_6":
            "---",
        "slot_6_num":
            0,
        "slot_7":
            "---",
        "slot_7_num":
            0,
        "slot_8":
            "---",
        "slot_8_num":
            0,
        "slot_9":
            "---",
        "slot_9_num":
            0,
        "slot_10":
            "---",
        "slot_10_num":
            0
    },
    "player": { #All other info for the Player (Name,money,badges,level cap)
        "name":
            "---",
        "floor":
            0,
        "money":
            0,
        "badges":
            0,
        "lv_cap":
            10
    }
}

enemy = { #All Enemy & their PYthonMon info
    "py_1": { #All 1st PYthonMon info (Enemy)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "xp_given":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_2": { #All 2nd PYthonMon info (Enemy)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "xp_given":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_3": { #All 3rd PYthonMon info (Enemy)
        "name":
            "---",
        "base_hp":
            0,
        "base_atk":
            0,
        "base_def":
            0,
        "base_spd":
            0,
        "base_spec":
            0,
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp":
            0,
        "next_lv":
            0,
        "xp_given":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    },
    "py_active": { #All PYthonMon (currently in battle) info (Enemy)
        "name":
            "---",
        "hp":
            0,
        "max_hp":
            0,
        "atk":
            0,
        "def":
            0,
        "spd":
            0,
        "spec":
            0,
        "move_1":
            "---",
        "move_2":
            "---",
        "move_3":
            "---",
        "move_4":
            "---",
        "lv":
            0,
        "xp_given":
            0,
        "hp_bar":
            "░░░░░░░░░░░░░░░░░░░░",
        "f_sprite":
            load_sprite("Sprites/f_1.txt"),
        "b_sprite":
            load_sprite("Sprites/b_1.txt")
    }
}

moves = { #All Moves in the game and all info on the Moves
    "Vine Whip": { #Move 01
        "base_power":
            45,
        "accuracy":
            100,
        "effect_1":
            "None",
        "chance_1":
            0,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Grass"
    },
    "Tackle": { #Move 02
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "None",
        "chance_1":
            0,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Sleep Powder": { #Move 03
        "base_power":
            0,
        "accuracy":
            75,
        "effect_1":
            "Sleep",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Grass"
    },
    "Poison Powder": { #Move 04
        "base_power":
            0,
        "accuracy":
            75,
        "effect_1":
            "Poison",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Poison"
    },
    "Ember": { #Move 05
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "Burn",
        "chance_1":
            20,
        "effect_2":
            "None",
        "chance_1":
            0,
        "type":
            "Fire"
    },
    "Scratch": { #Move 06
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "None",
        "chance_1":
            0,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Leer": { #Move 07
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "DEF-",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Growl": { #Move 08
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "ATK-",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Water Gun": { #Move 09
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "None",
        "chance_1":
            0,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Water"
    },
    "Withdraw": { #Move 10
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "DEF+",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Water"
    },
    "Tail Whip": { #Move 11
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "DEF-",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Quick Attack": { #Move 12
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "Priority",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Super Fang": { #Move 13
        "base_power":
            0,
        "accuracy":
            90,
        "effect_1":
            "Half",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Focus Energy": { #Move 14
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "CRIT+",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Normal"
    },
    "Thunder Shock": { #Move 15
        "base_power":
            40,
        "accuracy":
            100,
        "effect_1":
            "Paralyze",
        "chance_1":
            20,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Electric"
    },
    "Thunder Wave": { #Move 16
        "base_power":
            0,
        "accuracy":
            90,
        "effect_1":
            "Paralyze",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Electric"
    },
    "Wing Attack": { #Move 17
        "base_power":
            60,
        "accuracy":
            100,
        "effect_1":
            "None",
        "chance_1":
            0,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Flying"
    },
    "Sand-Attack": { #Move 18
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "ACC-",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Ground"
    },
    "Agility": { #Move 19
        "base_power":
            0,
        "accuracy":
            100,
        "effect_1":
            "SPE+",
        "chance_1":
            100,
        "effect_2":
            "None",
        "chance_2":
            0,
        "type":
            "Pyschic"
    }
}

clear()

print_slow("\nThis game is not affiliated with Nintendo or The Pokémon Company and is only used for educational purposes.")

time.sleep(3)
clear()

print_sprite("Sprites/c_1.txt")

time.sleep(2)
clear()

print_sprite("Sprites/c_2.txt")
    
time.sleep(2)
clear()

print_sprite("Sprites/c_3.txt")
    
time.sleep(2)
clear()

print_sprite("Sprites/c_4.txt")
    
time.sleep(2)
clear()

print_sprite("Sprites/PYthonMon Title (Black).txt")
   
time.sleep(3)
clear()

print_sprite("Sprites/PYthonMon Title.txt")
input(" ")

while True:
    clear()
    print(pythonmon[1]["weaknesses"])
    print_slow("""What difficulty will you choose?
[Normal] [Hard]

--->""")
    difficulty = input(" ")
    if difficulty.lower() != "normal" and "hard":
        print_slow("\nInvalid difficulty. Please select again.")
        time.sleep(3)
    else:
        break

normal()
player_starters()

while True:
    clear()
    p_id_1 = 1
    print(f"""{player["py_1"]["f_sprite"]}

Name: {player["py_1"]["name"]}
Move 1: {player["py_1"]["move_1"]}
Move 2: {player["py_1"]["move_2"]}
Move 3: {player["py_1"]["move_3"]}
Move 4: {player["py_1"]["move_4"]}""")
    print_slow("\n\nThis is your starter. Are you ok with it?")
    choice = input("""\n1: Yes
2: No (Refresh starters)

---> """)
    if choice == "1":
        break
    elif choice == "2":
        print_slow("\nRandomising!")
        time.sleep(3)
        normal()
        player_starters()
    else:
        print_slow("\nInvalid choice. Select again.")
        time.sleep(3)
battle()
