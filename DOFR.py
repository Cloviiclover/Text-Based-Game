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

def print_frame():
    ascii_lines = player["other"]["ascii"].split("\n")
    num_lines = len(ascii_lines)
    
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

def print_frame_2():
    ascii_lines_2 = enemies["enemy"]["ascii"].split("\n")
    num_lines_2 = len(ascii_lines_2)

    for line in ascii_lines_2:
        sys.stdout.write("\033[2K")
        sys.stdout.write(line.format(
            enemy_name=enemies["enemy"]["name"],
            enemy_hp_bar=enemies["enemy"]["hp_bar"]
        ) + "\n")
    sys.stdout.flush()

def player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player): #Animation for Player's HP, HP bar, and MP stars
    ascii_lines = player["other"]["ascii"].split("\n")
    num_lines = len(ascii_lines)
    ascii_lines_2 = enemies[1]["ascii"].split("\n")
    num_lines_2 = len(ascii_lines_2)
    if heal_hp_player != 0:
        for _ in range(heal_hp_player):
            player["hero"]["hp"] += 1
            if player["hero"]["hp"] > player["hero"]["maxhp"]:
                player["hero"]["hp"] = player["hero"]["maxhp"]
                break

            hp_bar(player)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.1)

    if heal_mp_player != 0:
        for _ in range(heal_mp_player):
            player["hero"]["mp"] += 1
            if player["hero"]["mp"] > player["hero"]["maxmp"]:
                player["hero"]["mp"] = player["hero"]["maxmp"]
                break

            mp_stars(player)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.2)
    
    if damage_player != 0:
        for _ in range(damage_player):
            player["hero"]["hp"] -= 1
            if player["hero"]["hp"] < 0:
                player["hero"]["hp"] = 0
                break

            hp_bar(player)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.1)

    if mp_deplete_player != 0:
        for _ in range(mp_deplete_player):
            player["hero"]["mp"] -= 1

            mp_stars(player)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.2)

def enemy_animation(heal_hp_enemy, damage_enemy): #Animation for Enemy's HP bar
    ascii_lines = player["other"]["ascii"].split("\n")
    num_lines = len(ascii_lines)
    ascii_lines_2 = enemies[1]["ascii"].split("\n")
    num_lines_2 = len(ascii_lines_2)
    if heal_hp_enemy != 0:
        for _ in range(heal_hp_enemy):
            enemies["enemy"]["hp"] += 1
            if enemies["enemy"]["hp"] > enemies["enemy"]["maxhp"]:
                enemies["enemy"]["hp"] = enemies["enemy"]["maxhp"]
                break

            hp_bar_enemy(enemies)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.1)
    
    if damage_enemy != 0:
        for _ in range(damage_enemy):
            enemies["enemy"]["hp"] -= 1
            if enemies["enemy"]["hp"] < 0:
                enemies["enemy"]["hp"] = 0
                break

            hp_bar_enemy(enemies)

            sys.stdout.write(f"\033[{num_lines_2}F")
            sys.stdout.flush()
            
            sys.stdout.write(f"\033[{num_lines}F")
            sys.stdout.flush()

            print_frame_2()
            print_frame()
            time.sleep(0.1)

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

def hp_bar_enemy(enemies): #HP bar generation for the Enemy
    max_bars = 20
    hp = max(enemies["enemy"]["hp"], 0)
    maxhp = enemies["enemy"]["maxhp"]

    percent = hp / maxhp
    if percent < 1 and percent > 0.94:
        percent = 0.95
    elif percent <= 0.05 and percent > 0:
        percent = 0.05
    filled_bars = round(percent * max_bars)

    bar = "█" * filled_bars + "░" * (max_bars - filled_bars)
    enemies["enemy"]["hp_bar"] = bar

def mp_stars(player): #MP stars generation
    if player["hero"]["maxmp"] != 0:
        player["other"]["mp_stars"] = "*" * player["hero"]["mp"]
    else:
        player["other"]["mp_stars"] = "LOCKED"

