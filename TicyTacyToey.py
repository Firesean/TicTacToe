import Player as player
class TicTacToe:

    in_a_row = 3

    def __init__(self, players=[player.Player("X"), player.Player("O")]):
        self.board = []
        self.players = players

        # Main
        self.current_player = self.players[0]
        self.new_board()

    def is_empty_spot(self, row, col):
        if self.board[row][col]:
            return False
        return True

    def get_current_player(self):
        return self.current_player

    def get_positions(self, *args):
        items = []
        for item in args:
            items.append(self.board[item[0]][item[1]])
        return items

    def get_in_a_row(self):
        return self.in_a_row

    def get_winner(self):
        for p in self.players: # p = Player
            for row in self.board:
                if row.count(p.get_initial()) == self.in_a_row:
                    return p
            for col in range(self.in_a_row):
                if self.get_positions((0, col), (1, col),(2, col)).count(p.get_initial()) == self.in_a_row:
                    return p
            if self.get_positions((0,0),(1,1),(2,2)).count(p.get_initial()) == self.in_a_row:
                return p
            if self.get_positions((0,2),(1,1),(2,0)).count(p.get_initial()) == self.in_a_row:
                return p
        count = 0
        for row in self.board:
            count += row.count(None)
        if count:
            return None
        return "Cats Game"

    def new_board(self):
        self.current_player = self.players[0]
        self.board = []
        for row in range(self.in_a_row):
            self.board.append([])
            for spot in range(self.in_a_row):
                self.board[row].append(None)

    def place_marker(self, p, row, col):
        self.board[row][col] = p.get_initial()

    def print_board(self):
        for row in self.board:
            for i in range(len(row)):
                print(row[i], end="")
                if i < len(row)-1:
                    print("|", end="")
                else:
                    print("\n")

    def set_current_player(self, p):
        self.current_player = p
