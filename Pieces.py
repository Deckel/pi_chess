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
    def available_moves(self, board):
        available_moves = []
        # define rook moves
        for i in range(len(board.squares)+1):
            available_moves.append((self.x, i)) # all squares on column
            available_moves.append((i, self.y)) # all squares on row

        return available_moves

class Knight(ChessPiece):
    def available_moves(self, board):
        # just hardcode all the jumps
        available_moves = [
            (self.x + 2, self.y + 1), (self.x + 2, self.y - 1),
            (self.x - 2, self.y + 1), (self.x - 2, self.y - 1),
            (self.x + 1, self.y + 2), (self.x + 1, self.y - 2),
            (self.x - 1, self.y + 2), (self.x - 1, self.y - 2)
        ]

        return available_moves

class Bishop(ChessPiece):
    def available_moves(self, board):
        available_moves = []
        # Define directions for diagonal movement
        directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

        for dx, dy in directions:
            new_x, new_y = self.x, self.y
            for _ in range(7):  # Maximum 7 squares along the diagonal
                new_x, new_y = new_x + dx, new_y + dy
                available_moves.append((new_x, new_y))
        
        return available_moves

class Queen(ChessPiece):
    def available_moves(self, board):
        available_moves = []

        # Define directions for diagonal movement
        directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

        for dx, dy in directions:
            new_x, new_y = self.x, self.y
            for _ in range(7):  # Maximum 7 squares along the diagonal
                new_x, new_y = new_x + dx, new_y + dy
                available_moves.append((new_x, new_y))

        # define horizontal directions
        for i in range(len(board.squares)+1):
            available_moves.append((self.x, i)) # all squares on column
            available_moves.append((i, self.y)) # all squares on row

        return available_moves

class King(ChessPiece):
    def available_moves(self):
        # Hard code basic king moves
        available_moves = [
            (-1, 0), 
            (-1, 1),
            (-1, -1),
            (0, -1), 
            (1, -1), 
            (1, 0),
            (1, 1)
            (0, 1),
        ]
        return available_moves