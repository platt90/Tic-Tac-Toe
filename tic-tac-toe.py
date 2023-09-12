##########################
## Author: Jon Platt    ##
##########################
## Program: Tic Tac Toe ## 
##########################

####################
# Global Libraries #
####################
import random

####################
# Global variables #
####################
leaderBoard = []
diagonalCheck = []
gameBoard = None
playerName = None
player = None
cpu = None
moveCounter = None
playerWin = None
cpuWin = None

#########################
# Function declarations #
#########################

# Function: resetGame - Resets the game for a new playthrough
def resetGame():
    # Import global variables
    global gameBoard
    global moveCounter
    global playerWin
    global cpuWin
    global diagonalCheck
    
    gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ], [ "E", "E", "E" ] ] # Resets the gameboard to empty
    diagonalCheck = [ [ "E", "E", "E" ], [ "E", "E", "E" ], [ "E", "E", "E" ] ] # Resets the diagonal ckeck list to empty
    moveCounter = 0 # Reset move counter to zero
    playerWin = False # Resets playerWin trigger to False
    cpuWin = False # Resets cpuWin trigger to False
    setPrimaryPlayer() # Calls function to randomly assign Primary Player to either player or cpu

# Function: printGameTitle - Displays the Game Title 'Tic Tac Toe' at the beginning of the game
def printGameTitle():
    #Print Game Title
    print("\n")
    print("$$$$$$$$\ $$$$$$\  $$$$$$\        $$$$$$$$\  $$$$$$\   $$$$$$\        $$$$$$$$\  $$$$$$\  $$$$$$$$\ ")
    print("\__$$  __|\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\       \__$$  __|$$  __$$\ $$  _____|")
    print("   $$ |     $$ |  $$ /  \__|         $$ |   $$ /  $$ |$$ /  \__|         $$ |   $$ /  $$ |$$ |      ")
    print("   $$ |     $$ |  $$ |               $$ |   $$$$$$$$ |$$ |               $$ |   $$ |  $$ |$$$$$\    ")
    print("   $$ |     $$ |  $$ |               $$ |   $$  __$$ |$$ |               $$ |   $$ |  $$ |$$  __|   ")
    print("   $$ |     $$ |  $$ |  $$\          $$ |   $$ |  $$ |$$ |  $$\          $$ |   $$ |  $$ |$$ |      ")
    print("   $$ |   $$$$$$\ \$$$$$$  |         $$ |   $$ |  $$ |\$$$$$$  |         $$ |    $$$$$$  |$$$$$$$$\ ")
    print("   \__|   \______| \______/          \__|   \__|  \__| \______/          \__|    \______/ \________|\n")
    print("\t\t\t\t\tAuthor: Jon Platt\n")

# Function: printGameBoard - Creats the game board using the list of lists gameBoard and outputs it with column letters and row numbers
def printGameBoard():
    # Import global variables
    global gameBoard

    print() # Line seperator to give the board a space between the previous line of text on screen
    print("\t  A B C") # Print the column letters
    
    for rowCount, row in enumerate(gameBoard):
        print("\t" + str(rowCount + 1), end=" ")
        for colCount, col in enumerate(row):
            if rowCount < 2:
                if col == "E":
                    print("_", end="")
                elif col == "X":
                    print("\033[4mX\033[0m", end="")
                else:
                    print("\033[4mO\033[0m", end="")
            else:
                if col == "E":
                    print(" ", end="")
                elif col == "X":
                    print("X", end="")
                else:
                    print("O", end="")
            if colCount < 2:
                print("|", end="")
        print()
    print() # Line seperator

# Function: getPrimaryPlayer - Randomly picks whether player or cpu is the primary player - Makes use of Global Library: Random
def setPrimaryPlayer():
    # Import Global Variables
    global player
    global cpu

    playerSelect = random.randint(0, 1) # Randomly sets player to either 1 or 0
    if playerSelect == 0: # If player was set to 0
        player = 'X' # Player is primary X
        cpu = 'O' # CPU is O
    else: # Else CPU is the primary player
        cpu = 'X'
        player = 'O'

