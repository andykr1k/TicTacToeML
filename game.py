import numpy as np
from nn import *

class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.board = np.zeros((3, 3))
        self.legal_moves = [i for i in range(9)]

    def Human(self):
        r = int(input("Row: "))
        c = int(input("Col: "))
        while(self.Move(r,c)==False):
            print(self.board)
            r = int(input("Row: "))
            c = int(input("Col: "))
        self.ChangeLegalMoves(r,c)

    def AI(self):
        best_score = float('-inf')
        best_move = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    self.board[i][j] = -1
                    score = minimax(self, 0, False)
                    self.board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        r = best_move[0]
        c = best_move[1]
        self.Move(r,c)
        self.ChangeLegalMoves(r,c)

    def CheckForWin(self):
        if not any(0 in row for row in self.board):
            return True

        for row in self.board:
            if 1 in row and np.all(row == 1):
                return True
            elif -1 in row and np.all(row == -1):
                return True

        for col in self.board.transpose():
            if 1 in col and np.all(col == 1):
                return True
            elif -1 in col and np.all(col == -1):
                return True

        for diag in [self.board.diagonal(), np.fliplr(self.board).diagonal()]:
            if 1 in diag and np.all(diag == 1):
                return True
            elif -1 in diag and np.all(diag == -1):
                return True

        return False

    def CheckForWinner(self):
        for row in self.board:
            if 1 in row and np.all(row == 1):
                return 'X wins'
            elif -1 in row and np.all(row == -1):
                return 'O wins'

        for col in self.board.transpose():
            if 1 in col and np.all(col == 1):
                return 'X wins'
            elif -1 in col and np.all(col == -1):
                return 'O wins'

        for diag in [self.board.diagonal(), np.fliplr(self.board).diagonal()]:
            if 1 in diag and np.all(diag == 1):
                return 'X wins'
            elif -1 in diag and np.all(diag == -1):
                return 'O wins'

        if not any(0 in row for row in self.board):
            return 'Draw!'

        return 'No winner yet'

    def ChangeTurn(self):
        self.turn ^= 1

    def ChangeLegalMoves(self, row, col):
        num = row * 3 + col
        if num in self.legal_moves:
            self.legal_moves.remove(num)


    def Move(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            print("Invalid input. Please enter integers for row and col.")
            return False

        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid row or column index. Please enter valid indices.")
            return False

        if self.board[row][col] != 0:
            print("Invalid input. The spot has already been played.")
            return False

        piece = 1 if self.turn == 0 else -1

        self.board[row][col] = piece
        return True