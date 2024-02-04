from ChessPiece import ChessPiece

class Pawn(ChessPiece):
    def available_moves(self, board):
        available_moves = []

        # define direction
        if self.color == 'white':
            direction = +1
        else:
            direction =-1
        
        # define double move
        if self.y == 1 and self.color == 'white':
            available_moves.append((self.x, self.y + 2*direction))
        if self.y == 6 and self.color == 'black':
            available_moves.append((self.x, self.y + 2*direction))
    
        # define single move
        #TODO: technically this logic could live in the ChessPiece class as a legal move
        # but it kind of is attribute of only the pawn
        if not board.squares[self.y+1*direction][self.x].piece:
            available_moves.append((self.x, self.y + 1*direction))
        
        # define diagnoal capture
        #TODO: technically this logic could live in the ChessPiece class as a legal move
        # but it kind of is attribute of only the pawn
        if board.squares[self.y+1*direction][self.x+1].piece:
            available_moves.append((self.x+1, self.y+1*direction)) # caprure to the right

        if board.squares[self.y+1*direction][self.x-1].piece:
            available_moves.append((self.x-1, self.y+1*direction)) # caprure to the left
        
        return available_moves

class Rook(ChessPiece):
    def available_moves(self):
        moves = []

        moves += self.x

        return moves


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