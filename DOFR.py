import sys,os,time,random
from colorama import init
init() #This is so that sys clear can work in CMD

def print_slow(str): #Prints out text slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def print_slow2(str): #Prints out text slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def clear(): #Clears all text on screen
    os.system('cls' if os.name == 'nt' else 'clear')

MAPS = {
    "r_1": [
        "### ####################",
        "#......#...............#",
        "#......#......T........#",
        "#..N...#...............#",
        "#......######.##########",
        "#......................#",
        "#.###########..........#",
        "#...........#..........#",
        "###########/############",
    ],
    "r_2": [
        "########################",
        "#.......T.......#......#",
        "#...............#...N..#",
        "#...............#......#",
        "/...................... ",
        "#...######......#......#",
        "#...#.T..#......#......#",
        "#...#...........#......#",
        "### ####################",
    ],
    "r_3": [
        "#################",
        "#.....T.N.T.....#",
        "#............... ",
        "#...............#",
        "#################",
    ],
    "r_4": [
        "########### ############",
        "#........##.####.......#",
        "#.######.##.####.#####.#",
        "#.######....####.#...#.#",
        "#.##############.#.#.#.#",
        "#................#.#...#",
        "##################.#####",
        "###########........#####",
        "###########/############",
    ],
    "r_5": [
        "########### ############",
        "#...#.....#.....#......#",
        "#.#.#.###.#####.#.####.#",
        "#.#...###.....#...####.#",
        "#.###########.########.#",
        "#...........#..........#",
        "###########.############",
        "###########.############",
        "###########/############",
    ],
}

