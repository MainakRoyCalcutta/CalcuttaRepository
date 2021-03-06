"""
TIC TAC TOE GAME
Basic Using PlaceHolder Numbers: Top left corner as zero and bottom right corner 8
"""
#Board function
board = [" "] * 9
def my_board(board):
    print(" " + board[0] + "  | " + board[1] + " |  " + board[2] + " ")
    print(" --- --- --- ")
    print(" " + board[3] + "  | " + board[4] + " |  " + board[5] + " ")
    print(" --- --- --- ")
    print(" " + board[6] + "  | " + board[7] + " |  " + board[8] + " ")

#Accepting player choice for first player, the second player automatically get the the other symbol    
def player_choice():
    play = False
    print("Welcome to the Game\n")
    while play == False:
        pl = input("Do you want to Choose X or O : ")
        pl = pl.upper()
        if pl == "X":
            pl1 = "X"
            pl2 = "O"
            play = True
            print(f"PLAYER 1: {pl1} \nPLAYER 2: {pl2}")
        elif pl == "O":
            pl1 = "O"
            pl2 = "X"
            play = True
            print(f"PLAYER 1: {pl1} \nPLAYER 2: {pl2}")
        else:
            #Wrong Input's Output
            print("Wrong Input!!! Please Choose X or O")
            play = False
    return pl1, pl2

#Function to accept Player's choice input i.e. where the user wants to place its symbol and return the input position
def player_inpt():
    #Input is not taken as integer as if there was an non-number input, .isdigit condition canot be applied
    indx_inpt = input("Enter where you want to place (0 - 8) : ")
    while indx_inpt.isdigit() :
        if int(indx_inpt) < 9 and int(indx_inpt) > -1:
            if board[int(indx_inpt)] != "X" and board[int(indx_inpt)] != "O":
                break
            else:
                #If the place is already filled with any symbol then output
                print("You cannot overwrite!!")
                return player_inpt()
        else:
            #Invalid input's output if input range not between 0 or 8
            print("Invalid Input!! Enter an index between 0 to 8")
            return player_inpt()
    else:
        #Invalid input's output if input not a number
        print("Invalid Input!! Enter an index between 0 to 8")
        return player_inpt()
    return int(indx_inpt)

#Winning Condition
def winner(playr):
    a = [playr, playr, playr]
    if [board[0], board[1], board[2]] == a or [board[3], board[4], board[5]] == a or [board[6], board[7],
                                                                                      board[8]] == a:
        return 1
    elif [board[0], board[3], board[6]] == a or [board[1], board[4], board[7]] == a or [board[2], board[5],
                                                                                        board[8]] == a:
        return 1
    elif [board[0], board[4], board[8]] == a or [board[2], board[4], board[6]] == a:
        return 1
    else:
        pass

#Function for asking if user wants to play again
def play_agn():
    pl_agn = input("Do you want to play again ? (Y/N) : ")
    pl_agn = pl_agn.upper()
    while pl_agn == "Y":
        print("\n"*100)
        reset_board()
        replce(player_choice())
        pl_agn= "%"
        break
    else:
        if pl_agn == "N":
            print("Thank you")

#Final Function to replace the empty places by X or O
def replce(player_choice):
    pl1, pl2 =player_choice
    while set(board) != {"X", "O"}:
        print("Player 1")
        board[player_inpt()] = pl1
        print(my_board(board))
        if winner(pl1) == 1:
            print("GAME WON BY PLAYER 1")
            return play_agn()
            break
        if set(board) != {"X", "O"}:
            print("Player 2")
            board[player_inpt()] = pl2
            print(my_board(board))
            if winner(pl2) == 1:
                print("GAME WON BY PLAYER 2")
                return play_agn()
                break
    else:
        print("Match Draw")
        return play_agn()
#reset the used board
def reset_board():
    for _ in range(0,9):
        board[_] = " "
    my_board(board)

#Final Fuction calls    
my_board(board)
replce(player_choice())