# Function: getValidPlayerName - Ask the player to enter their initials. Gives the function the 'prompt' and 'error message' perameters as a string
def getValidPlayerName(prompt, errorMessage): 
    # Import global variables
    global playerName

    valid = False # Variable to act as a validity switch for our while loop. While loop will continue until criteria is met and validity switch becomes True
    while not valid: # While valid = False
        playerName = input(prompt) # Get initials from the player using the 'prompt' perameter
        playerName = playerName.upper() # Changes the input to uppercase
        if str.isalpha(playerName) == True and len(playerName) == 3: # Player input meets the required criterea
            valid = True # Validity switch is turned to True as requirement is met. This allows the while loop to end
        elif playerName == "QUIT": # Player inputs Quit
            quit() # Quits the application
        else:
            print(errorMessage) # Tells player they've entered an incorrect name using the 'error message' perameter

# Fuction: getValidPlayerMove - Asks the player to enter a move and updates the game board if valid move is entered. Gives the function the 'prompt', 'invalidMove' and 'spaceTaken' perameters as a string
def getValidPlayerMove(prompt, invalidMove, spaceTaken):
    # Import global variables
    global gameBoard
    global cpuWin

    validMoves = [ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', '1A', '2A', '3A', '1B', '2B', '3B', '1C', '2C', '3C' ] # List of valid player moves

    printGameBoard() # Function to print the up to date gameboard
    valid = False # Variable to act as a validity switch for our while loop. While loop will continue until player enters a valid move and validity switch becomes True
    while not valid: # While valid = False
        move = input(prompt) # Uses the 'prompt'perameter to ask the player for their move
        move = move.upper() # Converts the input to upper case
        if move == 'QUIT': # If use enters 'Quit' then the cpu wins and the games ends
            cpuWin = True
            valid = True
        elif move in validMoves: # If move is in list of valid moves
            j = move[0] # Sets j to the first character input by the player
            if str.isalpha(j): # Checks if j is a letter and if so makes sets i to the second character input by the player
                i = int(move[1])
                i -= 1
            else: # If j is not a letter then it means the player entered the number in first, in which case i becomes the first character and j is the second
                j = move[1]
                i = int(move[0])
                i -= 1
            if j == 'A': # Checks if player entered A and sets the to 0 for the game board to be updated correctly
               j = 0
            elif j == 'B':  # Checks if player entered B and sets the to 0 for the game board to be updated correctly
                j = 1
            elif j == 'C':  # Checks if player entered C and sets the to 0 for the game board to be updated correctly
                j = 2
            if gameBoard[i][j] == "E": # Checks that the space the player has entered is empty and therefore a valid move
                gameBoard[i][j] = (player) # If space isn't taken the the board is updated with the players letter and validity switch becomes true and the while loop can end
                valid = True
            else:
                print(spaceTaken) # Else the space is already taken and the player is told to re-enter a correct move
        else:
            print(invalidMove) # Else the player hasn't entered a valid move from the validMoves list and is told to re-enter a correct move

# Function: gameMoves - Checks who is the primary player and begins gameplay
def gameMoves():
    # Import global variables
    global moveCounter

    if player == 'X': # If player is primary they will make the first move
        getValidPlayerMove("Make your move: ", "Invalid Move", "Space Already Taken") # Function to get a valid player move. Gives the function the 'promt', 'invalidMove' and 'spaceTaken' parameters
        moveCounter += 1 # moveCounter is incremented by 1
        checkForWin() # Checks for a win scenario
        if not playerWin and not cpuWin and moveCounter < 9: # If player and cpu have not won and moveCounter is less than 9
            cpuWinningMove()
            moveCounter += 1 # moveCounter is incremented by 1
    else: # Else cpu is the primary player and they will make the first move
        cpuWinningMove()
        moveCounter += 1 # moveCounter is incremented by 1
        checkForWin() # Checks for a win scenario
        if not cpuWin and not playerWin and moveCounter < 9: # If player and cpu have not won and moveCounter is less than 9
            getValidPlayerMove("Make your move: ", "Invalid Move", "Space Already Taken") # Function to get a valid player move. Gives the function the 'promt', 'invalidMove' and 'spaceTaken' parameters
            moveCounter += 1 # moveCounter is incremented by 1

# Function - checkForWin - Checks if the 'Win' criterea has been met by either the player or computer
def checkForWin():
    #Import global variables
    global gameBoard
    global diagonalCheck
    global playerWin
    global cpuWin

    # Row Checks
    for row in gameBoard: # For each rown in the gameboard
        if row == [player, player, player]: # Checks for a player win on a row
            playerWin = True # Sets playerWin trigger to True
        elif row == [cpu, cpu, cpu]: # Checks for a player win on a row
            cpuWin = True # Sets cpuWin trigger to True
    # Column Checks
    for i in range(0, len(gameBoard)):
        if [gameBoard[0][i], gameBoard[1][i], gameBoard[2][i]] == [player, player, player]: # Checks whether a column is won by player
            playerWin = True # Sets playerWin trigger to True
        elif [gameBoard[0][i], gameBoard[1][i], gameBoard[2][i]] == [cpu, cpu, cpu]: # Checks whether a column is won by CPU
            cpuWin = True # Sets cpuWin trigger to True
    # Diagonal checks
    for row in diagonalCheck:
        if row == [player, player, player] or [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]] == [player, player, player]: # Checks whether a diagonal is won by player
            playerWin = True # Sets playerWin trigger to True
        elif row == [cpu, cpu, cpu] or [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]] == [cpu, cpu, cpu]: # Checks whether a diagonal is won by CPU
            cpuWin = True # Sets cpuWin trigger to True

