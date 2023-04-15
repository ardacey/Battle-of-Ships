import sys
open ('Battleship.out', 'w').close() #clear the output file
error_list = []
player1 = []
player2 = []
player1_battle = {1: [], 2: []}
player1_patrol = {1: [], 2: [], 3:[], 4:[]}
player2_battle = {1: [], 2: []}
player2_patrol = {1: [], 2: [], 3:[], 4:[]}
ship_inital = {"C":[5,1,"C",5], "B":[4,2,"B",4], "D":[3,1,"D",3], "S":[3,1,"S",3], "P":[2,4,"P",2]}  #i need this initial value because i changed the values in the player1_ships and player2_ships.
player1_ships = {"C":[5,1,"C",5], "B":[4,2,"B",4], "D":[3,1,"D",3], "S":[3,1,"S",3], "P":[2,4,"P",2]}
player2_ships = {"C":[5,1,"C",5], "B":[4,2,"B",4], "D":[3,1,"D",3], "S":[3,1,"S",3], "P":[2,4,"P",2]}
def output(text):
    with open('Battleship.out', mode='a', encoding="utf-8") as x:
        x.write(str(text))
    print(str(text), end = "")
def output_newline(text):
    with open('Battleship.out', mode='a', encoding="utf-8") as x:
        x.write(str(text) + "\n")
    print(str(text))
try:
    with open(sys.argv[1], "r") as x:
            player1_board = x.read().split("\n")
except IOError:
    error_list.append("Player1.txt")
try:
    with open(sys.argv[2], "r") as y:
            player2_board = y.read().split("\n")
except IOError:
    error_list.append("Player2.txt")
try:
    with open(sys.argv[3], "r") as z:
            player1_moves = z.read().replace("\n","")
            player1_moves = player1_moves.split(";")
except IOError:
    error_list.append("Player1.in")
try:
    with open(sys.argv[4], "r") as v:
        player2_moves = v.read().replace("\n","")
        player2_moves = player2_moves.split(";")
except IOError:
    error_list.append("Player2.in")
if error_list != []:
    output(f"IOError: input file(s) {', '.join(error_list)} is/are not reachable.")
    sys.exit()
