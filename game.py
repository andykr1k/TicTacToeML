import numpy as np

class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.board = np.zeros((3, 3))
        self.legal_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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
        if not any(0 in row for row in self.board):
            return 'Draw!'
        
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
            return

        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid row or column index. Please enter valid indices.")
            return

        if self.board[row][col] != 0:
            return

        piece = 1 if self.turn == 0 else -1

        self.board[row][col] = piece
