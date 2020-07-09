from math import inf 
import random
import numpy as np

""" 
    An implementation Tic Tac Toe
    game using minimax Ai Algorithm 
    with alpha-beta pruning
    in python.
"""



def eval(board):
"""
    Heuristic Approach:
    This function is the evaluation of each state.
    The input considered is the present state and this outputs +10 if computer i.e., Ai 
    wins , -10 if human wins the game and 0 if none of them win i.e., NOT the terminal(winning) case or is a draw
""" 
    for i in range(len(board)):
        # checking for the case when all the values in the same row are equal and not empty
        if board[i][0]!='-' and all(x==board[i][0] for x in board[i]):
            if board[i][0]=='X': #when all are  'X' 
                return 10
            else:# when all are  "O"
                return -10
    for i in range(len(board)):
        #checking for the case when all the values in the column are equal and not empty
        k=np.array(board)
        k=k.T
        if board[0][i]!='-' and all(x==k[i][0] for x in k[i]):
            if board[0][i]=='X':# when all are 'X'
                return 10
            else: # when all are 'O'
                return -10
    
    if  board[0][0]!='-' and all(board[x][x]==board[0][0] for x in range(len(board)) ) :
        #checking the diagonal
        if board[0][0]=='X' :
            return 10
        else:
            return -10
    if board[0][len(board)-1]!='-' and all(board[x][len(board)-x-1]==board[0][len(board)-1] for x in range(len(board))):
        #checking the other diagonal 
        if board[0][len(board)-1]=='X':
            return 10
        else:
            return -10
    return 0
def movesleft(board):
"""
    this function takes in the state as the input and outputs True 
    if any moves are left i.e., if any empty spaces left else False.
"""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='-':
                return True
    return False
"""
    Minimax algorithm with Alpha-beta Pruning
    Alpha-beta pruning is used to decrease the nodes that are to be evaluated
    where alpha is the best value the maximizer can guarantee at the given level or above
    and beta is the best value the minimizer can guarantee at the given level or above.
"""
def minimax(board,depth,ismax,alpha,beta,given_depth):
"""
    This functions choices out the best move
    Input: the state, the depth which is actually the depth of the minimax tree 
    ,alpha ,beta  and the given_depth which is entered by the user for varying the difficulty of the game
"""

    score=eval(board)
    if score==10: # winning case
        return score-depth
    if score==-10: #winning case
        return score+depth
    if given_depth==depth: 
        return score
    if movesleft(board)==False:#terminal but not winning case
        return 0
    if ismax==True: #Maximizer
        best_score=-inf
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='-':
                    board[i][j]='X'
                    best_score=max(best_score,minimax(board,depth+1,False,alpha,beta,given_depth)) #recursive call for the minimax function and maximum best_score finds the max score obtained till then
                    board[i][j]='-'
                    alpha=max(best_score,alpha)
                    if beta<=alpha:
                        break
        return best_score
    else: #Minimizer
        best_score=+inf
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='-':
                    board[i][j]='O'
                    best_score=min(best_score,minimax(board,depth+1,True,alpha,beta,given_depth)) #minimum bestscore obtained till then
                    board[i][j]='-'
                    beta=min(best_score,beta)
                    if beta<=alpha: 
                        break
        return best_score
''' Best move at a given state'''
def bestmove(board,given_depth):
    move=[-1,-1]
    bestval=-inf
    best_array=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='-':
                board[i][j]='X' #maximizer's best move 
                moveval=minimax(board,0,False,-inf,inf,given_depth)
                board[i][j]='-'
                if moveval>=bestval:
                    move[0]=i
                    move[1]=j
                    bestval=moveval #best score
                    best_array.append([list(move),bestval])
    k=max(map(lambda x:x[1],best_array))
    best_moves=[]
    '''
    this following 'for' loop is for the case when the bestscore's are equal for varying moves
    that are on the same level
    '''
    for i in range(len(best_array)):
        if k==best_array[i][1]:
            best_moves.append(best_array[i][0])
    return random.choice(best_moves) #returns a move among all the best moves available
#if eval returns True then the game ends with a player winning
def is_win(board): 
    if eval(board)!=0:
        return True
    else:
        return False