output_newline("Battle of Ships Game")
player1_grid = []
player1_grid = [["-" for j in range(10)] for i in range(10)] #This is an ordinary grid for showboard function, all shots are shown in these grids.
player2_grid = []
player2_grid = [["-" for j in range(10)] for i in range(10)]
def showboard():
    player1_battle_values = list(player1_battle.values())
    player2_battle_values = list(player2_battle.values())
    player1_patrol_values = list(player1_patrol.values())
    player2_patrol_values = list(player2_patrol.values())
    if winner == False:
        if player1_turn:
            output_newline("\nPlayer1's Move\n")
        else:
            output_newline("\nPlayer2's Move\n")
        output(f"Round : {round}\t\t\t\t\t")
        output_newline("Grid Size: 10x10\n")
        output_newline("Player1's Hidden Board"+"\t\t"+"Player2's Hidden Board")
    elif winner == True:
        output_newline("Final Information\n")
        output_newline("Player1's Board"+"\t\t\t\t"+"Player2's Board")
    output_newline("  A B C D E F G H I J\t\t  A B C D E F G H I J")
    for k in range(10):
        if winner == False:
            if k == 9:
                output(str(k+1)+""+' '.join(player1_grid[k])+"\t\t")
                output_newline(str(k+1)+""+' '.join(player2_grid[k]))
            else:
                output(str(k+1)+" "+' '.join(player1_grid[k])+"\t\t")
                output_newline(str(k+1)+" "+' '.join(player2_grid[k]))
        elif winner == True:
            if k == 9:
                output(str(k+1)+""+' '.join(player1[k])+"       ")
                output_newline(str(k+1)+""+' '.join(player2[k]))
            else:
                output(str(k+1)+" "+' '.join(player1[k])+"       ")
                output_newline(str(k+1)+" "+' '.join(player2[k]))
    output_newline("")
    output("Carrier\t\t"+str("X " * (ship_inital["C"][1]-player1_ships["C"][1]))+str("-" * player1_ships["C"][1])+"\t\t\t\t")
    output_newline("Carrier\t\t"+str("X " * (ship_inital["C"][1]-player2_ships["C"][1]))+str("- " * player2_ships["C"][1]))
    output("Battleship\t"+str("X " * (player1_battle_values.count([])))+str("- " * (2-player1_battle_values.count([])))+"\t\t\t")
    output_newline("Battleship\t"+str("X " * (player2_battle_values.count([])))+str("- " * (2-player2_battle_values.count([]))))
    output("Destroyer\t"+str("X " * (ship_inital["D"][1]-player1_ships["D"][1]))+str("-" * player1_ships["D"][1])+"\t\t\t\t")
    output_newline("Destroyer\t"+str("X " * (ship_inital["D"][1]-player2_ships["D"][1]))+str("- " * player2_ships["D"][1]))
    output("Submarine\t"+str("X " * (ship_inital["S"][1]-player1_ships["S"][1]))+str("-" * player1_ships["S"][1])+"\t\t\t\t")
    output_newline("Submarine\t"+str("X " * (ship_inital["S"][1]-player2_ships["S"][1]))+str("- " * player2_ships["S"][1]))
    output("Patrol Boat\t"+str("X " * (player1_patrol_values.count([])))+str("- " * (4-player1_patrol_values.count([])))+"\t\t")
    output_newline("Patrol Boat\t"+str("X " * (player2_patrol_values.count([])))+str("- " * (4-player2_patrol_values.count([]))))
    output_newline("")
    #this part seems hard to understand, but i have no other idea rather than simply count the ships one by one.
    #These outputs just count the letters in the data dictionary and output as many as the number of the letters.
    if winner == False:
        if player1_turn:
            output_newline("Enter your move: "+player1_moves[player1_move])
        else:
            output_newline("Enter your move: "+player2_moves[player2_move])
def battleship_finder(player, player_battle, player_list):
    #as there are more than one battleships, when i count the battleships i need to consider multiple possibilites(e.g index errors, ships side by side)
    if str(battleship+1) + chr(b_row+65) in player_battle[1]:
        pass
    elif str(battleship+1) + chr(b_row+65) in player_battle[2]:
        pass
    else:
        player_list.append(str(battleship+1) + chr(b_row+65))
        try:
            if player[battleship][b_row+1] == "B" and player[battleship][b_row+2] == "B" and player[battleship][b_row+3] == "B":
                player_list.append(str(battleship+1) + chr(b_row+66))
                player_list.append(str(battleship+1) + chr(b_row+67))
                player_list.append(str(battleship+1) + chr(b_row+68))
            elif player[battleship+2][b_row] == "B" and player[battleship+3][b_row] == "B" and player[battleship+4][b_row] == "B":
                player_list.append(str(battleship+2) + chr(b_row+65))
                player_list.append(str(battleship+3) + chr(b_row+65))
                player_list.append(str(battleship+4) + chr(b_row+65))
        except IndexError:
            pass
def patrol_finder(player, player_patrol, player_list):
    #like battleships, when i count patrols i need to check multiple possibilities.
    if (str(patrol+1) + chr(b_row+65)) in player_patrol[1]:
        pass
    elif (str(patrol+1) + chr(b_row+65)) in player_patrol[2]:
        pass
    elif (str(patrol+1) + chr(b_row+65)) in player_patrol[3]:
        pass
    elif(str(patrol+1) + chr(b_row+65)) in player_patrol[4]:
        pass
    else:
        player_list.append(str(patrol+1) + chr(b_row+65))
        try:
            if player[patrol][b_row+1] == "P":
                player_list.append(str(patrol+1) + chr(b_row+66))
            elif player[patrol+1][b_row] == "P":
                player_list.append(str(patrol+2) + chr(b_row+65))
        except IndexError:
            pass