WARPS = {
    ("r_1", 0, 3): ("r_2", 7, 3),
    ("r_2", 8, 3): ("r_1", 1, 3),
    ("r_2", 4, 0): ("r_3", 2, 15),
    ("r_3", 2, 16): ("r_2", 4, 1),
    ("r_1", 8, 11): ("r_4", 1, 11),
    ("r_4", 0, 11): ("r_1", 7, 11),
    ("r_4", 8, 11): ("r_5", 1, 11),
    ("r_5", 0, 11): ("r_4", 7, 11),
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

for key, rows in MAPS.items():
    MAPS[key] = [list(row) for row in rows]

def find_start(game_map):
    #Fail save if the player is stuck in a wall
    for r,row in enumerate(game_map):
        for c,ch in enumerate(row):
            if ch == ".":
                return r,c
    return 1,1

def draw(game_map, player_pos, messages=None):
    clear()
    r0,c0 = player_pos
    for r,row in enumerate(game_map):
        line = ""
        for c,ch in enumerate(row):
            if (r,c) == (r0,c0):
                line += "@"
            else:
                line += ch
        print(line)
    if messages:
        print("\n" + "\n".join(messages[-4:]))

def can_move(game_map, r,c):
    if r < 0 or c < 0 or r >= len(game_map) or c >= len(game_map[0]):
        return False
    return game_map[r][c] in ("."," ")#Walkable tiles

def interact_at(game_map, r,c, messages):
    ch = game_map[r][c]
    if ch == "T":
        messages.append("You found a treasure!")
        game_map[r][c] = "."
        if current_map == "r_2":
            if "---" in player["other"]["inv"]:
                player["other"]["inv"][player["other"]["inv"].index("---")] = "Bomb"
    elif ch == "N":
        if current_map == "r_1":
            messages.append("NPC: 'A hero! Wait you're a rogue? Boring...'")
        elif current_map == "r_2":
            messages.append("NPC: '67.'")
        elif current_map == "r_3":
            messages.append("NPC: 'You found the secret too?!'")
    if ch == "/":
        messages.append("A cracked wall. Seems breakable...")
        if "Bomb" in player["other"]["inv"]:
            messages.append("Use Bomb? [Y/N]")
            draw(game_map, (player_r, player_c), messages)
            choice_map = input("--> ")
            if choice_map.lower() == "y":
                messages.append(f"{player["hero"]["name"]} blew up the wall.")
                game_map[r][c] = " "
                del player["other"]["inv"][player["other"]["inv"].index("Bomb")]
                player["other"]["inv"].append("---")
            else:
                messages.append("You decided to ignore it.")
        
def main():
    global current_map, game_map, player_r, player_c, enemies, e_num, hp_bar, mp_stars, hp_bar_enemy, idx, choice_item, player, items, heal_hp_player, heal_mp_player
    player_r, player_c = 7,19
    messages = ["Use WASD to move, E to interact, Q to use items and check stats."]

    while True:
        draw(game_map, (player_r, player_c), messages)
        choice_map = input("--> ").strip().lower()
        if not choice_map:
            continue
        if choice_map in ("w","a","s","d"):
            dr = {"w":-1,"s":1,"a":0,"d":0}[choice_map]
            dc = {"w":0,"s":0,"a":-1,"d":1}[choice_map]
            nr, nc = player_r + dr, player_c + dc
            if can_move(game_map, nr, nc):
                player_r, player_c = nr, nc
                if (current_map, nr, nc) in WARPS:
                    dest_map, dest_r, dest_c = WARPS[(current_map, nr, nc)]
                    current_map = dest_map
                    game_map = MAPS[current_map]
                    player_r, player_c = dest_r, dest_c
                    continue
                if random.randint(1,100) <= 0:
                    print_slow("\n(!) BATTLE START!")
                    time.sleep(3)
                    e_num = random.randint(1,1)
                    enemies["enemy"]["name"] = enemies[e_num]["name"]
                    enemies["enemy"]["hp"] = enemies[e_num]["hp"]
                    enemies["enemy"]["maxhp"] = enemies[e_num]["maxhp"]
                    enemies["enemy"]["mp"] = enemies[e_num]["mp"]
                    enemies["enemy"]["maxmp"] = enemies[e_num]["maxmp"]
                    enemies["enemy"]["atk"] = enemies[e_num]["atk"]
                    enemies["enemy"]["def"] = enemies[e_num]["def"]
                    enemies["enemy"]["magic"] = enemies[e_num]["magic"]
                    enemies["enemy"]["spells"] = enemies[e_num]["spells"]
                    enemies["enemy"]["xp_given"] = enemies[e_num]["xp_given"]
                    enemies["enemy"]["ascii"] = enemies[e_num]["ascii"]
                    hp_bar(player), mp_stars(player), hp_bar_enemy(enemies)
                    battle(player, enemies, damage_player, damage_enemy, heal_hp_player, mp_deplete_player, heal_hp_enemy, spells, defend_player, defend_enemy, run, enemy_choice)
            else:
                messages.append("You bump into something.")
        elif choice_map == "e":
            interacted = False
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = player_r+dr, player_c+dc
                if 0 <= nr < len(game_map) and 0 <= nc < len(game_map[0]):
                    if game_map[nr][nc] in ("T", "N", "/"):
                        interact_at(game_map, nr, nc, messages)
                        interacted = True
                        break
            if not interacted:
                messages.append("You see nothing to interact with.")
        elif choice_map == "q":
            clear()
            hp_bar(player), mp_stars(player)
            print(f"""{player["hero"]["name"]} LV: {player["other"]["lv"]}
HP: {player["other"]["hp_bar"]} {player["hero"]["hp"]} / {player["hero"]["maxhp"]}
MP: {player["other"]["mp_stars"]}
ATK: {player["hero"]["atk"]} DEF: {player["hero"]["def"]} MAGIC: {player["hero"]["magic"]}
XP: {player["other"]["xp"]}
XP needed for next LV: {player["other"]["next_lv"]}
 ____________________________________
¦
¦ 1: [{player["other"]["inv"][0]}]
¦ 2: [{player["other"]["inv"][1]}]
¦ 3: [{player["other"]["inv"][2]}]
¦ 4: [{player["other"]["inv"][3]}]
¦ 5: [{player["other"]["inv"][4]}]
¦ 6: [{player["other"]["inv"][5]}]
¦ 7: [{player["other"]["inv"][6]}]
¦ 8: [{player["other"]["inv"][7]}]
¦____________________________________

What item will you use?
Press enter to go back.""")
            choice_item = input("\n--> ")
            if choice_item.strip() == "":
                continue
            try:
                idx = int(choice_item) - 1
            except ValueError:
                print_slow("\nInvalid choice. Please select again.")
                time.sleep(1)
                clear()
                continue
            if player["other"]["inv"][idx] == "---":
                print_slow("\nThere is no item in that slot.")
                time.sleep(1)
                continue
            if player["other"]["inv"][idx] != "---":
                if items[player["other"]["inv"][idx]]["type"] == "Health": #Healing HP
                    heal_hp_player = items[player["other"]["inv"][idx]]["recovery"]
                    print_slow(f"\n{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
                    player["hero"]["hp"] += heal_hp_player
                    if player["hero"]["hp"] >= player["hero"]["maxhp"]:
                        player["hero"]["hp"] = player["hero"]["maxhp"]
                        print_slow(f"\nRecovered All HP.")
                    else:
                        print_slow(f"\nRecovered {heal_hp_player} HP.")
                    heal_hp_player = 0
                    del player["other"]["inv"][idx]
                    player["other"]["inv"].append("---")
                    time.sleep(1)
                elif items[player["other"]["inv"][idx]]["type"] == "MP": #Healing MP
                    heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
                    print_slow(f"\n{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
                    player["hero"]["mp"] += heal_mp_player
                    if player["hero"]["mp"] >= player["hero"]["maxmp"]:
                        player["hero"]["mp"] = player["hero"]["maxmp"]
                        print_slow(f"\nRecovered All MP.")
                    else:
                        print_slow(f"\nRecovered {heal_mp_player} MP.")
                    heal_mp_player = 0
                    del player["other"]["inv"][idx]
                    player["other"]["inv"].append("---")
                    time.sleep(1)
                elif items[player["other"]["inv"][idx]]["type"] == "Health and MP": #Healing both HP and MP
                    heal_hp_player = heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
                    print_slow(f"\n{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
                    player["hero"]["hp"] += heal_hp_player
                    if player["hero"]["hp"] >= player["hero"]["maxhp"]:
                        player["hero"]["hp"] = player["hero"]["maxhp"]
                        print_slow(f"\nRecovered All HP ")
                    else:
                        print_slow(f"\nRecovered {heal_hp_player} HP ")
                    player["hero"]["mp"] += heal_mp_player
                    if player["hero"]["mp"] >= player["hero"]["maxmp"]:
                        player["hero"]["mp"] = player["hero"]["maxmp"]
                        print_slow(f"and All MP.")
                    else:
                        print_slow(f"and {heal_mp_player} MP.")
                    heal_hp_player = heal_mp_player = 0
                    del player["other"]["inv"][idx]
                    player["other"]["inv"].append("---")
                    time.sleep(1)
                elif items[player["other"]["inv"][idx]]["type"] == "Other": #Other
                    print_slow(f"""\n{player["hero"]["name"]} tried to used {player["other"]["inv"][idx]}.
But nothing happened.""")
                    time.sleep(1)
        else:
            messages.append("Unknown command. Use WASD/E/Q.")

def load_ascii(filename): #Loads ASCII/ASCII text file
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def print_ascii(filename): #Prints out a ASCII/ASCII text file
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

def print_frame(): #Prints Player's battle text file
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

def print_frame_2(): #Prints Enemy's battle text file
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
    if heal_hp_player != 0: #HP Recovery animation
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
        
    if heal_mp_player != 0: #MP Recovery animation
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
    
    if damage_player != 0: #HP going down animation
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

    if mp_deplete_player != 0: #MP going down animation
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
    if heal_hp_enemy != 0: #HP Recovery animation
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
    
    if damage_enemy != 0: #HP going down animation
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

def item_effects(idx, choice_item, player, items, heal_hp_player, heal_mp_player): #All Items effects in play
    if player["other"]["inv"][idx] != "---":
        if items[player["other"]["inv"][idx]]["type"] == "Health": #Healing HP
            heal_hp_player = items[player["other"]["inv"][idx]]["recovery"]
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["hero"]["hp"] == player["hero"]["maxhp"]:
                print_slow(f"\nRecovered All HP.")
            else:
                print_slow(f"\nRecovered {heal_hp_player} HP.")
            heal_hp_player = 0
            del player["other"]["inv"][idx]
            player["other"]["inv"].append("---")
            time.sleep(1)
        elif items[player["other"]["inv"][idx]]["type"] == "MP": #Healing MP
            heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["hero"]["mp"] == player["hero"]["maxmp"]:
                print_slow(f"\nRecovered All MP.")
            else:
                print_slow(f"\nRecovered {heal_mp_player} MP.")
            heal_mp_player = 0
            del player["other"]["inv"][idx]
            player["other"]["inv"].append("---")
            time.sleep(1)
        elif items[player["other"]["inv"][idx]]["type"] == "Health and MP": #Healing both HP and MP
            heal_hp_player = heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{player["hero"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["hero"]["hp"] == player["hero"]["maxhp"]:
                print_slow(f"\nRecovered All HP ")
            else:
                print_slow(f"\nRecovered {heal_hp_player} HP ")
            if player["hero"]["mp"] == player["hero"]["maxmp"]:
                print_slow(f"and All MP.")
            else:
                print_slow(f"and {heal_mp_player} MP.")
            heal_hp_player = heal_mp_player = 0
            del player["other"]["inv"][idx]
            player["other"]["inv"].append("---")
            time.sleep(1)
        elif items[player["other"]["inv"][idx]]["type"] == "Other": #Other
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"""\n{player["hero"]["name"]} tried to used {player["other"]["inv"][idx]}.
But nothing happened.""")
            time.sleep(1)
            
def level_stats(player): #All stats going up when levelling up
    print_slow(f"""\n\nYou leveled up!
HP: {player["hero"]["maxhp"]} --> HP: {player["hero"]["maxhp"]+7}
MP: {player["hero"]["maxmp"]} --> MP: {player["hero"]["maxmp"]}
ATK: {player["hero"]["atk"]} --> ATK: {player["hero"]["atk"]+2}
DEF: {player["hero"]["def"]} --> DEF: {player["hero"]["def"]+1}
MAGIC: {player["hero"]["magic"]} --> MAGIC: {player["hero"]["magic"]+1}""")
    player["hero"]["maxhp"] += 7
    player["hero"]["hp"] = player["hero"]["maxhp"]
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

def battle(player, enemies, damage_player, damage_enemy, heal_hp_player, heal_hp_enemy, mp_deplete_player, spells, defend_player, defend_enemy, run, enemy_choice): #The entire battle system
    while True:
        while True:
            if defend_player == True:
                defend_player = False
                player["hero"]["def"] /= 1.5
                if player["hero"]["def"] % 1 == 0:
                    player["hero"]["def"] = int(player["hero"]["def"])
                else:
                    player["hero"]["def"] = round(player["hero"]["def"])
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
                    damage_enemy = 0
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
¦ 1: [{player["hero"]["spells"][0]}] Cost: [{spells[player["hero"]["spells"][0]]["cost"]} MP]
¦ 2: [{player["hero"]["spells"][1]}] Cost: [{spells[player["hero"]["spells"][1]]["cost"]} MP]
¦ 3: [{player["hero"]["spells"][2]}] Cost: [{spells[player["hero"]["spells"][2]]["cost"]} MP]
¦ 4: [{player["hero"]["spells"][3]}] Cost: [{spells[player["hero"]["spells"][3]]["cost"]} MP]
¦ 5: [{player["hero"]["spells"][4]}] Cost: [{spells[player["hero"]["spells"][4]]["cost"]} MP]
¦ 6: [{player["hero"]["spells"][5]}] Cost: [{spells[player["hero"]["spells"][5]]["cost"]} MP]
¦ 7: [{player["hero"]["spells"][6]}] Cost: [{spells[player["hero"]["spells"][6]]["cost"]} MP]
¦ 8: [{player["hero"]["spells"][7]}] Cost: [{spells[player["hero"]["spells"][7]]["cost"]} MP]
¦____________________________________

What spell will you use?
Press enter to go back.""")
                choice_magic = input("\n--> ")
                if choice_magic.strip() == "":
                    continue
                try:
                    idx = int(choice_magic) - 1
                except ValueError:
                    print_slow("\nInvalid choice. Please select again.")
                    time.sleep(1)
                    clear()
                    continue
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
                            if player["hero"]["hp"] == player["hero"]["maxhp"]:
                                print_slow(f"\nRecovered All HP.")
                            else:
                                print_slow(f"\nRecovered {heal_hp_player} HP.")
                            heal_hp_player = mp_deplete_player = 0
                            time.sleep(1)
                            break
                        elif spells[player["hero"]["spells"][idx]]["type"] == "Damage":
                            damage_enemy = (player["hero"]["magic"] * spells[player["hero"]["spells"][idx]]["multiplier"]) - (enemies["enemy"]["magic"] * 0.75)
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            mp_deplete_player = spells[player["hero"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["hero"]["name"]} casted {player["hero"]["spells"][idx]}!")
                            enemy_animation(heal_hp_enemy, damage_enemy)
                            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                            print_slow(f"\nDealt {damage_enemy} damage.")
                            damage_enemy = mp_deplete_player = 0
                            time.sleep(1)
                            break
                        elif spells[player["hero"]["spells"][idx]]["type"] == "Half":
                            damage_enemy = enemies["enemy"]["hp"] / 2
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            mp_deplete_player = spells[player["hero"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["hero"]["name"]} casted {player["hero"]["spells"][idx]}!")
                            enemy_animation(heal_hp_enemy, damage_enemy)
                            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                            print_slow(f"\nDealt {damage_enemy} damage.")
                            damage_enemy = mp_deplete_player = 0
                            time.sleep(1)
                            break
                    else:
                        print_slow("\nNot enough MP.")
                        time.sleep(1)
                        clear()
                else:
                    print_slow("\nYou do not know that spell.")
                    time.sleep(1)
                    clear()

            elif choice == "3":
                #PLAYER TURN [ITEM]
                clear()
                print(f"""
 ____________________________________
¦
¦ 1: [{player["other"]["inv"][0]}]
¦ 2: [{player["other"]["inv"][1]}]
¦ 3: [{player["other"]["inv"][2]}]
¦ 4: [{player["other"]["inv"][3]}]
¦ 5: [{player["other"]["inv"][4]}]
¦ 6: [{player["other"]["inv"][5]}]
¦ 7: [{player["other"]["inv"][6]}]
¦ 8: [{player["other"]["inv"][7]}]
¦____________________________________

What item will you use?
Press enter to go back.""")
                choice_item = input("\n--> ")
                if choice_item.strip() == "":
                    continue
                try:
                    idx = int(choice_item) - 1
                except ValueError:
                    print_slow("\nInvalid choice. Please select again.")
                    time.sleep(1)
                    clear()
                    continue
                if player["other"]["inv"][idx] == "---":
                    print_slow("\nThere is no item in that slot.")
                    time.sleep(1)
                    continue
                item_effects(idx, choice_item, player, items, heal_hp_player, heal_mp_player)
                break

            elif choice == "4":
                #PLAYER TURN [DEFEND]
                clear()
                print_frame_2()
                print_frame()
                defend_player = True
                player["hero"]["def"] *= 1.5
                if player["hero"]["def"] % 1 == 0:
                    player["hero"]["def"] = int(player["hero"]["def"])
                else:
                    player["hero"]["def"] = round(player["hero"]["def"])
                print_slow(f"{player["hero"]["name"]} defended.")
                time.sleep(1)
                break

            elif choice == "5":
                #PLAYER TURN [RUN]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{player["hero"]["name"]} tried to run")
                print_slow2("...")
                if random.randint(1,100) >= 75:
                    run = True
                    print_slow("\nAnd did!")
                    time.sleep(1)
                    break
                else:
                    print_slow("\nAnd failed!")
                    time.sleep(1)
                    break
        if run == True:
            run = False
            break

        if enemies["enemy"]["hp"] != 0:
            #ENEMY TURN
            if enemies["enemy"]["spells"] != "None":
                enemy_choice = random.randint(1,2)
            else:
                enemy_choice = 1
            if enemy_choice == 1:
                #ENEMY TURN [FIGHT]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{enemies[1]["name"]} attacks!")
                if random.randint(1,100) > 5:
                    if random.randint(1,100) <= 15:
                        print_slow(" CRITICAL HIT!!")
                        damage_player = (enemies[1]["atk"] - (player["hero"]["def"]/2)) * 1.5
                    else:
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
                    damage_player = 0
                    time.sleep(1)
                else:
                    print_slow(" Missed!")
                    time.sleep(1)
            elif enemy_choice == 2:
                #ENEMY TURN [MAGIC]
                clear()
                print_frame_2()
                print_frame()
                if spells[enemies["enemy"]["spells"]]["type"] == "Heal":
                    heal_hp_enemy = enemies["enemy"]["maxhp"] * spells[enemies["enemy"]["spell"]]["multiplier"]
                    if heal_hp_enemy % 1 == 0:
                        heal_hp_enemy = int(heal_hp_enemy)
                    else:
                        heal_hp_enemy = round(heal_hp_enemy)
                    clear()
                    print_frame_2()
                    print_frame()
                    print_slow(f"{enemies["enemy"]["name"]} casted {enemies["enemy"]["spells"]}!")
                    enemy_animation(heal_hp_player, damage_player)
                    if enemies["enemy"]["hp"] == enemies["enemy"]["maxhp"]:
                        print_slow(f"\nRecovered All HP.")
                    else:
                        print_slow(f"\nRecovered {heal_hp_enemy} HP.")
                    heal_hp_enemy = 0
                    time.sleep(1)
                elif spells[enemies["enemy"]["spells"]]["type"] == "Damage":
                    damage_player = (enemies["enemy"]["magic"] * spells[player["hero"]["spells"][idx]]["multiplier"]) - (enemies["enemy"]["magic"] * 0.75)
                    if damage_player % 1 == 0:
                        damage_player = int(damage_player)
                    else:
                        damage_player = round(damage_player)
                    clear()
                    print_frame_2()
                    print_frame()
                    print_slow(f"{enemies["enemy"]["name"]} casted {enemies["enemy"]["spells"]}!")
                    player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                    print_slow(f"\nDealt {damage_player} damage.")
                    damage_player = 0
                    time.sleep(1)
                elif spells[enemies["enemy"]["spells"]]["type"] == "Half":
                    damage_player = player["hero"]["hp"] / 2
                    if damage_player % 1 == 0:
                        damage_player = int(damage_player)
                    else:
                        damage_player = round(damage_player)
                    clear()
                    print_frame_2()
                    print_frame()
                    print_slow(f"{enemies["enemy"]["name"]} casted {enemies["enemy"]["spells"]}!")
                    player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                    print_slow(f"\nDealt {damage_player} damage.")
                    damage_player = 0
                    time.sleep(1)
                
        if enemies["enemy"]["hp"] == 0:
            clear()
            
            enemies["enemy"]["name"] = " "
            enemies["enemy"]["ascii"] = load_ascii("ascii/empty.txt")
            
            print_frame_2()
            print_frame()
            
            print_slow(f"""YOU WIN!
You got {enemies["enemy"]["xp_given"]} XP!""")
            player["other"]["xp"] += enemies["enemy"]["xp_given"]
            player["other"]["next_lv"] -= enemies["enemy"]["xp_given"]
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
            1,
        "magic":
            4,
        "spells":
            ["Heal","Fireball","Split","---","---","---","---","---"]
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
            ["Jelly Juice","Green Tea","Golden Juice","---","---","---","---","---"],
        "ascii":
            load_ascii("ascii/player.txt")
    }
}

enemies = { #All enemy info
    1: { #All Slime info
        "name":
            "Slime",
        "hp":
            15,
        "maxhp":
            15,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            5,
        "def":
            0,
        "magic":
            3,
        "spells":
            "None",
        "xp_given":
            1,
        "gold_given":
            1,
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
            4,
        "def":
            0,
        "magic":
            4,
        "spells":
            "Split",
        "xp_given":
            1,
        "gold_given":
            1,
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
        "spells":
            " ",
        "xp_given":
            0,
        "gold_given":
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
            0,
        "type":
            "Damage",
        "multiplier":
            9999999999
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
    "Split": { #All Drain info
        "cost":
            5,
        "type":
            "Half",
        "multiplier":
            0
    }
}

items = { #All Item info
    "---": { #Placeholder info
        "recovery":
            9999999999,
        "type":
            "Health and MP"
    },
    "Jelly Juice": { #All Jelly Juice info
        "recovery":
            20,
        "type":
            "Health"
    },
    "Green Tea": { #All Green Tea info
        "recovery":
            1,
        "type":
            "MP"
    },
    "Golden Juice": { #All Golden Juice info
        "recovery":
            9999999999,
        "type":
            "Health and MP"
    },
    "Bomb": { #All Bomb info
        "recovery":
            0,
        "type":
            "Other"
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
defend_player = False
defend_enemy = False
run = False
enemy_choice = 0
e_num = 0

current_map = "r_1"
game_map = MAPS[current_map]
player_r, player_c = 7, 19
main()
