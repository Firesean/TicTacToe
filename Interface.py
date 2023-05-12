from Player import Player
import tkinter as tk
from tkinter import messagebox
class Interface:

    def __init__(self, game, window_size, root=tk.Tk()):
        # Root
        self.root = root

        # Declarations
        self.canvas = tk.Canvas(self.root,
                                width=window_size,
                                height=window_size)
        self.cursor = None
        self.game = game
        self.menu_bar = None
        self.player_menu = None
        self.reference = []
        self.window_size = window_size

        # Main
        self.set_binds()
        self.create_interface()
        self.set_menu()
        self.root.mainloop()

    def change_current_player(self) -> None:
        index = self.game.players.index(self.get_current_player())
        self.game.set_current_player(self.game.players[index-1])

    def clear_interface(self) -> None:
        self.reference = []
        self.canvas.delete("all")
        self.create_interface()


    def create_interface(self) -> None:
        self.cursor = self.canvas.create_text(0, 0, text="")
        self.draw_lines()
        self.canvas.pack()
        self.root.iconbitmap("FireIcon32x32.ico")
        self.root.title(type(self.game).__name__)
        self.root.geometry("{0}x{0}".format(self.window_size))

    def display_current_player(self, event=None) -> None:
        if event:
            initial = self.get_current_player().get_initial()
            self.canvas.itemconfigure(self.cursor, text=initial,
                                      font="TimesNewRoman {0} bold".format(int(self.get_offset()/self.game.get_board_size())))
            self.canvas.coords(self.cursor, event.x, event.y)

    def draw_lines(self) -> None:
        self.canvas.create_rectangle(2,2, self.get_window_size(), self.get_window_size())
        for line in range(self.game.get_board_size()):
            self.canvas.create_line(0, line*self.get_spacer(),
                                    self.get_window_size(),
                                    line * self.get_spacer())
            self.canvas.create_line(line*self.get_spacer(), 0,
                                    line * self.get_spacer(),
                                    self.get_window_size())

    def draw_marker(self, row, col, player) -> None:
        if self.game.is_empty_spot(row, col):
            self.reference.append(self.canvas.create_text(row*self.get_spacer()+self.get_offset(),
                                                          col* self.get_spacer()+self.get_offset(),
                                                          str(player.get_initial()),
                                                          font="TimesNewRoman {0} bold".format(player.get_initial())))

    def get_current_player(self) -> Player:
        return self.game.get_current_player()

    def get_offset(self) -> int:
        return int(self.get_spacer() / 2)

    def get_row_col_with_xy(self, x, y) -> tuple:
        spacer = self.get_spacer()
        offset = self.get_offset()
        x = int(x / spacer)
        y = int(y / spacer)
        return x, y

    def get_spacer(self) -> int:
        return int(self.get_window_size() / self.game.get_board_size())

    def get_window_size(self) -> int:
        return self.window_size

    def place_marker(self, event=None) -> None:
        if event:
            spacer = self.get_spacer()
            offset = self.get_offset()
            row, col = self.get_row_col_with_xy(event.x, event.y)
            if self.game.is_empty_spot(row,col):
                self.game.place_marker(self.get_current_player(), row, col)
                self.canvas.create_text(row * spacer + offset, col * spacer + offset,
                                        text=str(self.get_current_player().get_initial()),
                                        font="TimesNewRoman {0} bold".format(spacer))
                self.change_current_player()
                winner = self.game.get_winner()
                if winner:
                    if winner == "Cats Game":
                        title = "Tie"
                        message = "No winner, Cats Game"
                    else:
                        title = "Winner {0}".format(winner.get_initial())
                        message = "{0} has won".format(winner.get_initial())
                    tk.messagebox.showinfo(title, message)
                    self.clear_interface()
                    self.game.new_board()

    def set_menu(self) -> None:
        self.menu_bar = tk.Menu(self.root)
        self.player_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.player_menu.add_radiobutton(label="One Player", command=lambda:print("One"))
        self.player_menu.add_radiobutton(label="Two Players", command=lambda:print("Two"))
        self.menu_bar.add_cascade(label="Players", menu=self.player_menu)
        self.root.config(menu=self.menu_bar)

    def set_binds(self) -> None:
        self.root.bind("<Motion>", lambda event: self.display_current_player(event))
        self.root.bind("<Button-1>", lambda event: self.place_marker(event))


