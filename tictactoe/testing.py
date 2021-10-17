from tictactoe import player, actions, result, winner, terminal, utility, minimax, scoretracker


def main():
    board1 = [[None, None, None], [None, None, None], [None, None, None]]
    board2 = [[None, None, None], [None, 'X', None], [None, None, None]]
    board3 = [[None, 'X', None], ['O', None, None], ['O', 'X', None]]
    board4 = [['X', None, None], ['X', 'O', None], [None, None, None]]
    board5 = [['X', 'O', 'O'], ['X', 'O', None], [None, None, 'X']]
    board6 = [['X', 'O', 'O'], ['X', 'X', None], ['O', None, 'X']]
    board7 = [['X', None, 'O'], ['X', 'O', None], ['O', None, 'X']]
    board8 = [['O', 'X', None], [None, 'X', None], ['O', 'X', None]]
    board9 = [['X', None, 'X'], ['X', 'X', None], ['O', 'O', 'O']]
    board10 = [['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'O']]
    print(f"player 1: {player(board1)}, 2: {player(board2)}, 3: {player(board3)}, 4: {player(board4)}, 5: {player(board5)}")
    print(f"action 1: {actions(board1)}, 2: {actions(board2)}, 3: {actions(board3)}, 4: {actions(board4)}, 5: {actions(board5)}, 10: {actions(board10)}")
    print(f"result 1: {result(board1, (1, 2))}, 2: {result(board2, (0, 1))}, 3: {result(board3, (1,1))}, 4: {result(board4, (2,0))}")
    #print(f"5: {result(board5, (0, 1))}") #raise index error here
    print(f"winner 1: {winner(board1)}, 2: {winner(board2)}, 3: {winner(board3)}, 4: {winner(board4)}, 5: {winner(board5)}", end="")
    print(f", 6: {winner(board6)}, 7: {winner(board7)}, 8: {winner(board8)}, 9: {winner(board9)}, 10: {winner(board10)}")
    print(f"terminal 1: {terminal(board1)}, 2: {terminal(board2)}, 3: {terminal(board3)}, 4: {terminal(board4)}, 5: {terminal(board5)}", end="")
    print(f", 6: {terminal(board6)}, 7: {terminal(board7)}, 8: {terminal(board8)}, 9: {terminal(board9)}, 10: {terminal(board10)}")
    print(f"utility 1: {utility(board1)}, 2: {utility(board2)}, 3: {utility(board3)}, 4: {utility(board4)}, 5: {utility(board5)}", end="")
    print(f", 6: {utility(board6)}, 7: {utility(board7)}, 8: {utility(board8)}, 9: {utility(board9)}, 10: {utility(board10)}")
    print(f"minimax 1: {minimax(board1)}, 2: {minimax(board2)}, 3: {minimax(board3)}, 4: {minimax(board4)}, 5: {minimax(board5)}", end="")
    print(f", 6: {minimax(board6)}, 7: {minimax(board7)}, 8: {minimax(board8)}, 9: {minimax(board9)}, 10: {minimax(board10)}")
    print(f"scoretracker 1: {scoretracker(board1, -2, 2)}, 2: {scoretracker(board2, -2, 2)}, 3: {scoretracker(board3, -2, 2)}, 4: {scoretracker(board4, -2, 2)}, 5: {scoretracker(board5, -2, 2)}", end="")
    print(f", 6: {scoretracker(board6, -2, 2)}, 7: {scoretracker(board7, -2, 2)}, 8: {scoretracker(board8, -2, 2)}, 9: {scoretracker(board9, -2, 2)}, 10: {scoretracker(board10, -2, 2)}")


main()