# Function: beginGame - Takes player move and cpu move and checks for a win scenario
def beginGame():
    # Import Global Variables - These will act as triggers for a win, draw or lose scenario
    global playerWin # Boolean to trigger when the game is Won
    global cpuWin # Boolean to trigger when the game is Lost
    global moveCounter # Move Counter allows us to set max turns. This will trigger a draw when it gets to above 9

    resetGame() # Calls upon function resetGame to reset the game to its intial state
 
    while not playerWin and not cpuWin and moveCounter < 9: #while loop to determines if the game is won, lost or drawn
        gameMoves() # Calls upon function to make the game moves
        checkForWin() # Checks for a win scenario
    if playerWin == True: # Checks if the player has won
        printGameBoard() # Prints the final gameboard
        print("\033[1m\033[4m" + "You Win!" + "\033[0m\n") # Tells the player they've won (Text is bold and underlined)
    elif cpuWin == True: # Checks if the cpu has won
        printGameBoard() # Prints the final gameboard
        print("\033[1m\033[4m" + "You Lose!" + "\033[0m\n") # Tells the player they've lost (Text is bold and underlined)
    else: # moveCounter must have hit 9 with no playerWin or cpuWin and therefore must be a draw
        printGameBoard() # Prints the final gameboard
        print("\033[1m\033[4m" + "It's a Draw!" + "\033[0m\n") # Tells the player they've drawn (Text is bold and underlined)
    
    updateLeaderBoard(playerName) # Calls upon function to update the leader board once a game is ended
    displayLeaderBoard() # Calls upon function to display the updated leader board

    playAgain = input("Would you like to play again? (y/n): ") # Asks the player if they want to play again
    if playAgain.upper() == 'Y': # If player answers Y then the game restarts
        beginGame() # Begins the game again

# Function: readLeaderBoardFile - Reads in the leaderboard.dat file, if the file doesn't exist it will be created and an empty leader board will be output to the user
def readLeaderBoardFile():
    # Import global variables
    global leaderBoard

    try: # Trys to load the leaderboard.dat file as read only if it exists
        leaderBoardFile = open("leaderboard.dat", "r")
    except Exception: # If no leaderboard.dat file exists then it throws the exception and displays an empty leader board list
        print("\033[1m\033[4mPlayer\tWin %\tDraw %\tLoss %\033[0m") # Leader Board header
        print("---\t--\t--\t--\n---\t--\t--\t--\n---\t--\t--\t--\n---\t--\t--\t--\n---\t--\t--\t--\n") # Displays empty player info when there is no leader board file
    else:
        leaderBoardData = leaderBoardFile.readline().strip() # Loads and strips the data from the leaderboaard.dat file and adds to leaderBoardData

        while leaderBoardData:
            leaderBoardPlayers = leaderBoardData.split(",") # Takes the data from leaderBoardData and adds to leaderBoardPlayers splitting the data whenever there is a comma
            try:
                leaderBoard.append([leaderBoardPlayers[0], int(leaderBoardPlayers[1]), int(leaderBoardPlayers[2]), int(leaderBoardPlayers[3])]) # Adds the data to the leaderBoard list
            except Exception:
                print("Leader Board File Corrupted")  #If the data is corrupt an error message will appear and the program will quit
                quit()
            else:
                leaderBoardData = leaderBoardFile.readline().strip()

        leaderBoardFile.close() # Closes the leader board file
        displayLeaderBoard() # Calls upon function to display the leader board

