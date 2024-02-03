from ChessPiece import ChessPiece

class Pawn(ChessPiece):    
    def move(self):
        print("Pawn moves forward.")
        if self.color == 'white':
            self.y += 1
        if self.color == 'black':
            self.y -= 1

class Rook(ChessPiece):
    def move(self):
        print("Rook moves horizontally or vertically.")

class Knight(ChessPiece):
    def move(self):
        print("Knight moves in an L-shape.")

class Bishop(ChessPiece):
    def move(self):
        print("Bishop moves diagonally.")

class Queen(ChessPiece):
    def move(self):
        print("Queen moves horizontally, vertically, or diagonally.")

class King(ChessPiece):
    def move(self):
        print("King moves one square in any direction.")