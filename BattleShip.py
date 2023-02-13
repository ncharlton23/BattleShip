'''
Created on Jan 30, 2023
@author: ncharlton23
Purpose of code: Play a game of
battleship against an AI, first 
to lose all four ships loses the
game.
'''
import random             #Imports the random module for AI
from time import sleep    #Imports the sleep module for polish

def main():                                                                                         #Main contains variable definitions and then runs placement functions
     
    counter = 0                                                                                     #Sets general counter as 0
    player_hit_counter = 0                                                                          #Sets player hit counter as 0
    AI_hit_counter = 0                                                                              #Sets AI hit counter as 0
     
    playerBoard = [[' ','A','B','C','D','E',' '],                                                   #The board of the player to keep track of player ships and enemy shots
            ['1','-','-','-','-','-',' '],
            ['2','-','-','-','-','-','|---------------|'],
            ['3','-','-','-','-','-','|Your Ship Board|'],
            ['4','-','-','-','-','-','|---------------|'],
            ['5','-','-','-','-','-',' '],]
    
    enemyBoard = [[' ','A','B','C','D','E',' '],                                                    #The board of the AI to keep track of AI ships and player shots
            ['1','-','-','-','-','-',' '],
            ['2','-','-','-','-','-','|----------------|'],
            ['3','-','-','-','-','-','|Enemy Ship Board|'],
            ['4','-','-','-','-','-','|----------------|'],
            ['5','-','-','-','-','-',' '],]
    
    firingBoard = [[' ','A','B','C','D','E',' '],                                                   #The players firing board to keep track of where they have fired
            ['1','-','-','-','-','-',' '],
            ['2','-','-','-','-','-','|-----------------|'],
            ['3','-','-','-','-','-','|Your Firing Board|'],
            ['4','-','-','-','-','-','|-----------------|'],
            ['5','-','-','-','-','-',' '],]
    
    enemyPlacementAI(enemyBoard)                                                                    #Runs AI ship placement function
    shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter)     #Runs player ship placement function
    
def playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter):                                                  #PlayerMoves keeps track of the players shots for hits and misses

    firingBoardPrint(firingBoard)                                                                                                               #Prints the firing board for player convenience 
    player_choice = input("Enter your firing target coordinates. Ex:A2")                                                                        #Takes the players desired firing coordinates 
    try:
        letter, number = [(x) for x in str(player_choice)]                                                                                      #Separates the coordinates into two variables
    except ValueError:                                                                                                                          #Fail safe for if the player enters too-many/too-few coordinates
        print("Please enter a valid coordinate")                                                                                                #Notifies player of mistake
        playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                                               #Re-runs the function so the player can enter a valid coordinate pair
    
    if letter == "A":                                                                                                                           #Assigns the A coordinate the value of 1
        letter = 1
    elif letter == "B":                                                                                                                         #Assigns the B coordinate the value of 2
        letter = 2
    elif letter == "C":                                                                                                                         #Assigns the C coordinate the value of 3
        letter = 3
    elif letter == "D":                                                                                                                         #Assigns the D coordinate the value of 4
        letter = 4
    elif letter == "E":                                                                                                                         #Assigns the E coordinate the value of 5
        letter = 5
    elif letter != "A" or "B" or "C" or "D" or "E":                                                                                             #Fail safe for if the player enters invalid letter coordinates
        print("please enter a valid coordinate")                                                                                                #Notifies player of mistake
        playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                                               #Re-runs the function so the player can enter a valid letter coordinate

    try:
            number = int(number)                                                                                                                #Converts the number part of the coordinate to an integer
    except ValueError:                                                                                                                          #Fail safe for if the player enters invalid number coordinates
        print('please enter valid coordinate')                                                                                                  #Notifies the player of mistake
        playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                                               #Re-runs the function so the player can enter a valid number coordinate
    if number == 0:
        print('please enter valid coordinate')
        playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)
    if enemyBoard[number][letter] == 'O':                                                                                                       #Prevents the player from firing at the same tile twice
        print('please enter a valid coordinate')                                                                                                #Notifies the player of mistake
        playerMoves(firingBoard, enemyBoard, playerBoard, counter, player_hit_counter, AI_hit_counter)                                          #Re-runs the function so the player can enter a valid target coordinate
    elif enemyBoard[number][letter] == 'X':                                                                                                     #Prevents the player from firing at the same tile twice
        print('please enter a valid coordinate')                                                                                                #Notifies the player of mistake
        playerMoves(firingBoard, enemyBoard, playerBoard, counter, player_hit_counter, AI_hit_counter)                                          #Re-runs the function so the player can enter a valid target coordinate
    elif enemyBoard[number][letter] == 'V':                                                                                                     #Identifies that the player hit a ship
        enemyBoard[number][letter] = 'X'                                                                                                        #Turns that tile on the enemy board to a "destroyed" tile
        firingBoard[number][letter] = 'X'                                                                                                       #Turns that tile on the player firing board to a "destroyed" tile
        player_hit_counter += 1                                                                                                                 #Adds a value to the player hit counter because the player hit a ship
        sleep(1)
        print("Hit")                                                                                                                            #Notifies the player of the hit
    elif enemyBoard[number][letter] != 'V':                                                                                                     #Identifies that the player missed a ship
        enemyBoard[number][letter] = 'O'                                                                                                        #Turns that tile on the enemy board to a "missed" tile
        firingBoard[number][letter] = 'O'                                                                                                       #Turns that tile on the player firing board to a "missed" tile
        sleep(1)
        print("Miss")                                                                                                                           #Notifies the player of the miss
        
    if player_hit_counter == 4:                                                                                                                 #If the player hits four ships this will activate
        play_again = input("Congratulations! Your fleet has prevailed and your enemy has been defeated! Would you like to play again? Yes/No")  #Notifies the player that they have won the game
        if play_again == ("Yes"):                                                                                                               #If they enter yes, they play again
            main()                                                                                                                              #Runs the main to start over
        elif play_again == ("No"):                                                                                                              #If they enter no, the program terminates
            exit()                                                                                                                              #Terminates program
        
    sleep(1)
    firingBoardPrint(firingBoard)                                                                                                               #Prints the players firing board for convenience                                                                                                     
    enemyFiringAI(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                                                 #Runs the AI firing function
  
def shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter):                #ShipPlacement allows the players to place their ships on their board
    
    playerBoardPrint(playerBoard)                                                                               #Prints player board for convenience
    while counter < 4:                                                                                          #Runs this segment 4 times
        player_choice = input("Enter your ship placement coordinates. Ex:A2")                                   #Takes ship placement coordinates from the user
        try:
            letter, number = [(x) for x in str(player_choice)]                                                  #Separates the coordinates into two variables  
        except ValueError:                                                                                      #Fail safe for if the player enters too-many/too-few coordinates
            print("Please enter a valid coordinate")                                                            #Notifies the player of mistake
            shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter)         #Re-runs the function so the player can enter a valid coordinate pair
    
        if letter == "A":                                                                                       #Assigns the A coordinate the value of 1
            letter = 1
        elif letter == "B":                                                                                     #Assigns the B coordinate the value of 2
            letter = 2
        elif letter == "C":                                                                                     #Assigns the C coordinate the value of 3
            letter = 3
        elif letter == "D":                                                                                     #Assigns the D coordinate the value of 4
            letter = 4
        elif letter == "E":                                                                                     #Assigns the E coordinate the value of 5
            letter = 5
        elif letter != "A" or "B" or "C" or "D" or "E":                                                         #Fail safe for if the player enters invalid letter coordinates
            print("please enter a valid coordinate")                                                            #Notifies the player of mistake
            shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter)         #Re-runs the function so the player can enter a valid letter coordinate
            
        try:
            number = int(number)                                                                                #Converts the number part of the coordinate to an integer
        except ValueError:                                                                                      #Fail safe for if the player enters invalid number coordinates
            print('please enter valid coordinate')                                                              #Notifies player of mistake 
            shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter)         #Re-runs the function so the player can enter valid number coordinate
        if number == 0:
            print('please enter valid coordinate')
            shipPlacement(playerBoard,firingBoard,enemyBoard,counter,player_hit_counter,AI_hit_counter)
        if playerBoard[number][letter] == 'V':                                                                  #Identifies if the player has or has not already placed a ship in the desired tile
            print("Sorry, you already have a ship there.")                                                      #Notifies the player of mistake
            shipPlacement(playerBoard, firingBoard, enemyBoard, counter, player_hit_counter, AI_hit_counter)    #Re-runs the function so the player can enter a valid ship coordinate 
        playerBoard[number][letter] = 'V'                                                                       #Turns the desired tile into a "ship" tile
        playerBoardPrint(playerBoard)                                                                           #Prints player board for convenience
        counter += 1                                                                                            #Adds a value to the counter
    
    playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                   #Runs the playerMoves function
    