# Function: updateLeaderBoard - Checks if the player is already on the leader board. Updates that players details or appends the list if it's a new player
def updateLeaderBoard(playerName):

    playerFound = -1 # Sets playerFount to -1
    for index in range(0, len(leaderBoard)):
        if leaderBoard[index][0] == playerName: # Checks to see if the current player is already on the leader board
            playerFound = index # If so then playerFound is changed in line with the index number of the player

    if playerFound != -1: # If player is on leader board
        #We are updating the player score
        leaderBoard[playerFound][1] +=1 # Increments the games played count by 1
        if playerWin == True:
            leaderBoard[playerFound][2] +=1 # If player has won the this increments their win score by 1
        elif playerWin == False and cpuWin == False:
            leaderBoard[playerFound][3] +=1 # If player hasn't won or lost then their draw count increments by 1
    else:
        #We are appending a new player
        if playerWin == True:
            leaderBoard.append([playerName, + 1, + 1, + 0]) # If new player has won we add their details with 1 game played and 1 win
        elif playerWin == False and cpuWin == False:
            leaderBoard.append([playerName, + 1, + 0, + 1]) # If new player has drawn we add their details with 1 game played 1 draw
        else:
            leaderBoard.append([playerName, + 1, + 0, + 0]) # Else the player must have lost so we add new player with just 1 game played

# Function: displayLeaderBoard - Outputs the up to date leader board to the game
def displayLeaderBoard():
    # Import Global Variables
    global leaderBoard

    # Algorithm to sort the leader board
    for i in range(0, len(leaderBoard) -1):
        for j in range(i+1, len(leaderBoard)):
            if leaderBoard[i][2] / leaderBoard[i][1] < leaderBoard[j][2] / leaderBoard[j][1]:
                leaderBoard[i], leaderBoard[j] = leaderBoard[j], leaderBoard[i]

    print("\033[1m\033[4mPlayer\tWin %\tDraw %\tLoss %\033[0m") # Prints header for the leader board
    for player in leaderBoard: # For eacg player in the leader board
        winPercent = player[2] / player[1] * 100 # Calculates players win percentages and stores in local variable
        drawPercent = player[3] / player[1] * 100 # Calculates players draw percentages and stores in local variable
        gamesLost = 100 - (winPercent + drawPercent) # Calculates players loss percentages by subtracting the win percent + draw percent from 100 and stores in local variable
        print(player[0] + "\t" + format(winPercent, ".1f") + "\t" + format(drawPercent, ".1f") + "\t" + format(gamesLost, ".1f")) # Takes the data from the leader board list and outputs to the game, outputs percentages to 1 decimal place
    print() # Seperator

# Function: writeLeaderBoardFile - Writes the updated players and scores to the leaderboard file
def writeLeaderBoardFile():
    # Import global variables
    global leaderBoard

    try:
        leaderBoardFile = open("leaderboard.dat", "w") # Trts to open the leaderboard file with write privileges
    except Exception:
        print("Unable to overwrite the leader board file, any changes you have made have been lost") # If it can't load the file then it throws an exception and displays an error message
    else:
        for player in leaderBoard: # For each player in the leader board
            leaderBoardFile.write(player[0] + "," + str(player[1]) + "," + str(player[2]) + "," + str(player[3]) + "\n") # Writes the updated information to the file
        leaderBoardFile.close() # Closes the leaderBoardFile