for row in player1_board:
    a = row.split(";")
    for i in range(len(a)):
        if a[i] == "":
            a[i] = "-"
    player1.append(a)
for row in player2_board:
    b = row.split(";")
    for j in range(len(b)):
        if b[j] == "":
            b[j] = "-"
    player2.append(b)
for battleship in range(10):
    for b_row in range(10):
        if player1[battleship][b_row] == "B":
            if player1_battle[1] == []:
                battleship_finder(player1, player1_battle, player1_battle[1])
            elif player1_battle[1] != []:
                battleship_finder(player1, player1_battle, player1_battle[2])                  
        elif player2[battleship][b_row] == "B":
            if player2_battle[1] == []:
                battleship_finder(player2, player2_battle, player2_battle[1])
            elif player2_battle[1] != []:
                battleship_finder(player2, player2_battle, player2_battle[2])
for patrol in range(10):
    for b_row in range(10):
        if player1[patrol][b_row] == "P":
            if player1_patrol[1] == []:
                patrol_finder(player1, player1_patrol, player1_patrol[1])
            elif player1_patrol[2] == []:
                patrol_finder(player1, player1_patrol, player1_patrol[2])
            elif player1_patrol[3] == []:
                patrol_finder(player1, player1_patrol, player1_patrol[3])
            elif player1_patrol[4] == []:
                patrol_finder(player1, player1_patrol, player1_patrol[4])
        elif player2[patrol][b_row] == "P":
            if player2_patrol[1] == []:
                patrol_finder(player2,player2_patrol,  player2_patrol[1])
            elif player2_patrol[2] == []:
                patrol_finder(player2, player2_patrol, player2_patrol[2])
            elif player2_patrol[3] == []:
                patrol_finder(player2, player2_patrol, player2_patrol[3])
            elif player2_patrol[4] == []:
                patrol_finder(player2, player2_patrol, player2_patrol[4])
