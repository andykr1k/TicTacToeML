import streamlit as st
from game import *

def init_game():
    game = TicTacToe()
    return {
        'opponent': 'AI',
        'game': game,
        'board': game.board,
        'player': 'X',
        'warning': False,
        'winner': None,
        'over': False,
        'win': {'X': 0, 'O': 0}
    }

def main():
    if 'game_state' not in st.session_state:
        st.session_state.game_state = init_game()

    game_state = st.session_state.game_state

    st.write(
        """
        # ❎🅾️ Tic Tac Toe
        """
    )

    reset, score, player = st.columns([1, 1, 1])
    reset.button('New game', on_click=init_game)

    grid_columns = st.columns(3)

    for i in range(3):
        for j in range(3):
            cell_value = game_state['board'][i, j]
            button_key = f"{i}-{j}"

            if cell_value == 0 and not game_state['winner']:
                if game_state['player'] == 'X':
                    if grid_columns[j].button('', key=button_key, on_click=make_move, args=(i, j)):
                        pass
                else:
                    make_ai_move(game_state)
            else:
                grid_columns[j].write(get_display_value(cell_value), width=100, height=100, font_size=36,
                                       horizontal_alignment='center', vertical_alignment='center')

    if game_state['winner']:
        st.write(game_state['winner'])

    score.button(f'❌{game_state["win"]["X"]} 🆚 {game_state["win"]["O"]}⭕')
    player.button(
        f'{"❌" if game_state["player"] == "X" else "⭕"}\'s turn'
        if not game_state['winner']
        else f'🏁 Game finished'
    )

def make_move(i, j):
    game_state = st.session_state.game_state
    if game_state['player'] == 'X':
        game_state['game'].Move(i, j)
        game_state['board'] = game_state['game'].board
        game_state['player'] = 'O'
        make_ai_move(game_state)

def make_ai_move(game_state):
    if game_state['player'] == 'O':
        game_state['game'].AI()
        game_state['board'] = game_state['game'].board
        game_state['player'] = 'X'

def get_display_value(value):
    if value == 1:
        return 'X'
    elif value == -1:
        return 'O'
    else:
        return ''

if __name__ == '__main__':
    main()