
from Square import Square
# from ChessPiece import ChessPiece
from Pieces import Rook, Knight, Bishop, Queen, King, Pawn


def create_squares():
    board = []
    for x in range(0,8):
        for y in range(0,8):
            board.append(Square(x, y, piece=None))
    return board

def game_start(board):
    for square in board:
        if square.y == 0:
            if square.x == 0 or square.x== 7 :
                square.piece = Rook(color='white')
            if square.x == 1 or square.x== 6 :
                square.piece = Knight(color='white')
            if square.x == 2 or square.x== 5 :
                square.piece = Bishop(color='white')
            if square.x == 3:
                square.piece = Queen(color='white')
            if square.x == 4:
                square.piece = King(color='white')
        if square.y == 1:
            square.piece = Pawn(color='white')
        if square.y == 7:
            if square.x == 0 or square.x== 7 :
                square.piece = Rook(color='black')
            if square.x == 1 or square.x== 6 :
                square.piece = Knight(color='black')
            if square.x == 2 or square.x== 5 :
                square.piece = Bishop(color='black')
            if square.x == 3:
                square.piece = Queen(color='black')
            if square.x == 4:
                square.piece = King(color='black')
        if square.y == 6:
            square.piece = Pawn(color='black')
        


if __name__ == '__main__':
    board = create_squares()

    game_start(board)

    for square in board:
        print(square)