def enemyFiringAI(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter):                            #enemyFiringAI allows the AI to fight back against the player without repeating shots
    
    coordinate_list = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]  #A list of all possible target coordinates on the board                                        
    enemy_choice = random.choice(coordinate_list)                                                                           #Randomly selects a coordinate from the list
    letter, number = [(x) for x in str(enemy_choice)]                                                                       #Separates the two coordinate values into variables
    letter = int(letter)                                                                                                    #Assigns letter variable integer designation
    number = int(number)                                                                                                    #Assigns number variable integer designation
    if playerBoard[number][letter] == 'O':                                                                                  #Checks to see if AI is firing at a tile that has already been shot at
        enemyFiringAI(firingBoard, enemyBoard, playerBoard, counter, player_hit_counter, AI_hit_counter)                    #Re-runs the function so the AI picks a different target
    elif playerBoard[number][letter] == 'X':                                                                                #Checks to see if AI is firing at a tile that has already been shot at 
        enemyFiringAI(firingBoard, enemyBoard, playerBoard, counter, player_hit_counter, AI_hit_counter)                    #Re-runs the function so the AI picks a different target
    elif playerBoard[number][letter] == 'V':                                                                                #Checks to see if AI hit a player ship  
        playerBoard[number][letter] = 'X'                                                                                   #Turns the tile on the player board to a "destroyed" tile
        AI_hit_counter += 1                                                                                                 #Adds a value to the AI hit counter
        print("Enemy is firing!")                                                                                           
        sleep(1)
        print("Hit")                                                                                                        #Notifies player of hit
    elif playerBoard[number][letter] != 'V':                                                                                #Checks to see if AI missed a player ship
        playerBoard[number][letter] = 'O'                                                                                   #Turns the tile on the player board to a "missed" tile 
        print("Enemy is firing!")                                                                                           
        sleep(1)
        print("Miss")
        
    if AI_hit_counter == 4:                                                                                                 #Checks to see if AI has hit four ships
        print("All of your vessels have been sunk, countless lives who looked to you for leadership have been lost")
        sleep(2)
        print("Your coast lies defenseless and vulnerable, the enemy sails onwards, triumphant and ready to strike")
        sleep(2)
        print("The consequences of your failure weighs upon your shoulders, you have let down those you swore to protect")
        sleep(2)
        print("Get up sailor, you have lost the battle, but you have not lost the war")
        sleep(2)
        play_again = input("Try again? Yes/No")                                                                             #Prompts user to play again
        if play_again == ("Yes"):                                                                                           #Checks to see if player wants to play again
            main()                                                                                                          #Re-runs entire program
        elif play_again == ("No"):                                                                                          #Checks to see if player does not want to play again
            exit()                                                                                                          #Terminates program
        
    sleep(1)
    playerBoardPrint(playerBoard)                                                                                           #Prints player board for convenience
    sleep(2)
    playerMoves(firingBoard,enemyBoard,playerBoard,counter,player_hit_counter,AI_hit_counter)                               #Runs playerMoves function
    
def enemyPlacementAI(enemyBoard):                                                                                           #enemyPlacementAI places four enemy ships randomly without repeating on the enemy board
    
    coordinate_list = [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55]  #Coordinate list containing all possible placement coordinates                                       
    result=set(coordinate_list)                                                                                             #Designates coordinate_list as a set and assigns it a variable (result)
    noRepeat=list(result)                                                                                                   #Designates result as another list and assigns it a variable (noRepeat)
    enemy_choice=(random.sample(noRepeat, 4))                                                                               #Takes four random, non repeating coordinate pairs from the list
    enemy_choice1 = enemy_choice[0]                                                                                         #Designates coordinate one as a variable
    enemy_choice2 = enemy_choice[1]                                                                                         #Designates coordinate two as a variable
    enemy_choice3 = enemy_choice[2]                                                                                         #Designates coordinate three as a variable
    enemy_choice4 = enemy_choice[3]                                                                                         #Designates coordinate four as a variable
    letter, number = [(x) for x in str(enemy_choice1)]                                                                      #Separates the two numbers into two variables
    letter = int(letter)                                                                                                    #Assigns integer value to letter variable (I'm 90% sure this is pointless but it works so hey)
    number = int(number)                                                                                                    #Assigns integer value to number variable (I'm 90% sure this is pointless but it works so hey)
    enemyBoard[number][letter] = 'V'                                                                                        #Converts the designated tile on the enemy board to a ship tile
    letter, number = [(x) for x in str(enemy_choice2)]                                                                      #Repeat
    letter = int(letter)
    number = int(number)
    enemyBoard[number][letter] = 'V'
    letter, number = [(x) for x in str(enemy_choice3)]                                                                      #Repeat
    letter = int(letter)
    number = int(number)
    enemyBoard[number][letter] = 'V'
    letter, number = [(x) for x in str(enemy_choice4)]                                                                      #Repeat
    letter = int(letter)
    number = int(number)
    enemyBoard[number][letter] = 'V'

def playerBoardPrint(playerBoard):                      #playerBoardPrint prints the player board

    for row in range(0,6):
        col = 0
        for col in range(0,7):
            print(playerBoard[row][col], end = " ")
        print("")  
        
def enemyBoardPrint(enemyBoard):                        #ememyBoardPrint prints the enemy board

    for row in range(0,6):
        col = 0
        for col in range(0,7):
            print(enemyBoard[row][col], end = " ")
        print("")  

def firingBoardPrint(firingBoard):                      #firingBoardPrint prints the firing board
    
    for row in range(0,6):
        col = 0
        for col in range(0,7):
            print(firingBoard[row][col], end = " ")
        print("")  
        
if __name__ == '__main__':
    main()