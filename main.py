import os
import re

from Square import Square
from Pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self):
        self.squares = [[Square(x, y, None) for x in range(8)] for y in range(8)]
        self.game_end = self.game_end()
        self.player_turn = 'white'
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


    def extract_target_square(move):
        # Regular expression to match the target square
        match = re.search(r'([a-hA-H][1-8])', move)
        if match:
            # Return the matched target square
            return match.group(1)
        else:
            # TODO: Handle the case when no target square is found
            return None
    
    
    def pgn_str_to_move(pgn_str):
        # examples: a4, Kc6, O-O, Bxc6
        pgn_x_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        # find square to move too
        target_square = (pgn_x_map[extract_target_square(pgn_str)[0]], int(extract_target_square(pgn_str)[1])-1)
        return target_square

    def target_in_legal_moves(target, legal_moves):
        if target not in legal_moves:
            raise ValueError('Target is not in legal move list')

    board = Board()
    board.initialize_pieces()

    while board.game_end == False:
        
        os.system('clear')
        print(board)

        # fetch user input
        while True:
            try:
                from_square = pgn_str_to_move(input("Enter a from:"))
                target_square = pgn_str_to_move(input("Enter a target:"))

                legal_moves = board.squares[from_square[1]][from_square[0]].piece.legal_moves(board)
                target_in_legal_moves(target_square, legal_moves)
            except ValueError:
                print("Sorry, but that's not a fucking legal move")
                continue
            except AttributeError:
                print("Sorry but there is no fucking piece you selected to move")
            else:
                break

        board.squares[from_square[1]][from_square[0]].piece.move(target_square)

        board.update_pieces()
        

            

    


    





        


