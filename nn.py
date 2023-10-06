import numpy as np
import tensorflow as tf
from tensorflow import keras
from scipy.ndimage import rotate
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Dense

char_mapping = {'x': 1, 'o': -1, 'b': 0}
bool_mapping = {True: 1, False: 0}

def GetData():
    df = pd.read_csv('tic-tac-toe_csv.csv')
    df.replace(char_mapping, inplace=True)
    df.replace(bool_mapping, inplace=True)
    x = df.iloc[:, :-1].values
    y = df['class'].values
    return x, y

def create_model():
    model = keras.Sequential([
        Dense(256, activation='relu', input_shape=(9,)),
        Dense(128, activation='relu'),
        Dense(128, activation='relu'),
        Dense(32, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def TrainSplit(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    return test_loss, test_accuracy

def make_move(model, board, legal_moves):    
    flattened_board = board.flatten()

    predictions = model.predict(np.array([flattened_board]))

    for move_index in range(len(predictions)):
        if not legal_moves[move_index]:
            predictions[move_index] = -float('inf')

    print(predictions)

    move_index = np.argmax(predictions)
    row = move_index // 3
    col = move_index % 3
    print(row, col)
    return int(row), int(col)