"""
    very similar to the movesleft function
"""
def is_end(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='-':
                return False
    return True
'''
    prints the tic tac toe or the matrix (dimxdim)
'''
def print_board(board):
    for i in range(len(board)):
            print(' '.join(board[i]))
    print()
'''
    This function is used in the case of depth 0.
    Returns all the moves that are not filled
'''
def all_moves_left(board):
    moves=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='-':
                moves.append([i,j])
    return moves
'''
    This function takes input as the name of the player who starts
    the game first, the starting state i.e., all empty values 
    and the depth
'''
def play(player,board,depth):
    if player=="ai":
        while(is_end(board))==False:
            move=bestmove(board,depth) #gives a random best move  
            board[move[0]][move[1]]='X'
            if is_win(board)==True:
                print("Computer Wins!") #checks if there is a winning case if yes prints the statement and breaks out of the loop
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!") #this is when there is no empty space and no winning case
                break
        ''' 
            Human enters a move in the form of "x y" where 
            x denotes the row  starting 0 to dim
            and y denotes the column starting 0 to dim
        '''
            x,y=map(int,input().split()) 
            if board[x][y]!='-': # check for when the player enters a coordinate which has no empty value
                print("invalid move!enter again") 
                x,y=map(int,input().split())
            board[x][y]='O'
            if is_win(board)==True:
                print("human Wins!")  #check if human wins 
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!")
                break
    '''
    similar to the if statement above but here the human plays first
    '''
    elif player=="human":
        while is_end(board)==False:
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move!enter again")
                x,y=map(int,input().split())
            board[x][y]='O'
            if is_win(board)==True:
                print("human Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!")
                break
            move=bestmove(board,depth)
            board[move[0]][move[1]]='X'
            if is_win(board)==True:
                print("Computer Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!")
                break
'''
    This function is when the depth is 0 i.e., no involvement of AI
    ,just a random function to select a place in AI's turn
'''
def play_0(board,player):
    if player=="human":
        while is_end(board)==False:
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move!enter again")
                x,y=map(int,input().split())
            board[x][y]='O'
            if is_win(board)==True:
                print("human Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
            move=random.choice(all_moves_left(board)) #random function to select out of all moves left
            board[move[0]][move[1]]="X"
            if is_win(board)==True:
                print("Computer Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!")
                break
    elif player=="ai":
        while is_end(board)==False:
            move=random.choice(all_moves_left(board))
            board[move[0]][move[1]]="O"
            if is_win(board)==True:
                print("Computer Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move!enter again")
                x,y=map(int,input().split())
            board[x][y]='X'
            if is_win(board)==True:
                print("Human Wins!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("It's a Tie!")
                break
''' 
    For the case when human plays with human.Again,no involvement of Ai.
    input : the state and the frst player name
'''
def play_hvsh(board,player):
    if player=="X":
        print_board(board)
        while is_end(board)==False:
            print("player X's turn")
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move ! enter again")
                x,y=map(int,input().split())
            board[x][y]='X'
            if is_win(board):
                print("player X wins the game!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
            print("player O's turn")
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move ! enter again")
                x,y=map(int,input().split())
            board[x][y]='O'
            if is_win(board):
                print("player O wins the game!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
    elif player=='O':
        print_board(board)
        while is_end(board)==False:
            print("player O's turn")
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move ! enter again")
                x,y=map(int,input().split())
            board[x][y]='O'
            if is_win(board):
                print("player O wins the game!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
            print("player X's turn")
            x,y=map(int,input().split())
            if board[x][y]!='-':
                print("invalid move ! enter again")
                x,y=map(int,input().split())
            board[x][y]='X'
            if is_win(board):
                print("player X wins the game!")
                print_board(board)
                break
            print_board(board)
            if movesleft(board)==False:
                print("its a tie!")
                break
if __name__=="__main__":
    print("select mode:") #select a mode of the 2 options given below
    print("enter 1 for human vs human")
    print("enter 2 for Ai vs human")
    mode=int(input()) #enter 1 or 2
    print("Enter dimension: any number from 3 to 5") 
    dim=int(input()) #enter an integer from 3 to 5 (inclusive)
    board=[]
    for i in range(dim):
        board.append(['-']*dim) #create a board of size dim x dim
    if mode==2: #for ai vs human
        print("enter depth")
        depth=int(input()) #enter a difficulty level from 0 to 4
        print("enter first player")
        player=input() #frst player either "ai" or "human"
        if depth==0:
            play_0(board,player) #handles the depth 0 case
        else:
            play(player,board,depth)
    elif mode==1: #for human vs human
        print("enter first player X or O(case senitive)") 
        player=input() # enter frst player as either 'X' or 'O'
        play_hvsh(board,player)
        
    
    
            






