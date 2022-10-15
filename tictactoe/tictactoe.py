"""
Tic Tac Toe Player
"""

import math
import random # for the minimax function
from copy import deepcopy # for the function result

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
    if (board == [[EMPTY, EMPTY, EMPTY], 
                  [EMPTY, EMPTY, EMPTY], 
                  [EMPTY, EMPTY, EMPTY]]) : return X
    else: 
        compt_x = 0
        compt_o = 0
        for el in board:
            for i in range(len(el)):
                if (el[i]==X) : compt_x+=1
                elif (el[i]==O) : compt_o+=1
        if compt_x > compt_o : return O
        else: return X
        
  
                
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos = set()
    for j in range(len(board)):
        for i in range(len(board)):
            if (board[i][j]==EMPTY) : pos.add((i,j))
    return pos
            
            
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the choosen move is valid:
        
    if (action[0] not in [0, 1, 2] or action[1] not in [0, 1, 2]):
      raise Exception('Result function given an invalid board position for action: ')
    elif (board[action[0]][action[1]] != EMPTY):
      raise Exception('Result function tried to perform invalid action on occupied tile: ')

    copy = deepcopy(board)
    copy[action[0]][action[1]] = player(board)

    return copy
        


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # For X :
        
    # The 2 diagonals :
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X):
        return X
    elif (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    
    # The vertical ligns :
    elif (board[0][0] == X and board[1][0] == X and board[2][0] == X):
        return X
    elif (board[0][1] == X and board[1][1] == X and board[2][1] == X):
        return X
    elif (board[0][2] == X and board[1][2] == X and board[2][2] == X):
        return X
    
    # The horizontal ligns :
    elif (board[0][0] == X and board[0][1] == X and board[0][2] == X):
        return X
    elif (board[1][0] == X and board[1][1] == X and board[1][2] == X):
        return X
    elif (board[2][0] == X and board[2][1] == X and board[2][2] == X):
        return X
    
    # For O :
        
    # The 2 diagonals :
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O):
        return O
    elif (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    
    # The vertical ligns :
    elif (board[0][0] == O and board[1][0] == O and board[2][0] == O):
        return O
    elif (board[0][1] == O and board[1][1] == O and board[2][1] == O):
        return O
    elif (board[0][2] == O and board[1][2] == O and board[2][2] == O):
        return O
    
    # The horizontal ligns :
    elif (board[0][0] == O and board[0][1] == O and board[0][2] == O):
        return O
    elif (board[1][0] == O and board[1][1] == O and board[1][2] == O):
        return O
    elif (board[2][0] == O and board[2][1] == O and board[2][2] == O):
        return O
    
    # If there is no winner :
    else : return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    compt = 0
    for el in board:
        for i in range(len(el)):
            if (el[i]==None) : compt+=1
    if winner(board) != None:
        return True
    elif compt == 0: return True
    else : return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winr = winner(board)
    if winr == X: return 1
    elif  winr == O: return -1
    elif terminal(board)==True : return 0


def find(element,liste):
    if element in liste:
        return 1
    else:
        return 0  
    
actions_expl = 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global actions_expl
    actions_expl = 0

    def max_player(board, best_min = 10):
      global actions_expl

      # If the game is over it returns board value :
      if terminal(board):
        return (utility(board), None)

      value = -10
      best_action = None

      # Get set of actions and then select a random one until list is empty:
      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to min_player if lower result already found:
        if best_min <= value:
          break

        actions_expl += 1
        min_player_result = min_player(result(board, action), value)
        if int(min_player_result[0]) > value:
          best_action = action
          value = min_player_result[0]

      return (value, best_action)


    def min_player(board, best_max = -10):
      global actions_expl

      if terminal(board):
        return (utility(board), None)

      # Else pick the action giving the min value when max_player plays optimally
      value = 10
      best_action = None

      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to max_player if higher result already found:
        if best_max >= value:
          break

        actions_expl += 1
        max_player_result = max_player(result(board, action), value)
        if int(max_player_result[0]) < value:
          best_action = action
          value = max_player_result[0]

      return (value, best_action)


    # Return None if the game is finished:
    if terminal(board):
      return None
    # else :
    if player(board) == X:
      print('AI is exploring possible actions...')
      best_move = max_player(board)[1]
      print('Actions explored by AI: ', actions_expl)
      return best_move
    else:
      print('AI is exploring possible actions...')
      best_move = min_player(board)[1]
      print('Actions explored by AI: ', actions_expl)
      return best_move
        
   
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
