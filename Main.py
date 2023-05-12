import Interface as ui
import TicyTacyToey as TTT
import os

def main(game=TTT.TicTacToe(), window_size=800):
    ui.Interface(game, window_size)

if __name__ == '__main__':
    _game = TTT.TicTacToe(in_a_row=3, board_size=3)
    _window_size = 800
    main(_game, _window_size)
else:
    print("This file must be ran with the main file...{0}".format(os.path.basename(__file__)))