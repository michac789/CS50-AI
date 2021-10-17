"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    # Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Returns player who has the next turn on a board.
    x_pieces = 0
    o_pieces = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_pieces += 1
            elif board[i][j] == O:
                o_pieces += 1
    if x_pieces == o_pieces:
        return X
    elif x_pieces == o_pieces + 1:
        return O
    else:
        return 'E'


def actions(board):
    # Returns set of all possible actions (i, j) available on the board.
    valid_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                valid_moves.add((i, j))
    return valid_moves


def result(board, action):
    # Returns the board that results from making move (i, j) on the board.
    board_temp = copy.deepcopy(board)
    if board_temp[action[0]][action[1]] == None:
        board_temp[action[0]][action[1]] = player(board)
    else:
        raise 'Invalid Move'
    return board_temp


def winner(board):
    # Returns the winner of the game, if there is one.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][2] == X:
                return X
            elif board[i][2] == O:
                return O
        if board[0][i] == board[1][i] == board[2][i]:
            if board[2][i] == X:
                return X
            elif board[2][i] == O:
                return O
        if i < 2:
            if board[0][0 + i * 2] == board[1][1] == board[2][2 - i * 2]:
                if board[1][1] == X:
                    return X
                elif board[2][2] == O:
                    return O
    return None


def terminal(board):
    # Returns True if game is over, False otherwise.
    if winner(board) != None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