def battle(player, enemies, damage_player, damage_enemy, heal_hp_player, heal_hp_enemy, mp_deplete_player, spells): #The entire battle system
    while True:
        while True:
            #RESETING THESE SO THEY DON'T OVERLAP IN EFFECT
            damage_player = 0
            damage_enemy = 0
            heal_hp_player = 0
            heal_hp_enemy = 0
            mp_deplete_player = 0
            clear()
            print_frame_2()
            print_frame()
            choice = input("""[1: FIGHT] [2: MAGIC] [3: ITEM] [4: DEFEND] [5: RUN]

--> """)
            if choice == "1":
                #PLAYER TURN [ATTACK]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{player["hero"]["name"]} attacks!")
                if random.randint(1,100) > 5:
                    if random.randint(1,100) <= 15:
                        print_slow(" CRITICAL HIT!!")
                        damage_enemy = (player["hero"]["atk"] - (enemies["enemy"]["def"]/2)) * 1.5
                    else:
                        damage_enemy = player["hero"]["atk"] - (enemies["enemy"]["def"]/2)
                    if damage_enemy % 1 == 0:
                        damage_enemy = int(damage_enemy)
                    else:
                        damage_enemy = round(damage_enemy)
                    damage_enemy += random.randint(-2,4)
                    if damage_enemy <= 0:
                        damage_enemy = 1
                    enemy_animation(heal_hp_enemy, damage_enemy)
                    print_slow(f"\nDealt {damage_enemy} damage.")
                    time.sleep(1)
                    break
                else:
                    print_slow(" Missed!")
                    time.sleep(1)
                    break
            elif choice == "2":
                #PLAYER TURN [MAGIC]
                clear()
                print(f"""
 ____________________________________
¦
¦ 1: [{player["hero"]["spells"][0]}] Cost: [{spells[player["hero"]["spells"][0]]["cost"]}]
¦ 2: [{player["hero"]["spells"][1]}] Cost: [{spells[player["hero"]["spells"][1]]["cost"]}]
¦ 3: [{player["hero"]["spells"][2]}] Cost: [{spells[player["hero"]["spells"][2]]["cost"]}]
¦ 4: [{player["hero"]["spells"][3]}] Cost: [{spells[player["hero"]["spells"][3]]["cost"]}]
¦ 5: [{player["hero"]["spells"][4]}] Cost: [{spells[player["hero"]["spells"][4]]["cost"]}]
¦ 6: [{player["hero"]["spells"][5]}] Cost: [{spells[player["hero"]["spells"][5]]["cost"]}]
¦ 7: [{player["hero"]["spells"][6]}] Cost: [{spells[player["hero"]["spells"][6]]["cost"]}]
¦ 8: [{player["hero"]["spells"][7]}] Cost: [{spells[player["hero"]["spells"][7]]["cost"]}]
¦____________________________________

What spell do you choose?
Press enter to go back.""")
                choice = input("\n--> ")
                idx = int(choice) - 1
                if player["hero"]["spells"][idx] != "---":
                    if player["hero"]["mp"] - spells[player["hero"]["spells"][idx]]["cost"] >= 0:
                        if spells[player["hero"]["spells"][idx]]["type"] == "Heal":
                            heal_hp_player = player["hero"]["maxhp"] * spells[player["hero"]["spells"][idx]]["multiplier"]
                            if heal_hp_player % 1 == 0:
                                heal_hp_player = int(heal_hp_player)
                            else:
                                heal_hp_player = round(heal_hp_player)
                            mp_deplete_player = spells[player["hero"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["hero"]["name"]} casted {player["hero"]["spells"][idx]}!")
                            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                            print_slow(f"\nHealed {heal_hp_player} HP.")
                            break
                        elif spells[player["hero"]["spells"][idx]]["type"] == "Damage":
                            damage_enemy = max(1, (player["hero"]["magic"] * spells[player["hero"]["spells"][idx]]["multiplier"]) - (enemies["enemy"]["magic"] * 0.75))
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            break
                        elif spells[player["hero"]["spells"][idx]]["type"] == "Half":
                            damage_enemy = enemies["enemy"]["hp"] / 2
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            break
                    else:
                        print_slow("\nNot enough MP.")
                        time.sleep(1)
                        clear()
                else:
                    print_slow("\nYou do not know that spell.")
                    time.sleep(1)
                    clear()
                
        #ENEMY TURN [FOR NOW]
        if enemies["enemy"]["hp"] != 0:
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{enemies[1]["name"]} attacks!")
            damage_player = enemies[1]["atk"] - (player["hero"]["def"]/2)
            if damage_player % 1 == 0:
                damage_player = int(damage_player)
            else:
                damage_player = round(damage_player)
            damage_player += random.randint(-2,4)
            if damage_player <= 0:
                damage_player = 1
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            print_slow(f"\nDealt {damage_player} damage.")
            time.sleep(1)
        if enemies["enemy"]["hp"] == 0:
            clear()
            
            enemies["enemy"]["name"] = " "
            enemies["enemy"]["ascii"] = load_ascii("ascii/empty.txt")
            battle_loop = False
            
            print_frame_2()
            print_frame()
            
            print_slow("YOU WIN!")
            time.sleep(2)
            break
        elif player["hero"]["hp"] == 0:
            print_slow(f"\n{player["hero"]["name"]} took mortal damage and died.")
            time.sleep(1)
            clear()
            print_ascii("ascii/game_over.txt")
            time.sleep(5)
            sys.exit(0)

player = { #All Player info
    "hero": { #All Hero info
        "name":
            "HERO",
        "hp":
            50,
        "maxhp":
            50,
        "mp":
            5,
        "maxmp":
            5,
        "atk":
            5,
        "def":
            0,
        "magic":
            2,
        "spells":
            ["Heal","---","---","---","---","---","---","---"]
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
        "inv":
            ["---","---","---","---","---","---","---","---"],
        "ascii":
            load_ascii("ascii/player.txt")
    }
}

enemies = { #All enemy info
    1: { #All Slime info
        "name":
            "Slime",
        "hp":
            150,
        "maxhp":
            150,
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
            "Bat",
        "hp":
            20,
        "maxhp":
            20,
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
    "enemy": { #All active enemy info
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
    "---": { #Placeholder info
        "cost":
            "?",
        "type":
            "?",
        "multiplier":
            "?"
    },
    "Heal": { #All Heal info
        "cost":
            1,
        "type":
            "Heal",
        "multiplier":
            0.33
    },
    "Fireball": { #All Fireball info
        "cost":
            2,
        "type":
            "Damage",
        "multiplier":
            2
    },
    "Drain": { #All Drain info
        "cost":
            3,
        "type":
            "Half",
        "multiplier":
            0
    }
}

damage_player = 0
mp_deplete_player = 0
heal_hp_player = 0
heal_mp_player = 0
damage_enemy = 0
mp_deplete_enemy = 0
heal_hp_enemy = 0
heal_mp_enemy = 0
hp_bar(player)
mp_stars(player)
enemies["enemy"]["name"] = enemies[1]["name"]
enemies["enemy"]["hp"] = enemies[1]["hp"]
enemies["enemy"]["maxhp"] = enemies[1]["maxhp"]
enemies["enemy"]["mp"] = enemies[1]["mp"]
enemies["enemy"]["maxmp"] = enemies[1]["maxmp"]
enemies["enemy"]["atk"] = enemies[1]["atk"]
enemies["enemy"]["def"] = enemies[1]["def"]
enemies["enemy"]["magic"] = enemies[1]["magic"]
enemies["enemy"]["ascii"] = enemies[1]["ascii"]
hp_bar_enemy(enemies)
battle(player, enemies, damage_player, damage_enemy, heal_hp_player, mp_deplete_player, heal_hp_enemy, spells)
