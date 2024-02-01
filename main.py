from Square import Square
from Pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self):
        self.squares = [[Square(x, y, None) for x in range(8)] for y in range(8)]

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

   
if __name__ == '__main__':

    board = Board()
    board.initialize_pieces()

    for row in board.squares:
        for col in row:
            print(col)