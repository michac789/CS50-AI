"""
Tic Tac Toe Player
"""

import math
import copy
from random import randint

X = "X"
O = "O"
EMPTY = None


def initial_state():
    # Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Returns player who has the next turn on a board. (checked)
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
    return O


def actions(board):
    # Returns set of all possible actions (i, j) available on the board. (checked)
    valid_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                valid_moves.add((i, j))
    return valid_moves


def result(board, action):
    # Returns the board that results from making move (i, j) on the board. (checked)
    board_temp = copy.deepcopy(board)
    if board_temp[action[0]][action[1]] == None:
        board_temp[action[0]][action[1]] = player(board)
    else:
        raise IndexError()
    return board_temp


def winner(board):
    # Returns the winner of the game, if there is one. (checked)
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
                elif board[1][1] == O:
                    return O
    return None


def terminal(board):
    # Returns True if game is over, False otherwise. (checked)
    if winner(board) != None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise. (checked)
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    return 0


def scoretracker(board, alpha, beta):
    # Return the highest possible score if maximize is True, else return lowest possible score of the move (checked)
    if terminal(board) == True:
        return utility(board)
    possible_moves = list(actions(board))
    if player(board) == X:
        initial_score = -2
        for moves in range(len(possible_moves)):
            score = scoretracker(result(board, list(possible_moves)[moves]), alpha, beta)
            initial_score = max(initial_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
    elif player(board) == O:
        initial_score = 2
        for moves in range(len(possible_moves)):
            score = scoretracker(result(board, list(possible_moves)[moves]), alpha, beta)
            initial_score = min(initial_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
    return initial_score


def minimax(board):
    # Returns the optimal action for the current player on the board. (checked)
    if terminal(board) == True:
        return None
    possible_moves = list(actions(board))
    optimal_move = (-1, -1)
    if player(board) == X:
        score = -2
        for moves in range(len(possible_moves)):
            board_simulation = result(board, list(possible_moves)[moves])
            if scoretracker(board_simulation, -2, 2) > score:
                score = scoretracker(board_simulation, -2, 2)
                optimal_move = possible_moves[moves]
            # if there are more than 1 optimal move, the computer do not always choose the exact same one
            elif scoretracker(board_simulation, -2, 2) == score: 
                if randint(0, 1) == 0:
                    score = scoretracker(board_simulation, -2, 2)
                    optimal_move = possible_moves[moves]
    elif player(board) == O:
        score = 2
        for moves in range(len(possible_moves)):
            board_simulation = result(board, list(possible_moves)[moves])
            if scoretracker(board_simulation, -2, 2) < score:
                score = scoretracker(board_simulation, -2, 2)
                optimal_move = possible_moves[moves]
            # if there are more than 1 optimal move, the computer do not always choose the exact same one
            elif scoretracker(board_simulation, -2, 2) == score:
                if randint(0, 1) == 0:
                    score = scoretracker(board_simulation, -2, 2)
                    optimal_move = possible_moves[moves]
    return optimal_move

