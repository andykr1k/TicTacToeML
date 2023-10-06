from game import *
from nn import *

def main():
    x, y = GetData()

    X_train, X_test, y_train, y_test = TrainSplit(x,y)

    model = create_model()

    loss, acc = train_model(model, X_train, y_train, X_test, y_test)

    print("Loss: " + str(loss) + ", Accuracy: " + str(acc))

    game = TicTacToe()

    while(game.CheckForWin() == False):
        print(game.board)
        if game.turn == 0:
            r = int(input("Row: "))
            c = int(input("Col: "))
            game.Move(r,c)
            game.ChangeLegalMoves(r,c)
        else:
            r, c = make_move(model, game.board, game.legal_moves)
            game.Move(r,c)
            game.ChangeLegalMoves(r,c)
        game.ChangeTurn()

    winner = game.CheckForWinner()

    print(winner)

if __name__ == "__main__":
    main()
