import os
import re
import traceback

from Square import Square
from Pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self):
        self.squares = [[Square(x, y, None) for x in range(8)] for y in range(8)]
        self.game_end = self.game_end()
        self.player = 'white',
        self.turn = 0
        self.pgn = ""

    #TODO: use this function to make self.squares, and then change all refernces to
    #      the array from array[y][x] to array[x][y] (big refactor hehe)
    def generate_squares(self):
        squares = [[Square(x, y, None) for x in range(8)] for y in range(8)]
        transpose_squares = [list(row) for row in zip(*squares)]
        reversed_transpose_squares = transpose_squares[::-1]
        return reversed_transpose_squares

    def print_board(self):
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
        #TODO: this prints out like 4 boards and I have no idea why
        class_name = type(self).__name__
        return f"{self.print_board()} \n"

    def initialize_pieces(self):
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        # initialize major and mnior pieces
        for y, color in ((0, 'white'), (1, 'white'), (6, 'black'), (7, 'black')):
            for x, piece_class in enumerate(piece_order):
                self.squares[y][x].piece = piece_class(color=color, x=x, y=y)

        # initialize pawns
        for y, color in ((1, 'white'), (6, 'black')):
            for x in range(8):
                self.squares[y][x].piece = Pawn(color=color, x=x, y=y)

    def update_pieces(self):
        # search over board and update game state
        for row in self.squares:
            for square in row:
                if square.piece is not None:
                    if (square.x, square.y) != (square.piece.x, square.piece.y):
                        # add piece to new square
                        self.squares[square.piece.y][square.piece.x].piece = square.piece
                        # remove piece from old square
                        self.squares[square.y][square.x].piece = None
                        
    

    def game_end(self):
        # will return False or something to indicate the game has ended
        return False
   
if __name__ == '__main__':

    def pgn_to_index(pgn_str, board):
        # Examples Kc4 Bxb2 c4 d7 fxg7 Bxc3+
        valid_pieces = {'K':King, 'Q':Queen, 'R':Rook, 'B':Bishop, 'N':Knight}
        pgn_x_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
                
        target_square_str = re.search(r'([a-h][1-8])', pgn_str).group(1)
        target_square = (pgn_x_map[target_square_str[0]], int(target_square_str[1])-1)
        
        # get piece and make a dummy piece to compare, defualt is a pawn
        origin_piece = Pawn(color=board.player, x=-1, y=-1)
        for piece in valid_pieces.keys():
            if piece in pgn_str:
                origin_piece = valid_pieces[piece](color=board.player, x=-1, y=-1)

        # find origin square by checking all pieces of class piece that could
        # move to target square.
        origin_square = []

        for row in board.squares:
            for square in row:
                if square.piece is not None:
                    if square.piece.__class__ == origin_piece.__class__ and square.piece.color == origin_piece.color:
                        if target_square in square.piece.legal_moves(board):
                            origin_square.append((square.piece.x, square.piece.y))
                            
        #TODO: just choose first valid piece, but handle an exception if there are two in the future
        origin_square = origin_square[0]

        return target_square, origin_square

    board = Board()
    board.initialize_pieces()

    while board.game_end == False:

        # set player
        if board.turn %2 == 0:
            board.player = 'white'
        else:
            board.player = 'black'

        # print the board
        # os.system('clear')
        print(board)

        # fetch user input
        while True:
            try:
                pgn_str = input("Enter a move:")
                target_square, origin_square = pgn_to_index(pgn_str, board)

                #TODO: Check move does not create a check

            except Exception as error:
                os.system('clear')
                print(board)
                print(f"{pgn_str} is not a valid move")
                print(traceback.format_exc()) # temp traceback print for debugging
            else:
                break

        # move, update board, and increment turn
        board.squares[origin_square[1]][origin_square[0]].piece.move(target_square)
        board.update_pieces()
        board.turn += 1

        # append pgn
        board.pgn.join(f'{pgn_str}, ')

        print(board.pgn)

        