import sys,os,time,random
from colorama import init
init() #This is so that sys clear can work in CMD

def print_slow(str): #Prints out text slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def clear(): #Clears all text on screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_ascii(filename): #Loads ASCII/ASCII text file
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def print_ascii(filename): #Prints out a ASCII/ASCII text file
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

def deplete_player(damage_player, mp_deplete): #Delpeting animation for Player's HP, HP bar, and MP stars
    ascii_lines = player["other"]["ascii"].split("\n")
    num_lines = len(ascii_lines)

    def print_frame():
        for line in ascii_lines:
            sys.stdout.write("\033[2K")
            sys.stdout.write(line.format(
                player_name=player["hero"]["name"],
                player_lv=player["other"]["lv"],
                player_hp_bar=player["other"]["hp_bar"],
                player_hp=player["hero"]["hp"],
                player_maxhp=player["hero"]["maxhp"],
                player_mp_stars=player["other"]["mp_stars"]
            ) + "\n")
        sys.stdout.flush()

    if damage_player != 0:
        for _ in range(damage_player):
            player["hero"]["hp"] -= 1
            if player["hero"]["hp"] < 0:
                player["hero"]["hp"] = 0
                break

            hp_bar(player)

            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame()
            time.sleep(0.05)

    if mp_deplete != 0:
        for _ in range(mp_deplete):
            player["hero"]["mp"] -= 1

            mp_stars(player)

            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame()
            time.sleep(0.2)

#def spells(player,spells): #All spell effects
    #if choice == "1":
        #if player["hero"]["mp"] - spells[player["hero"]["spells"][0]]["cost"] >= 0:
            #if spells[player["hero"]["spells"][0]]["type"] == "Heal":
                #
            #elif spells[player["hero"]["spells"][0]]["type"] == "Damage":
                #
            #elif spells[player["hero"]["spells"][0]]["type"] == "Half":
                #
        #else:
            #print_slow("\nNot enough MP.")
            #time.sleep(1)

def level_stats(player): #All stats going up when levelling up
    print_slow(f"""\n\nYou leveled up!
HP: {player["hero"]["maxhp"]} --> HP: {player["hero"]["maxhp"]+2}
MP: {player["hero"]["maxmp"]} --> MP: {player["hero"]["maxmp"]+1}
ATK: {player["hero"]["atk"]} --> ATK: {player["hero"]["atk"]+2}
DEF: {player["hero"]["def"]} --> DEF: {player["hero"]["def"]+1}
MAGIC: {player["hero"]["magic"]} --> MAGIC: {player["hero"]["magic"]+1}""")
    player["hero"]["maxhp"] += 2
    player["hero"]["hp"] = player["hero"]["maxhp"]
    player["hero"]["maxmp"] += 1
    player["hero"]["mp"] = player["hero"]["maxmp"]
    player["hero"]["atk"] += 2
    player["hero"]["def"] += 1
    player["hero"]["magic"] += 1

def level_system(player): #The entire levelling system for all levels
    if player["other"]["xp"] >= 10 and player["other"]["xp"] < 30: #LEVEL 2
        level_stats()
        player["other"]["next_lv"] += 20
    elif player["other"]["xp"] >= 30 and player["other"]["xp"] < 50: #LEVEL 3
        level_stats()
        player["other"]["next_lv"] += 40
    elif player["other"]["xp"] >= 70 and player["other"]["xp"] < 120: #LEVEL 4
        level_stats()
        player["other"]["next_lv"] += 50
    elif player["other"]["xp"] >= 120 and player["other"]["xp"] < 200: #LEVEL 5
        level_stats()
        player["other"]["next_lv"] += 80
    elif player["other"]["xp"] >= 200 and player["other"]["xp"] < 999999999999: #LEVEL 6
        level_stats()
        player["other"]["next_lv"] += 999999999999 #THIS IS BECAUSE THIS IS MAX SO FAR

def hp_bar(player): #HP bar generation
    max_bars = 20
    hp = max(player["hero"]["hp"], 0)
    maxhp = player["hero"]["maxhp"]

    percent = hp / maxhp
    if percent < 1 and percent > 0.94:
        percent = 0.95
    elif percent <= 0.05 and percent > 0:
        percent = 0.05
    filled_bars = round(percent * max_bars)

    bar = "█" * filled_bars + "░" * (max_bars - filled_bars)
    player["other"]["hp_bar"] = bar

def mp_stars(player): #MP stars generation
    if player["hero"]["maxmp"] != 0:
        player["other"]["mp_stars"] = "*" * player["hero"]["mp"]
    else:
        player["other"]["mp_stars"] = "LOCKED"

#def battle(): #The entire battle system
    

player = { #All Player info
    "hero": { #All Hero info
        "name":
            "HERO",
        "hp":
            761,
        "maxhp":
            761,
        "mp":
            20,
        "maxmp":
            20,
        "atk":
            5,
        "def":
            0,
        "magic":
            0,
        "spells":
            []      
    },
    "other": { #Other stats
        "weapon":
            "Basic Short Sword",
        "shield":
            "Basic Shield",
        "acc_1":
            "None",
        "acc_2":
            "None",
        "acc_3":
            "None",
        "weapon_atk":
            1,
        "shield_def":
            1,
        "acc_1_def":
            0,
        "acc_2_def":
            0,
        "acc_3_def":
            0,
        "hp_bar":
            " ",
        "mp_stars":
            " ",
        "lv":
            1,
        "xp":
            0,
        "next_lv":
            10,
        "gold":
            0,
        "battle_num":
            0,
        "ascii":
            load_ascii("ascii/player.txt")
    }
}

enemies = { #All enemy info
    1: { #All Slime info
        "name":
            "Slime",
        "hp":
            20,
        "maxhp":
            20,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            4,
        "def":
            0,
        "magic":
            10,
        "ascii":
            load_ascii("ascii/slime.txt")
    },
    2: { #All Bat info
        "name":
            "Slime",
        "hp":
            15,
        "maxhp":
            15,
        "mp":
            10,
        "maxmp":
            10,
        "atk":
            3,
        "def":
            0,
        "magic":
            8,
        "ascii":
            load_ascii("ascii/bat.txt")
    },
    "enemy_1": { #All active enemy info (1st enemy)
        "name":
            " ",
        "hp":
            0,
        "maxhp":
            0,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            0,
        "def":
            0,
        "magic":
            0,
        "hp_bar":
            " ",
        "ascii":
            " "
    },
    "enemy_2": { #All active enemy info (2nd enemy)
        "name":
            " ",
        "hp":
            0,
        "maxhp":
            0,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            0,
        "def":
            0,
        "magic":
            0,
        "hp_bar":
            " ",
        "ascii":
            " "
    }
}

spells = { #All Spell info
    "Heal": { #All Heal info
        "cost":
            1,
        "type":
            "Heal",
        "multipler":
            0.33
    },
    "Fireball": { #All Fireball info
        "cost":
            2,
        "type":
            "Damage",
        "multipler":
            2
    },
    "Drain": { #All Drain info
        "cost":
            3,
        "type":
            "Half",
        "multipler":
            0
    }
}

damage_player = 0
mp_deplete = 0
hp_bar(player)
mp_stars(player)
input("test")
deplete_player(damage_player,mp_deplete)