# Function: cpuWinnnigMove - Function for the computer AI to check for and make a winning move
def cpuWinningMove():
    # Import Global Variables
    global gameBoard
    global diagonalCheck
    validMove = False

    attackCheck = [ ["E", cpu , cpu], [cpu, "E", cpu], [cpu, cpu, "E"] ] # List of what a row looks like for cpu winning move. This will be used for cpu to check when it can win.
    attackMove = [cpu, cpu , cpu] # List to store the cpu winning move

    # Fills the diagonalCheck list
    for i in range (0, len(gameBoard)):
        for j in range (0, len(gameBoard)):
            if gameBoard[i][i] != "E":
                diagonalCheck[j][i] = gameBoard[i][i]
    # Row Checks
            if not validMove: # If move is not valid
                if gameBoard[i] == attackCheck[j]: # Checks if cpu can win on a row
                    gameBoard[i] = attackMove # If available gameboard changes the row to the winning move
                    validMove = True # Valid Move becomes true
    # Column Checks
                elif [gameBoard[0][i], gameBoard[1][i], gameBoard[2][i]] == attackCheck[j] and gameBoard[j][i] == "E": # Checks if cpu can win on a column
                    gameBoard[j][i] = (cpu) # If available the gameboard changes the column to the winning move
                    validMove = True # Valid Move becomes true
    # Diagonal Checks
                elif diagonalCheck[i] == attackCheck[j] and gameBoard[j][j] == "E": # Checks the diagonal check list for a potential winning move
                    gameBoard[j][j] = (cpu) # If available the gameboard changes the diagonal to the winning move
                    validMove = True # Valid Move becomes true
                elif [gameBoard[2][0], gameBoard[1][1], gameBoard[0][2]] == [cpu, cpu, "E"]: # Checks the game board for a potential winning move
                    gameBoard[0][2] = (cpu) # If available the gameboard changes the diagonal to the winning move
                    validMove = True # Valid Move becomes true
                elif [gameBoard[0][2],  gameBoard[1][1], gameBoard[2][0]]  == [cpu, cpu, "E"]: # Checks the game board for a potential winning move
                    gameBoard[2][0] = (cpu) # If available the gameboard changes the diagonal to the winning move
                    validMove = True # Valid Move becomes true
                elif [gameBoard[0][2], gameBoard[2][0], gameBoard[1][1]] == [cpu, cpu, "E"]: # Checks the game board for a potential winning move
                    gameBoard[1][1] = (cpu) # If available the gameboard changes the diagonal to the winning move
                    validMove = True # Valid Move becomes true
    if not validMove: # If no winning move was available then we check for a defensive move
        cpuDefensiveMove() # Defensive move function

# Function: DefensiveMove - Function for the computer AI to check for and make a defensive move
def cpuDefensiveMove():
    # Import Global Variables
    global gameBoard
    global diagonalCheck
    validMove = False

    defenseCheck = [ ["E", player , player], [player, "E", player], [player, player, "E"] ] # List of what a row looks like for cpu defensive move. This will be used for cpu to check when it needs to defend from a player winning move.
    defenseMove = [ [cpu, player , player], [player, cpu, player], [player, player, cpu] ] # List to store the cpu defensive moves

    # Row Checks
    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard)):
            if not validMove: # If move is not valid
                if gameBoard[i] == defenseCheck[j]: # Checks if player is lining up to win a row
                    gameBoard[i] = defenseMove[j] # Makes defensive move from defenseMove list
                    validMove = True # Valid Move becomes true
    # Column Checks
                elif [gameBoard[0][i], gameBoard[1][i], gameBoard[2][i]] == defenseCheck[j] and gameBoard[j][i] == "E": # Checks if cpu needs to defend a column
                    gameBoard[j][i] = (cpu) # If needed the gameboard changes the column to the defensive move
                    validMove = True # Valid Move becomes true
    # Diagonal Checks
                elif diagonalCheck[i] == defenseCheck[j] and gameBoard[j][j] == "E" : # Checks if cpu needs to defend a diagonal
                    gameBoard[j][j] = (cpu) # Makes defensive move if needed
                    validMove = True # Valid Move becomes true
                elif [gameBoard[2][0], gameBoard[1][1], gameBoard[0][2]] == [player, player, "E"]: # Checks if cpu needs to defend a row
                    gameBoard[0][2] = (cpu) # Makes defensive move if needed
                    validMove = True # Valid Move becomes true
                elif [gameBoard[0][2],  gameBoard[1][1], gameBoard[2][0]]  == [player, player, "E"]: # Checks if cpu needs to defend a row
                    gameBoard[2][0] = (cpu) # Makes defensive move if needed
                    validMove = True # Valid Move becomes true
                elif [gameBoard[0][2], gameBoard[2][0], gameBoard[1][1]] == [player, player, "E"]: # Checks if cpu needs to defend a row
                    gameBoard[1][1] = (cpu) # Makes defensive move if needed
                    validMove = True # Valid Move becomes true
    if not validMove: # If no defensive move was available then we check if a stragtegic move can be made
        cpuStrategicMove() # Strategic move function