winner = False
player1_turn = True
player1_move = 0
player2_move = 0
round = 1
error_flag = False
#This is the main part of the code. While there are no winners, code executes all the rounds and shots by the players. If any player wins the game, while loop stops and shows the final board.
while not winner:
    if player1_turn:
        try:
            if error_flag == True:
                error_flag = False
            else:
                showboard()
            move1 = player1_moves[player1_move].split(",")
            assert int(move1[0]) < 11 and ord(move1[1])-65 < 10
            player_move1 = player1_moves[player1_move].replace(",", "")
            data1 = player2[int(move1[0])-1][ord(move1[1])-65]
            player1_move += 1
        except IndexError:
            output_newline(f"Index Error: Found wrong argument at {player1_moves[player1_move]}")
            player1_move += 1
            output_newline("Enter your move: "+player1_moves[player1_move])
            error_flag = True
            continue
        except ValueError:
            output_newline(f"Value Error: Found wrong argument at {player1_moves[player1_move]}")
            player1_move += 1   
            output_newline("Enter your move: "+player1_moves[player1_move])
            error_flag = True
            continue
        except AssertionError:
            output_newline("AssertionError: Invalid Operation.")     
            player1_move += 1
            output_newline("Enter your move: "+player1_moves[player1_move])
            error_flag = True
            continue
        except:
            output_newline("kaBOOM: run for your life!")
        if data1.isalpha() is True:   #If there is letter in specified position, this means player hit any ship.
            if data1 == "B":
                if player_move1 in player2_battle[1]:
                    player2_battle[1].remove(player_move1)
                elif player_move1 in player2_battle[2]:
                    player2_battle[2].remove(player_move1)
            elif data1 == "P":
                if player_move1 in player2_patrol[1]:
                    player2_patrol[1].remove(player_move1)
                elif player_move1 in player2_patrol[2]:
                    player2_patrol[2].remove(player_move1)
                elif player_move1 in player2_patrol[3]:
                    player2_patrol[3].remove(player_move1)
                elif player_move1 in player2_patrol[4]:
                    player2_patrol[4].remove(player_move1)
            else:
                player2_ships[data1][0] -= 1
                if player2_ships[data1][0] == 0:
                    player2_ships[data1][0] = player2_ships[data1][3]
                    player2_ships[data1][1] -= 1
            player2[int(move1[0])-1][ord(move1[1])-65] = "X"
            player2_grid[int(move1[0])-1][ord(move1[1])-65] = "X"
        else:
            player2[int(move1[0])-1][ord(move1[1])-65] = "O"
            player2_grid[int(move1[0])-1][ord(move1[1])-65] = "O"
        player1_turn = not player1_turn
        merged_player2 = sum(player2, [])
    else:
        try:
            if error_flag == True:
                error_flag = False
            else:
                showboard()
            move2 = player2_moves[player2_move].split(",")
            assert int(move2[0]) < 11 and ord(move2[1])-65 < 10
            player_move2 = player2_moves[player2_move].replace(",", "")
            data2 = player1[int(move2[0])-1][ord(move2[1])-65]
            player2_move += 1
        except IndexError:
            output_newline(f"Index Error: Found wrong argument at {player2_moves[player2_move]}")
            player2_move += 1
            output_newline("Enter your move: "+player2_moves[player2_move])
            error_flag = True
            continue
        except ValueError:
            output_newline(f"Value Error: Found wrong argument at {player2_moves[player2_move]}")
            player2_move += 1
            output_newline("Enter your move: "+player2_moves[player2_move])
            error_flag = True
            continue
        except AssertionError:
            output_newline("AssertionError: Invalid Operation.")     
            player2_move += 1
            output_newline("Enter your move: "+player2_moves[player2_move])
            error_flag = True
            continue
        except:
            output_newline("kaBOOM: run for your life!")
        if data2.isalpha() is True:
            if data2 == "B":
                if player_move2 in player1_battle[1]:
                    player1_battle[1].remove(player_move2)
                elif player_move2 in player1_battle[2]:
                    player1_battle[2].remove(player_move2)
            elif data2 == "P":
                if player_move2 in player1_patrol[1]:
                    player1_patrol[1].remove(player_move2)
                elif player_move2 in player1_patrol[2]:
                    player1_patrol[2].remove(player_move2)
                elif player_move2 in player1_patrol[3]:
                    player1_patrol[3].remove(player_move2)
                elif player_move2 in player1_patrol[4]:
                    player1_patrol[4].remove(player_move2)
            else:
                player1_ships[data2][0] -= 1
                if player1_ships[data2][0] == 0:
                    player1_ships[data2][0] = player1_ships[data2][3]
                    player1_ships[data2][1] -= 1
            player1[int(move2[0])-1][ord(move2[1])-65] = "X"
            player1_grid[int(move2[0])-1][ord(move2[1])-65] = "X"
        else:
            player1[int(move2[0])-1][ord(move2[1])-65] = "O"
            player1_grid[int(move2[0])-1][ord(move2[1])-65] = "O"
        round += 1
        player1_turn = not player1_turn
        merged_player1 = sum(player1, [])
        if not any(item in merged_player1 for item in ["C", "B", "D", "S", "P"]) and not any(item in merged_player2 for item in ["C", "B", "D", "S", "P"]):
            winner = True
            winner_player = 3
        elif not any(item in merged_player1 for item in ["C", "B", "D", "S", "P"]):
            winner = True
            winner_player = 2
        elif not any(item in merged_player2 for item in ["C", "B", "D", "S", "P"]):
            winner = True
            winner_player = 1
if winner_player == 1:
    output_newline("\nPlayer1 Wins!\n")
    showboard()
elif winner_player == 2:
    output_newline("\nPlayer2 Wins!\n")
    showboard()
elif winner_player == 3:
    output_newline("\nIt is a Draw!\n")
    showboard()