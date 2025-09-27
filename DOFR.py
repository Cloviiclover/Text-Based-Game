import sys,os,time,random
from colorama import init
init() #This is so that sys clear can work in terminal/os/whatever and so no issues happen

def print_slow(str): #Prints out text slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def print_slow2(str): #Prints out text slowly (but faster)
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def clear(): #Clears all text on screen
    os.system('cls' if os.name == 'nt' else 'clear')


MAPS = { #All maps/rooms in the game
    "o_1": [
        "################# #################",
        "#.........#.............#.........#",
        "#.........#..N..........#.........#",
        "#.........#.....#.#.....#.........#",
        "#......##.#######.#######.##......#",
        "#......#T.#.............#..#......#",
        "#......####.............####......#",
        "#.................................#",
        "#.................................#",
        "#.................................#",
        "#.................................#",
        "#.................................#",
        "#.................................#",
        "#.........#.............#.........#",
        "#.........#.............#.........#",
        "#.........#.............#.........#",
        "#.........####### #######.........#",
        "#.........###############.........#",
        "#.........#S   H   O   P#.........#",
        "###################################",
    ],
    "o_2": [
        "######## ########",
        "#...............#",
        "#.######N######.#",
        "#.#...........#.#",
        "###TTTTTTTTTTT###",
    ],
    "r_1": [
        "### ####################",
        "#......#...............#",
        "#......#......T........#",
        "#..N...#...............#",
        "#......######.##########",
        "#......................#",
        "#.###########..........#",
        "#...........#..........#",
        "###########/####### ####",
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
        "#.......N.......#",
        "#.T............. ",
        "#...............#",
        "#################",
    ],
    "r_4": [
        "########### ############",
        "#........##...D........ ",
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
    "r_6": [
        "################ #######",
        "#.T.#.....#............#",
        "#.........#............#",
        "#####.....#####...######",
        " ......................#",
        "#####..............#...#",
        "#..................#...#",
        "#.N.#..............#.T.#",
        "########################",
    ],
    "r_7": [
        "########### ############",
        "#......................#",
        "#.......N..............D",
        "#......................#",
        "###########B############",
        "#......................#",
        "#.....T....T....T......#",
        "#......................#",
        "########################",
    ],
    "r_8": [
        "#### ####",
        "#.......#",
        " .......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#########",
    ],
    "r_9": [
        "#### ####",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "#### ####",
    ],
    "r_10": [
        "#########",
        " .......#",
        "#.......#",
        "#.......#",
        "####D####",
        "#.......#",
        "#.......#",
        "#.......#",
        "#### ####",
    ]
}

WARPS = {
    ("o_1", 16, 17): ("o_2", 1, 8),
    ("o_2", 0, 8): ("o_1", 15, 17),
    ("o_1", 0, 17): ("r_1", 7, 19),
    ("r_1", 8, 19): ("o_1", 1, 17),
    ("r_1", 0, 3): ("r_2", 7, 3),
    ("r_2", 8, 3): ("r_1", 1, 3),
    ("r_2", 4, 0): ("r_3", 2, 15),
    ("r_3", 2, 16): ("r_2", 4, 1),
    ("r_1", 8, 11): ("r_4", 1, 11),
    ("r_4", 0, 11): ("r_1", 7, 11),
    ("r_4", 8, 11): ("r_5", 1, 11),
    ("r_5", 0, 11): ("r_4", 7, 11),
    ("r_2", 4, 23): ("r_6", 4, 1),
    ("r_6", 4, 0): ("r_2", 4, 22),
    ("r_5", 8, 11): ("r_7", 1, 11),
    ("r_7", 0, 11): ("r_5", 7, 11),
    ("r_4", 1, 23): ("r_10", 1, 1),
    ("r_10", 1, 0): ("r_4", 1, 22),
    ("r_10", 8, 4): ("r_9", 1, 4),
    ("r_9", 0, 4): ("r_10", 7, 4),
    ("r_9", 8, 4): ("r_8", 1, 4),
    ("r_8", 0, 4): ("r_9", 7, 4),
    ("r_8", 2, 0): ("r_7", 2, 22),
    ("r_7", 2, 23): ("r_8", 2, 1),
}

for key, rows in MAPS.items():
    MAPS[key] = [list(row) for row in rows]

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
        if current_map == "o_1":
            if "---" in player["other"]["inv"]:
                messages.append("You found a treasure!")
                player["other"]["inv"][player["other"]["inv"].index("---")] = "Escape Orb"
                game_map[r][c] = "."
            else:
                messages.append("You don't have any space.")
        elif current_map == "o_2":
            if "---" in player["other"]["inv"]:
                messages.append("You found a treasure!")
                player["other"]["inv"][player["other"]["inv"].index("---")] = "Escape Orb"
                game_map[r][c] = "."
            else:
                messages.append("You don't have any space.")
        elif current_map == "r_2":
            if "---" in player["other"]["inv"]:
                messages.append("You found a treasure!")
                player["other"]["inv"][player["other"]["inv"].index("---")] = "Bomb"
                game_map[r][c] = "."
            else:
                messages.append("You don't have any space.")
        elif current_map == "r_1" or current_map == "r_6":
            if "---" in player["other"]["inv"]:
                messages.append("You found a treasure!")
                loot = random.randint(1,4)
                if loot == 1:
                    player["other"]["inv"][player["other"]["inv"].index("---")] = "Jelly Juice"
                    game_map[r][c] = "."
                elif loot == 2:
                    player["other"]["inv"][player["other"]["inv"].index("---")] = "Green Tea"
                    game_map[r][c] = "."
                elif loot == 3:
                    player["other"]["inv"][player["other"]["inv"].index("---")] = "Escape Orb"
                    game_map[r][c] = "."
                elif loot == 4:
                    player["other"]["inv"][player["other"]["inv"].index("---")] = "Bomb"
                    game_map[r][c] = "."
            else:
                messages.append("You don't have any space.")
        elif current_map == "r_3" or current_map == "r_7":
            if "---" in player["other"]["inv"]:
                messages.append("You found a treasure!")
                player["other"]["inv"][player["other"]["inv"].index("---")] = "Golden Juice"
                game_map[r][c] = "."
            else:
                messages.append("You don't have any space.")
    elif ch == "N":
        if current_map == "o_1":
            messages.append("NPC: 'This dungeon appeared out of nowhere.'")
        elif current_map == "o_2":
            while True:
                clear()
                print(f"""Welcome to the shop what do you want?
 ____________________________________
¦
¦ GOLD: {player["other"]["gold"]}G
¦
¦ 1: [Jelly Juice] [10G]
¦ 2: [Green Tea] [8G]
¦ 3: [Bomb] [20G]
¦ 4: [Escape Orb] [15G]
¦
¦ SELL: Sell items you have for GOLD
¦ STEAL: Steal an item
¦____________________________________

What item will you buy?
Press enter to go back.""")
                choice_shop = input("\n--> ")
                if choice_shop.strip() == "":
                    break
                try:
                    if choice_shop == "1":
                        if player["other"]["gold"] >= 10:
                            if "---" in player["other"]["inv"]:
                                print_slow("\nYou bought Jelly Juice!")
                                player["other"]["inv"][player["other"]["inv"].index("---")] = "Jelly Juice"
                                player["other"]["gold"] -= 10
                                time.sleep(1)
                            else:
                                print_slow("\nYou don't have any space.")
                                time.sleep(1)
                                continue
                        else:
                            print_slow("\nYou don't have enough GOLD.")
                            time.sleep(1)
                            continue
                    elif choice_shop == "2":
                        if player["other"]["gold"] >= 8:
                            if "---" in player["other"]["inv"]:
                                print_slow("\nYou bought Green Tea!")
                                player["other"]["inv"][player["other"]["inv"].index("---")] = "Green Tea"
                                player["other"]["gold"] -= 8
                                time.sleep(1)
                            else:
                                print_slow("\nYou don't have any space.")
                                time.sleep(1)
                                continue
                        else:
                            print_slow("\nYou don't have enough GOLD.")
                            time.sleep(1)
                            continue
                    elif choice_shop == "3":
                        if player["other"]["gold"] >= 20:
                            if "---" in player["other"]["inv"]:
                                print_slow("\nYou bought Bomb!")
                                player["other"]["inv"][player["other"]["inv"].index("---")] = "Bomb"
                                player["other"]["gold"] -= 20
                                time.sleep(1)
                            else:
                                print_slow("\nYou don't have any space.")
                                time.sleep(1)
                                continue
                        else:
                            print_slow("\nYou don't have enough GOLD.")
                            time.sleep(1)
                            continue
                    elif choice_shop == "4":
                        if player["other"]["gold"] >= 15:
                            if "---" in player["other"]["inv"]:
                                print_slow("\nYou bought Escape Orb!")
                                player["other"]["inv"][player["other"]["inv"].index("---")] = "Escape Orb"
                                player["other"]["gold"] -= 15
                                time.sleep(1)
                            else:
                                print_slow("\nYou don't have any space.")
                                time.sleep(1)
                                continue
                        else:
                            print_slow("\nYou don't have enough GOLD.")
                            time.sleep(1)
                            continue
                    elif choice_shop.lower() == "steal":
                        if steal_player == 0:
                            print_slow("Hey! No stealing allowed.")
                            time.sleep(1)
                            steal_player += 1
                        elif steal_player == 1:
                            print_slow("I'm being serious... No stealing allowed!")
                            time.sleep(1)
                            steal_player += 1
                        elif steal_player == 2:
                            print_slow("Fine try and steal and you'll be punished")
                            time.sleep(1)
                            steal_player += 1
                        elif steal_player == 3:
                            clear()
                            print(f"""...
 ____________________________________
¦
¦ GOLD: {player["other"]["gold"]}G
¦
¦ 1: [Jelly Juice] [STEAL]
¦ 2: [Green Tea] [STEAL]
¦ 3: [Bomb] [STEAL]
¦ 4: [Escape Orb] [STEAL]
¦____________________________________

What item will you buy?
Press enter to go back.""")
                        choice_steal = input("\n--> ")
                            if choice_shop.strip() == "":
                                break
                            try:
                                if choice_shop == "1":
                                    if "---" in player["other"]["inv"]:
                                        print_slow("\nYou bought Jelly Juice!")
                                        player["other"]["inv"][player["other"]["inv"].index("---")] = "Jelly Juice"
                                        time.sleep(1)
                                    else:
                                        print_slow("\nYou don't have any space.")
                                        time.sleep(1)
                                        continue
                                elif choice_shop == "2":
                                    if "---" in player["other"]["inv"]:
                                        print_slow("\nYou bought Green Tea!")
                                        player["other"]["inv"][player["other"]["inv"].index("---")] = "Green Tea"
                                        time.sleep(1)
                                    else:
                                        print_slow("\nYou don't have any space.")
                                        time.sleep(1)
                                        continue
                                elif choice_shop == "3":
                                    if "---" in player["other"]["inv"]:
                                        print_slow("\nYou bought Bomb!")
                                        player["other"]["inv"][player["other"]["inv"].index("---")] = "Bomb"
                                        time.sleep(1)
                                    else:
                                        print_slow("\nYou don't have any space.")
                                        time.sleep(1)
                                        continue
                                else:
                                    print_slow("\nYou don't have enough GOLD.")
                                    time.sleep(1)
                                    continue
                            elif choice_shop == "4":
                                if player["other"]["gold"] >= 15:
                                    if "---" in player["other"]["inv"]:
                                        print_slow("\nYou bought Escape Orb!")
                                        player["other"]["inv"][player["other"]["inv"].index("---")] = "Escape Orb"
                                        player["other"]["gold"] -= 15
                                        time.sleep(1)
                                    else:
                                        print_slow("\nYou don't have any space.")
                                        time.sleep(1)
                                        continue
                                else:
                                    print_slow("\nYou don't have enough GOLD.")
                                    time.sleep(1)
                                    continue
                    elif choice_shop.lower() == "sell":
                        clear()
                        print(f"""Sure I'll buy stuff from you!
 ____________________________________
¦
¦ GOLD: {player["other"]["gold"]}G
¦
¦ 1: [{player["other"]["inv"][0]}] [{items[player["other"]["inv"][0]]["sell"]}G]
¦ 2: [{player["other"]["inv"][1]}] [{items[player["other"]["inv"][1]]["sell"]}G]
¦ 3: [{player["other"]["inv"][2]}] [{items[player["other"]["inv"][2]]["sell"]}G]
¦ 4: [{player["other"]["inv"][3]}] [{items[player["other"]["inv"][3]]["sell"]}G]
¦ 5: [{player["other"]["inv"][4]}] [{items[player["other"]["inv"][4]]["sell"]}G]
¦ 6: [{player["other"]["inv"][5]}] [{items[player["other"]["inv"][5]]["sell"]}G]
¦ 7: [{player["other"]["inv"][6]}] [{items[player["other"]["inv"][6]]["sell"]}G]
¦ 8: [{player["other"]["inv"][7]}] [{items[player["other"]["inv"][7]]["sell"]}G]
¦____________________________________

What item will you sell?
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
                        if idx < 0 or idx >= len(player["other"]["inv"]):
                            print_slow("\nInvalid choice. Please select again.")
                            time.sleep(1)
                            clear()
                            continue
                        if player["other"]["inv"][idx] == "---":
                            print_slow("\nThere is no item in that slot.")
                            time.sleep(1)
                            continue
                        if choice_item.strip() == "":
                            continue
                        print_slow(f"\nYou sold {player["other"]["inv"][idx]} and got {items[player["other"]["inv"][idx]]["sell"]} GOLD!")
                        player["other"]["gold"] += items[player["other"]["inv"][idx]]["sell"]
                        del player["other"]["inv"][idx]
                        player["other"]["inv"].append("---")
                        time.sleep(1)
                except ValueError:
                    print_slow("\nInvalid choice. Please select again.")
                    time.sleep(1)
                    clear()
                    continue
        elif current_map == "r_1":
            messages.append("NPC: 'A hero! Wait you're a rogue? Boring...'")
        elif current_map == "r_2":
            messages.append("NPC: 'It feels like the deeper you explore")
            messages.append("the dungeon the less people there are.'")
        elif current_map == "r_3":
            messages.append("NPC: 'You found the secret too?!'")
        elif current_map == "r_6":
            messages.append("NPC: 'Many heroes explore the dungeon")
            messages.append("and never come back.'")
        elif current_map == "r_7":
            messages.append("NPC: 'I don't need this anymore. Take it!'")
            player["other"]["key_inv"][player["other"]["key_inv"].index("---")] = "Leader's Key"
            messages.append("You got the Leader's Key!")
    elif ch == "/":
        messages.append("A cracked wall. Seems breakable...")
        if "Bomb" in player["other"]["inv"]:
            messages.append("Use Bomb? [Y/N]")
            draw(game_map, (player_r, player_c), messages)
            choice_map = input("--> ")
            if choice_map.lower() == "y":
                messages.append(f"{player["rogue"]["name"]} blew up the wall.")
                game_map[r][c] = " "
                del player["other"]["inv"][player["other"]["inv"].index("Bomb")]
                player["other"]["inv"].append("---")
            else:
                messages.append("You decided to ignore it.")
    elif ch == "D":
        messages.append("A locked door. Needs some kind of key.")
        if "Leader's Key" in player["other"]["key_inv"]:
            messages.append("Use Leader's Key? [Y/N]")
            draw(game_map, (player_r, player_c), messages)
            choice_map = input("--> ")
            if choice_map.lower() == "y":
                messages.append(f"{player["rogue"]["name"]} unlocked the door.")
                if current_map == "r_4" or current_map == "r_10":
                    game_map[r][c] = "."
                elif current_map != "r_4" or current_map != "r_10":
                    game_map[r][c] = " "
            else:
                messages.append("You decided to ignore it.")
    elif ch == "B":
        if current_map == "r_7":
            messages.append("BOSS: 'WHY DID YOU COME HERE? DIE!'")
            draw(game_map, (player_r, player_c), messages)
            time.sleep(2)
            print_slow("\n(!) BATTLE START!")
            time.sleep(3)
            idx = 0
            enemies["enemy"]["name"] = enemies[2]["name"]
            enemies["enemy"]["hp"] = enemies[2]["hp"]
            enemies["enemy"]["maxhp"] = enemies[2]["maxhp"]
            enemies["enemy"]["mp"] = enemies[2]["mp"]
            enemies["enemy"]["maxmp"] = enemies[2]["maxmp"]
            enemies["enemy"]["atk"] = enemies[2]["atk"]
            enemies["enemy"]["def"] = enemies[2]["def"]
            enemies["enemy"]["magic"] = enemies[2]["magic"]
            enemies["enemy"]["spells"] = enemies[2]["spells"]
            enemies["enemy"]["xp_given"] = enemies[2]["xp_given"]
            enemies["enemy"]["gold_given"] = enemies[2]["gold_given"]
            enemies["enemy"]["ascii"] = enemies[2]["ascii"]
            hp_bar(player), mp_stars(player), hp_bar_enemy(enemies)
            battle(charge_player, charge_enemy, player, enemies, damage_player, damage_enemy, heal_hp_player, heal_hp_enemy, mp_deplete_player, spells, defend_player, defend_enemy, run, enemy_choice, level_system, idx, items) #The entire battle system
            charge_player = False
            charge_enemy = False
        if enemies["enemy"]["hp"] <= 0:
            game_map[r][c] = "."
        
def overworld():
    global mp_recovery, current_map, game_map, player_r, player_c, enemies, e_num, hp_bar, mp_stars, hp_bar_enemy, idx, choice_item, player, items, heal_hp_player, heal_mp_player
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
                if random.randint(1,100) <= 3 and current_map != "o_1" and current_map != "o_2":
                    draw(game_map, (player_r, player_c), messages)
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
                    enemies["enemy"]["gold_given"] = enemies[e_num]["gold_given"]
                    enemies["enemy"]["ascii"] = enemies[e_num]["ascii"]
                    hp_bar(player), mp_stars(player), hp_bar_enemy(enemies)
                    mp_recovery = 0
                    battle(mp_recovery, player, enemies, damage_player, damage_enemy, heal_hp_player, heal_hp_enemy, mp_deplete_player, spells, defend_player, defend_enemy, run, enemy_choice, level_system, idx, items) #The entire battle system
            else:
                messages.append("You bump into something.")
        elif choice_map == "e":
            interacted = False
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = player_r+dr, player_c+dc
                if 0 <= nr < len(game_map) and 0 <= nc < len(game_map[0]):
                    if game_map[nr][nc] in ("T", "N", "/", "B", "D"):
                        interact_at(game_map, nr, nc, messages)
                        interacted = True
                        break
            if not interacted:
                messages.append("You see nothing to interact with.")
        elif choice_map == "q":
            clear()
            hp_bar(player), mp_stars(player)
            print(f"""{player["rogue"]["name"]} LV: {player["other"]["lv"]}
HP: {player["other"]["hp_bar"]} {player["rogue"]["hp"]} / {player["rogue"]["maxhp"]}
MP: {player["other"]["mp_stars"]} {player["rogue"]["mp"]} / {player["rogue"]["maxmp"]}
ATK: {player["rogue"]["atk"]} DEF: {player["rogue"]["def"]} MAGIC: {player["rogue"]["magic"]}
XP: {player["other"]["xp"]}
XP needed for next LV: {player["other"]["next_lv"]}
GOLD: {player["other"]["gold"]}G
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
¦
¦ 9: Key items inventory
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
            if idx == 8:
                print(f"""
 ____________________________________
¦
¦ 1: [{player["other"]["key_inv"][0]}]
¦ 2: [{player["other"]["key_inv"][1]}]
¦ 3: [{player["other"]["key_inv"][2]}]
¦ 4: [{player["other"]["key_inv"][3]}]
¦ 5: [{player["other"]["key_inv"][4]}]
¦ 6: [{player["other"]["key_inv"][5]}]
¦ 7: [{player["other"]["key_inv"][6]}]
¦ 8: [{player["other"]["key_inv"][7]}]
¦____________________________________

Press enter to go back.""")
                input("\n--> ")
                continue
            if idx < 0 or idx >= len(player["other"]["inv"]):
                print_slow("\nInvalid choice. Please select again.")
                time.sleep(1)
                clear()
                continue
            if player["other"]["inv"][idx] == "---":
                print_slow("\nThere is no item in that slot.")
                time.sleep(1)
                continue
            clear()
            print(f"""
 ____________________________________
¦
¦ [{player["other"]["inv"][idx]}]
¦____________________________________

[1: Use Item] [2: Info] [3: Throw Away]
Press enter to go back.""")
            choice_item = input("\n--> ")
            if choice_item.strip() == "":
                continue
            if choice_item == "1":
                if player["other"]["inv"][idx] != "---":
                    if items[player["other"]["inv"][idx]]["type"] == "Health": #Healing HP
                        heal_hp_player = items[player["other"]["inv"][idx]]["recovery"]
                        print_slow(f"\n{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
                        player["rogue"]["hp"] += heal_hp_player
                        if player["rogue"]["hp"] >= player["rogue"]["maxhp"]:
                            player["rogue"]["hp"] = player["rogue"]["maxhp"]
                            print_slow(f"\nRecovered All HP.")
                        else:
                            print_slow(f"\nRecovered {heal_hp_player} HP.")
                        heal_hp_player = 0
                        del player["other"]["inv"][idx]
                        player["other"]["inv"].append("---")
                        time.sleep(1)
                    elif items[player["other"]["inv"][idx]]["type"] == "MP": #Healing MP
                        heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
                        print_slow(f"\n{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
                        player["rogue"]["mp"] += heal_mp_player
                        if player["rogue"]["mp"] >= player["rogue"]["maxmp"]:
                            player["rogue"]["mp"] = player["rogue"]["maxmp"]
                            print_slow(f"\nRecovered All MP.")
                        else:
                            print_slow(f"\nRecovered {heal_mp_player} MP.")
                        heal_mp_player = 0
                        del player["other"]["inv"][idx]
                        player["other"]["inv"].append("---")
                        time.sleep(1)
                    elif items[player["other"]["inv"][idx]]["type"] == "Health and MP": #Healing both HP and MP
                        heal_hp_player = heal_mp_player = items[player["other"]["inv"][idx]]["recovery"]
                        print_slow(f"\n{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
                        player["rogue"]["hp"] += heal_hp_player
                        if player["rogue"]["hp"] >= player["rogue"]["maxhp"]:
                            player["rogue"]["hp"] = player["rogue"]["maxhp"]
                            print_slow(f"\nRecovered All HP ")
                        else:
                            print_slow(f"\nRecovered {heal_hp_player} HP ")
                        player["rogue"]["mp"] += heal_mp_player
                        if player["rogue"]["mp"] >= player["rogue"]["maxmp"]:
                            player["rogue"]["mp"] = player["rogue"]["maxmp"]
                            print_slow(f"and All MP.")
                        else:
                            print_slow(f"and {heal_mp_player} MP.")
                        heal_hp_player = heal_mp_player = 0
                        del player["other"]["inv"][idx]
                        player["other"]["inv"].append("---")
                        time.sleep(1)
                    elif items[player["other"]["inv"][idx]]["type"] == "Other" or items[player["other"]["inv"][idx]]["type"] == "Explosive": #Other & Explosive
                        print_slow(f"""\n{player["rogue"]["name"]} tried to use {player["other"]["inv"][idx]}.
But nothing happened.""")
                        time.sleep(1)
                    elif items[player["other"]["inv"][idx]]["type"] == "Escape": #Escape (Teleport to Overworld)
                        print_slow(f"\n{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
                        del player["other"]["inv"][idx]
                        player["other"]["inv"].append("---")
                        current_map = "o_1"
                        game_map = MAPS[current_map]
                        player_r, player_c = 10, 17
                        time.sleep(1)
            elif choice_item == "2":
                print_slow(f"\n{items[player["other"]["inv"][idx]]["info"]}")
                time.sleep(1)
            elif choice_item == "3":
                print_slow(f"\nThrow {player["other"]["inv"][idx]} away? [Y/N]")
                choice_map = input("\n\n--> ")
                if choice_map.lower() == "y":
                    print_slow(f"\n{player["rogue"]["name"]} threw {player["other"]["inv"][idx]} away.")
                    del player["other"]["inv"][idx]
                    player["other"]["inv"].append("---")
                else:
                    print_slow("\nYou decide to not do that.")
                time.sleep(1)
            else:
                print_slow("\nInvalid choice. Please select again.")
                time.sleep(1)
                clear()
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
            player_name=player["rogue"]["name"],
            player_lv=player["other"]["lv"],
            player_hp_bar=player["other"]["hp_bar"],
            player_hp=player["rogue"]["hp"],
            player_maxhp=player["rogue"]["maxhp"],
            player_mp_stars=player["other"]["mp_stars"],
            player_mp=player["rogue"]["mp"],
            player_maxmp=player["rogue"]["maxmp"]
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
            player["rogue"]["hp"] += 1
            if player["rogue"]["hp"] > player["rogue"]["maxhp"]:
                player["rogue"]["hp"] = player["rogue"]["maxhp"]
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
            player["rogue"]["mp"] += 1
            if player["rogue"]["mp"] > player["rogue"]["maxmp"]:
                player["rogue"]["mp"] = player["rogue"]["maxmp"]
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
            player["rogue"]["hp"] -= 1
            if player["rogue"]["hp"] < 0:
                player["rogue"]["hp"] = 0
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
            player["rogue"]["mp"] -= 1

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

def item_effects(damage_enemy, enemy_animation, idx, choice_item, player, items, heal_hp_player, heal_mp_player): #All Items effects in play
    if player["other"]["inv"][idx] != "---":
        if items[player["other"]["inv"][idx]]["type"] == "Health": #Healing HP
            heal_hp_player = items[player["other"]["inv"][idx]]["recovery"]
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["rogue"]["hp"] == player["rogue"]["maxhp"]:
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
            print_slow(f"{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["rogue"]["mp"] == player["rogue"]["maxmp"]:
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
            print_slow(f"{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
            if player["rogue"]["hp"] == player["rogue"]["maxhp"]:
                print_slow(f"\nRecovered All HP ")
            else:
                print_slow(f"\nRecovered {heal_hp_player} HP ")
            if player["rogue"]["mp"] == player["rogue"]["maxmp"]:
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
            print_slow(f"""\n{player["rogue"]["name"]} tried to used {player["other"]["inv"][idx]}.
But nothing happened.""")
            time.sleep(1)
        elif items[player["other"]["inv"][idx]]["type"] == "Escape": #Escape battle
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"""\n{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!
Escaped!""")
            time.sleep(1)
        elif items[player["other"]["inv"][idx]]["type"] == "Explosive": #Explosive
            clear()
            print_frame_2()
            print_frame()
            print_slow(f"{player["rogue"]["name"]} used {player["other"]["inv"][idx]}!")
            damage_enemy = 15
            enemy_animation(heal_hp_enemy, damage_enemy)
            print_slow(f"\nDealt {damage_enemy} damage.")
            damage_enemy = 0
            del player["other"]["inv"][idx]
            player["other"]["inv"].append("---")
            time.sleep(1)
            
def level_stats(player): #All stats going up when levelling up
    if player["other"]["lv"] < 99:
        print_slow(f"""\n\nYou leveled up!
LV: {player["other"]["lv"]} --> LV: {player["other"]["lv"]+1}
HP: {player["rogue"]["maxhp"]} --> HP: {player["rogue"]["maxhp"]+7}
MP: {player["rogue"]["maxmp"]} --> MP: {player["rogue"]["maxmp"]+2}
ATK: {player["rogue"]["atk"]} --> ATK: {player["rogue"]["atk"]+2}
DEF: {player["rogue"]["def"]} --> DEF: {player["rogue"]["def"]+1}
MAGIC: {player["rogue"]["magic"]} --> MAGIC: {player["rogue"]["magic"]+1}""")
        player["other"]["lv"] += 1
        player["rogue"]["maxhp"] += 7
        player["rogue"]["hp"] = player["rogue"]["maxhp"]
        player["rogue"]["maxmp"] += 2
        player["rogue"]["mp"] = player["rogue"]["maxmp"]
        player["rogue"]["atk"] += 2
        player["rogue"]["def"] += 1
        player["rogue"]["magic"] += 1
        player["other"]["next_lv"] += 10+(3*player["other"]["lv"])
    if player["other"]["lv"] == 99:
        print_slow(f"""\n\nYou leveled up!
LV: {player["other"]["lv"]} --> LV: {player["other"]["lv"]+1}
HP: {player["rogue"]["maxhp"]} --> HP: 999
MP: {player["rogue"]["maxmp"]} --> MP: {player["rogue"]["maxmp"]+2}
ATK: {player["rogue"]["atk"]} --> ATK: {player["rogue"]["atk"]+2}
DEF: {player["rogue"]["def"]} --> DEF: {player["rogue"]["def"]+1}
MAGIC: {player["rogue"]["magic"]} --> MAGIC: {player["rogue"]["magic"]+1}""")
        player["other"]["lv"] += 1
        player["rogue"]["maxhp"] = 999
        player["rogue"]["hp"] = player["rogue"]["maxhp"]
        player["rogue"]["maxmp"] += 2
        player["rogue"]["mp"] = player["rogue"]["maxmp"]
        player["rogue"]["atk"] += 2
        player["rogue"]["def"] += 1
        player["rogue"]["magic"] += 1
        player["other"]["next_lv"] += 9999999999999999999999999

def level_system(player, level_stats): #The entire levelling system for all levels
    while player["other"]["next_lv"] <= 0:
        if player["other"]["lv"] == 100:
            break
        level_stats(player)
        if player["other"]["lv"] == 2:
            print_slow(f"\n\n{player["rogue"]["name"]} learnt Heal!")
            player["rogue"]["spells"][0] = "Heal"

def hp_bar(player): #HP bar generation
    max_bars = 20
    hp = max(player["rogue"]["hp"], 0)
    maxhp = player["rogue"]["maxhp"]

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
    max_bars = 20
    mp = max(player["rogue"]["mp"], 0)
    maxmp = player["rogue"]["maxmp"]

    percent = mp / maxmp
    if percent < 1 and percent > 0.94:
        percent = 0.95
    elif percent <= 0.05 and percent > 0:
        percent = 0.05
    filled_bars = round(percent * max_bars)

    bar = "*" * filled_bars + " " * (max_bars - filled_bars)
    player["other"]["mp_stars"] = bar

def battle(mp_recovery, player, enemies, damage_player, damage_enemy, heal_hp_player, heal_hp_enemy, mp_deplete_player, spells, defend_player, defend_enemy, run, enemy_choice, level_system, idx, items): #The entire battle system
    while True:
        while True:
            while True:
                if len(enemies["enemy"]["spells"]) > 0:
                    enemy_choice = random.randint(1,3)
                    break
                else:
                    enemy_choice = random.randint(1,2)
                    break
            if defend_player == True:
                defend_player = False
                player["rogue"]["def"] /= 1.5
                if player["rogue"]["def"] % 1 == 0:
                    player["rogue"]["def"] = int(player["rogue"]["def"])
                else:
                    player["rogue"]["def"] = round(player["rogue"]["def"])
            if defend_enemy == True:
                defend_enemy = False
                enemies["enemy"]["def"] /= 1.5
                if enemies["enemy"]["def"] % 1 == 0:
                    enemies["enemy"]["def"] = int(enemies["enemy"]["def"])
                else:
                    enemies["enemy"]["def"] = round(enemies["enemy"]["def"])
            clear()
            print_frame_2()
            print_frame()
            choice = input("""[1: FIGHT] [2: MAGIC] [3: ITEM] [4: DEFEND] [5: RUN]

--> """)
            if enemy_choice == 2 and choice == "1":
                clear()
                print_frame_2()
                print_frame()
                defend_enemy = True
                enemies["enemy"]["def"] *= 1.5
                if enemies["enemy"]["def"] % 1 == 0:
                    enemies["enemy"]["def"] = int(enemies["enemy"]["def"])
                else:
                    enemies["enemy"]["def"] = round(enemies["enemy"]["def"])
                print_slow(f"{enemies["enemy"]["name"]} defended.")
                time.sleep(1)
            else:
                enemy_choice = 1
            if choice == "1":
                #PLAYER TURN [ATTACK]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{player["rogue"]["name"]} attacks!")
                if random.randint(1,100) > 5:
                    if random.randint(1,100) <= 15:
                        print_slow(" CRITICAL HIT!!")
                        damage_enemy = (player["rogue"]["atk"] - (enemies["enemy"]["def"]/2)) * 1.5
                    else:
                        damage_enemy = player["rogue"]["atk"] - (enemies["enemy"]["def"]/2)
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
¦ 1: [{player["rogue"]["spells"][0]}] Cost: [{spells[player["rogue"]["spells"][0]]["cost"]} MP]
¦ 2: [{player["rogue"]["spells"][1]}] Cost: [{spells[player["rogue"]["spells"][1]]["cost"]} MP]
¦ 3: [{player["rogue"]["spells"][2]}] Cost: [{spells[player["rogue"]["spells"][2]]["cost"]} MP]
¦ 4: [{player["rogue"]["spells"][3]}] Cost: [{spells[player["rogue"]["spells"][3]]["cost"]} MP]
¦ 5: [{player["rogue"]["spells"][4]}] Cost: [{spells[player["rogue"]["spells"][4]]["cost"]} MP]
¦ 6: [{player["rogue"]["spells"][5]}] Cost: [{spells[player["rogue"]["spells"][5]]["cost"]} MP]
¦ 7: [{player["rogue"]["spells"][6]}] Cost: [{spells[player["rogue"]["spells"][6]]["cost"]} MP]
¦ 8: [{player["rogue"]["spells"][7]}] Cost: [{spells[player["rogue"]["spells"][7]]["cost"]} MP]
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
                if idx < 0 or idx >= len(player["rogue"]["spells"]):
                    print_slow("\nInvalid choice. Please select again.")
                    time.sleep(1)
                    clear()
                    continue
                if player["rogue"]["spells"][idx] != "---":
                    if player["rogue"]["mp"] - spells[player["rogue"]["spells"][idx]]["cost"] >= 0:
                        if spells[player["rogue"]["spells"][idx]]["type"] == "Heal":
                            heal_hp_player = player["rogue"]["maxhp"] * spells[player["rogue"]["spells"][idx]]["multiplier"]
                            if heal_hp_player % 1 == 0:
                                heal_hp_player = int(heal_hp_player)
                            else:
                                heal_hp_player = round(heal_hp_player)
                            mp_deplete_player = spells[player["rogue"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["rogue"]["name"]} casted {player["rogue"]["spells"][idx]}!")
                            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                            if player["rogue"]["hp"] == player["rogue"]["maxhp"]:
                                print_slow(f"\nRecovered All HP.")
                            else:
                                print_slow(f"\nRecovered {heal_hp_player} HP.")
                            heal_hp_player = mp_deplete_player = 0
                            time.sleep(1)
                            break
                        elif spells[player["rogue"]["spells"][idx]]["type"] == "Damage":
                            damage_enemy = (player["rogue"]["magic"] * spells[player["rogue"]["spells"][idx]]["multiplier"]) - (enemies["enemy"]["magic"] * 0.75)
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            mp_deplete_player = spells[player["rogue"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["rogue"]["name"]} casted {player["rogue"]["spells"][idx]}!")
                            enemy_animation(heal_hp_enemy, damage_enemy)
                            player_animation(heal_hp_player, heal_mp_player, damage_player, mp_deplete_player)
                            print_slow(f"\nDealt {damage_enemy} damage.")
                            damage_enemy = mp_deplete_player = 0
                            time.sleep(1)
                            break
                        elif spells[player["rogue"]["spells"][idx]]["type"] == "Half":
                            damage_enemy = enemies["enemy"]["hp"] / 2
                            if damage_enemy % 1 == 0:
                                damage_enemy = int(damage_enemy)
                            else:
                                damage_enemy = round(damage_enemy)
                            mp_deplete_player = spells[player["rogue"]["spells"][idx]]["cost"]
                            clear()
                            print_frame_2()
                            print_frame()
                            print_slow(f"{player["rogue"]["name"]} casted {player["rogue"]["spells"][idx]}!")
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
                if idx < 0 or idx >= len(player["other"]["inv"]):
                    print_slow("\nInvalid choice. Please select again.")
                    time.sleep(1)
                    clear()
                    continue
                if player["other"]["inv"][idx] == "---":
                    print_slow("\nThere is no item in that slot.")
                    time.sleep(1)
                    continue
                item_effects(damage_enemy, enemy_animation, idx, choice_item, player, items, heal_hp_player, heal_mp_player)
                if items[player["other"]["inv"][idx]]["type"] == "Escape": #Escape effect as for some reason it doesn't work in function
                    del player["other"]["inv"][idx]
                    player["other"]["inv"].append("---")
                    run = True
                break

            elif choice == "4":
                #PLAYER TURN [DEFEND]
                clear()
                print_frame_2()
                print_frame()
                defend_player = True
                player["rogue"]["def"] *= 1.5
                if player["rogue"]["def"] % 1 == 0:
                    player["rogue"]["def"] = int(player["rogue"]["def"])
                else:
                    player["rogue"]["def"] = round(player["rogue"]["def"])
                print_slow(f"{player["rogue"]["name"]} defended.")
                time.sleep(1)
                break

            elif choice == "5":
                #PLAYER TURN [RUN]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{player["rogue"]["name"]} tried to run")
                print_slow2("...")
                if random.randint(1,100) <= 75:
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
            if enemy_choice == 1:
                #ENEMY TURN [FIGHT]
                clear()
                print_frame_2()
                print_frame()
                print_slow(f"{enemies["enemy"]["name"]} attacks!")
                if random.randint(1,100) > 5:
                    if random.randint(1,100) <= 15:
                        print_slow(" CRITICAL HIT!!")
                        damage_player = (enemies["enemy"]["atk"] - (player["rogue"]["def"]/2)) * 1.5
                    else:
                        damage_player = enemies["enemy"]["atk"] - (player["rogue"]["def"]/2)
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
            elif enemy_choice == 3:
                #ENEMY TURN [MAGIC]
                clear()
                print_frame_2()
                print_frame()
                if spells[enemies["enemy"]["spells"]]["type"] == "Heal":
                    heal_hp_enemy = enemies["enemy"]["maxhp"] * spells[enemies["enemy"]["spells"]]["multiplier"]
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
                    damage_player = (enemies["enemy"]["magic"] * spells[enemies["enemy"]["spells"][idx]]["multiplier"]) - (player["rogue"]["magic"] * 0.75)
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
                    damage_player = player["rogue"]["hp"] / 2
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
You got {enemies["enemy"]["xp_given"]} XP and {enemies["enemy"]["gold_given"]} GOLD!""")
            player["other"]["xp"] += enemies["enemy"]["xp_given"]
            player["other"]["gold"] += enemies["enemy"]["gold_given"]
            player["other"]["next_lv"] -= enemies["enemy"]["xp_given"]
            level_system(player, level_stats)
            time.sleep(2)
            break
        elif player["rogue"]["hp"] == 0:
            print_slow(f"\n{player["rogue"]["name"]} took mortal damage and died.")
            time.sleep(1)
            clear()
            print_ascii("ascii/game_over.txt")
            time.sleep(5)
            sys.exit(0)

player = { #All Player info
    "rogue": { #All ROGUE info
        "name":
            "ROGUE",
        "hp":
            50,
        "maxhp":
            50,
        "mp":
            15,
        "maxmp":
            15,
        "atk":
            5,
        "def":
            1,
        "magic":
            4,
        "spells":
            ["---","---","---","---","---","---","---","---"]
    },
    "other": { #Other stats
        "weapon":
            "Rusty Sword",
        "shield":
            "Wooden Board",
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
            5,
        "gold":
            0,
        "inv":
            ["---","---","---","---","---","---","---","---"],
        "key_inv":
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
            10,
        "maxhp":
            10,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            5,
        "def":
            1,
        "magic":
            3,
        "spells":
            [],
        "xp_given":
            3,
        "gold_given":
            5,
        "ascii":
            load_ascii("ascii/slime.txt")
    },
    2: { #All Dimensional Beast info
        "name":
            "Dimensional Beast",
        "hp":
            100,
        "maxhp":
            100,
        "mp":
            0,
        "maxmp":
            0,
        "atk":
            30,
        "def":
            3,
        "magic":
            5,
        "spells":
            ["Dimensional Shriek"],
        "xp_given":
            100,
        "gold_given":
            300,
        "ascii":
            load_ascii("ascii/d_beast.txt")
    },
    3: { #All Bat info
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
            ["Split"],
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
            [],
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
            3,
        "type":
            "Heal",
        "multiplier":
            0.25
    },
    "Heal+1": { #All Heal+1 info
        "cost":
            15,
        "type":
            "Heal",
        "multiplier":
            0.33
    },
    "Heal+2": { #All Heal+1 info
        "cost":
            15,
        "type":
            "Heal",
        "multiplier":
            0.5
    },
    "Heal+3": { #All Heal+1 info
        "cost":
            15,
        "type":
            "Heal",
        "multiplier":
            0.65
    },
    "Heal+4": { #All Heal+1 info
        "cost":
            15,
        "type":
            "Heal",
        "multiplier":
            0.75
    },
    "Heal+5": { #All Heal+1 info
        "cost":
            15,
        "type":
            "Heal",
        "multiplier":
            1
    },
    "Fireball": { #All Fireball info
        "cost":
            5,
        "type":
            "Damage",
        "multiplier":
            3
    },
    "Split": { #All Drain info
        "cost":
            20,
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
            "Health and MP",
        "info":
            "PLACEHOLDER",
        "sell":
            0
    },
    "Jelly Juice": { #All Jelly Juice info
        "recovery":
            45,
        "type":
            "Health",
        "info":
            "Jelly Juice: Recovers 45 HP.",
        "sell":
            5
    },
    "Green Tea": { #All Green Tea info
        "recovery":
            10,
        "type":
            "MP",
        "info":
            "Green Tea: Recovers 10 MP.",
        "sell":
            4
    },
    "Golden Juice": { #All Golden Juice info
        "recovery":
            9999999999,
        "type":
            "Health and MP",
        "info":
            "Golden Juice: Recovers All HP and All MP.",
        "sell":
            100
    },
    "Bomb": { #All Bomb info
        "recovery":
            0,
        "type":
            "Explosive",
        "info":
            "Bomb: Breaks cracked walls and deals 15 damage.",
        "sell":
            15
    },
    "Escape Orb": { #All Escape Orb info
        "recovery":
            0,
        "type":
            "Escape",
        "info":
            "Escape Orb: Teleports the player to the overworld and escapes battles.",
        "sell":
            8
    },
    "Leader's Key": { #All Leader's Key info
        "recovery":
            0,
        "type":
            "Other",
        "info":
            "Leader's Key: Opens locked doors.",
        "sell":
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
defend_player = False
defend_enemy = False
run = False
enemy_choice = 0
e_num = 0
idx = 0
charge_player = False
charge_enemy = False

current_map = "o_1"
game_map = MAPS[current_map]
player_r, player_c = 10, 17
overworld()