# Function: cpuStrategicMove - Function for the computer AI to check for and make a strategic move
def cpuStrategicMove():
    # Import Global Variables
    global gameBoard
    global diagonalCheck
    validMove = False

    strategicCheck = [ ["E", cpu , "E"], ["E", "E", cpu], [cpu, "E", "E"] ] # List of what a row looks like for cpu strategic move. This will be used for cpu to check when it can build upon a row towards a winning move
    strategicMove = [ [cpu, cpu , "E"], ["E", cpu , cpu], [cpu, cpu , "E"] ] # List to store the cpu strategic moves

    # Row Checks
    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard)):
            if not validMove: # If move is not valid
                if gameBoard[i] == strategicCheck[j]: # Checks if a strategic row move is available
                    gameBoard[i] = strategicMove[j] # Makes the stratgic move
                    validMove = True # Valid Move becomes true
    # Column Checks
                elif [gameBoard[0][i], gameBoard[1][i], gameBoard[2][i]] == strategicCheck[j] and gameBoard[j][i] == "E": # Checks if a strategic column move is available
                    gameBoard[j][i] = (cpu) # Makes the stratgic move
                    validMove = True # Valid Move becomes true
    # Diagonal Checks
                elif diagonalCheck[i] == strategicCheck[j] and gameBoard[j][j] == "E": # Checks if a strategic diagonal move is available
                    gameBoard[j][j] = (cpu) # Makes the stratgic move
                    validMove = True # Valid Move becomes true
                elif [gameBoard[2][0], gameBoard[1][1], gameBoard[0][2]] == [cpu, "E", "E"]: # Checks if a strategic diagonal move is available
                    gameBoard[1][1] = (cpu) # Makes the stratgic move
                    validMove = True # Valid Move becomes true
                elif [gameBoard[0][2], gameBoard[2][0], gameBoard[1][1]] == [cpu, "E", "E"]: # Checks if a strategic diagonal move is available
                    gameBoard[1][1] = (cpu) # Makes the stratgic move
                    validMove = True # Valid Move becomes true
    if not validMove: # If no strategic move was available then cpu will make a random move
        cpuRandomMove() # Random move function

# Function: cpuRandomMove - Function for the computer AI to make a random move - Only used when a winning, defensive or strategic moves is not available
def cpuRandomMove():
    # Import global variables
    global gameBoard

    validMove = False # Variable to act as a validity switch for our while loop. While loop will continue until criteria is met and validity switch becomes True

    while not validMove: # While validMove is False.
        i = random.randint(0, 2) # Sets i to a random number between 0 and 2
        j = random.randint(0, 2) # Sets j to a random number between 0 and 2
        if gameBoard[i][j] == "E": # Checks the randomly created space is empty and therefore a valid move
            gameBoard[i][j] = (cpu) # If space isn't taken the the board is updated with the players letter and validity switch becomes true and the while loop can end
            validMove = True

#####################
# Main Program Code #
#####################
printGameTitle() # Prints Game Title
readLeaderBoardFile() # Reads in the leaderboard file. If file does not exist it will output an empty leaderboard
getValidPlayerName("Please enter your initials (must be 3 alphabetic characters) or type 'Quit' at any time during the game to exit: ","Invalid Input - Please Try Again") # Asks player for their initials. Gives two perameters 'prompt' and 'errorMessage'
beginGame() # Begins the game
writeLeaderBoardFile() # Writes the updated players and scores to the leaderboard file