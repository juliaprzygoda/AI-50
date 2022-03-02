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

    X_count = 0
    O_count = 0

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                X_count += 1
            elif board[row][col] == O:
                O_count += 1
            else:
                continue;

    # Check if the board is empty
    if X_count == 0 and O_count == 0:
        return X
    elif X_count > O_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                action = (row, col)
                possible_actions.add(action)
            else:
                continue
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Copy the board
    result = copy.deepcopy(board)

    # Append copied table with result
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check vertically
    for row in range(len(board)):
        X_count = 0
        O_count = 0
        for col in range(len(board)):
            if board[row][col] == X:
                X_count += 1
            elif board[row][col] == O:
                O_count += 1
        if X_count == 3:
            return X
        elif O_count == 3:
            return O
        else:
            continue

    # Check vertically
    for col in range(len(board)):
        X_count = 0
        O_count = 0
        for row in range(len(board)):
            if board[row][col] == X:
                X_count += 1
            elif board[row][col] == O:
                O_count += 1
        if X_count == 3:
            return X
        elif O_count == 3:
            return O
        else:
            continue

    # Check diagonally
    if (board[0][0] == X and board[1][1] == X and board [2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board [2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check winner
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def Max_Value(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, Min_Value(result(board, action)))
        return v

    def Min_Value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, Max_Value(result(board, action)))
        return v


    if terminal(board):
        return None
    else:
        if player(board) == X:
            v = float("-inf")
            for action in actions(board):
                x = Min_Value(result(board, action))
                if x > v:
                    v = x
                    move = action
        elif player(board) == O:
             v = float("inf")
             for action in actions(board):
                 x = Max_Value(result(board, action))
                 if x < v:
                     v = x
                     move = action

    return move