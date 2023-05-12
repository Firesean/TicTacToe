import Player as player
class TicTacToe:

    def __init__(self, players=[player.Player("X"), player.Player("O")], board_size=3, in_a_row=3):
        self.board = []
        self.players = players
        self.in_a_row = in_a_row
        self.board_size = board_size
        # Main
        self.current_player = self.players[0]
        self.new_board()

    def is_empty_spot(self, row, col) -> bool:
        if self.board[row][col]:
            return False
        return True

    def get_board_size(self) -> int:
        return self.board_size

    def get_current_player(self) -> player:
        return self.current_player

    def get_positions(self, *args) -> list:
        items = []
        for item in args:
            items.append(self.board[item[0]][item[1]])
        return items

    def get_in_a_row(self) -> int:
        return self.in_a_row

    def get_winner(self) -> str:
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

    def new_board(self) -> list:
        self.current_player = self.players[0]
        self.board = []
        for row in range(self.get_board_size()):
            self.board.append([])
            for spot in range(self.get_board_size()):
                self.board[row].append(None)

    def place_marker(self, p, row, col) -> None:
        self.board[row][col] = p.get_initial()

    def print_board(self) -> None:
        for row in self.board:
            for i in range(len(row)):
                print(row[i], end="")
                if i < len(row)-1:
                    print("|", end="")
                else:
                    print("\n")

    def set_current_player(self, p) -> None:
        self.current_player = p
