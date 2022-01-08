"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    k=0;
    for i in range (3):
        for j in range (3):
           if(board[i][j]==EMPTY):
               k=k+1

    if(k%2==0):
        return O
    else:
        return X   
     
   # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a=[]
    for i in range (3):
        for j in range (3):
           if(board[i][j]==EMPTY):
              a.append([i,j]) 
    return a
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board1=copy.deepcopy(board)
    L=player(board1)
    i=action

    if(board1[i[0]][i[1]]==EMPTY):

        board1[i[0]][i[1]]=L
        return board1
    else:
        raise Exception("Invalid move")
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]):
            return board[i][1]
            
    for j in range(3):
        if(board[0][j]==board[1][j]==board[2][j]):
            return board[1][j]   
    if(board[0][0]==board[1][1]==board[2][2] ):
        return board[0][0]
    if(board[0][2]==board[1][1]==board[2][0]):
        return board[1][1]
    else:
        return None       
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if( winner(board)==None):
        k=0
        for i in range (3):
            for j in range (3):
             if(board[i][j]==EMPTY):
                k=k+1
        if(k==0):
            return True
        else:
            return False   
    else:
        return True                
        
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    L=winner(board)
    if(L==X):
        return 1;
    if(L==O):
        return -1;
    else:
        return 0;       

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
    
    
