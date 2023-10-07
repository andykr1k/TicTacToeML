from game import *

def main():
    # x, y = GetData()

    # X_train, X_test, y_train, y_test = TrainSplit(x,y)

    # model = create_model()

    # loss, acc = train_model(model, X_train, y_train, X_test, y_test)

    # print("Loss: " + str(loss) + ", Accuracy: " + str(acc))

    game = TicTacToe()

    while(game.CheckForWin() == False):
        print("Your Turn" if game.turn == 0 else "AI Turn")
        print("Legal Moves: ", game.legal_moves)
        print(game.board)

        if game.turn == 0:
            game.Human()
        else:
            game.AI()
        game.ChangeTurn()

    winner = game.CheckForWinner()

    print(game.board)
    print(winner)

if __name__ == "__main__":
    main()
