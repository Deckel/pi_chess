from Square import Square
from Pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self):
        self.squares = [[Square(x, y, None) for x in range(8)] for y in range(8)]
        self.game_state = self.calculate_game_state()
        self.player_turn = 'white'

    def print_chess_row(self):
        board_str = ""
        # for reversed list of squares crate rows to print
        for i, row in enumerate(self.squares[::-1]):
            row_str = ""
            # for squares in row create the strings
            for square in row:
                if square.piece is not None:
                    row_str += f"|{square.piece} "
                else:
                    row_str += "|         "
            # create the lines since we cannot nest f strings to append |
            horizontal_line = f"-"*81
            # append row string
            board_str += f"{row_str}|\n"
            # append horizontal line
            board_str += f"{horizontal_line}\n"
        return board_str
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{self.print_chess_row()} \n"

    def initialize_pieces(self):
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        # initialize major and mnior pieces
        for y, color in ((0, 'white'), (1, 'white'), (6, 'black'), (7, 'black')):
            for x, piece_class in enumerate(piece_order):
                self.squares[y][x].piece = piece_class(color=color)

        # initialize pawns
        for y, color in ((1, 'white'), (6, 'black')):
            for x in range(8):
                self.squares[y][x].piece = Pawn(color=color)

    def calculate_game_state(self):
        # will return False or something to indicate the game has ended
        pass

   
if __name__ == '__main__':

    board = Board()
    board.initialize_pieces()

    print(board)
