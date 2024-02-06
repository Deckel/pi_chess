class ChessPiece():
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y= y
        
    def __repr__(self):
        class_name = type(self).__name__
        # max string length is 8 letters,
        # so we standardise this by adding spaces 
        pretty_str = f"{class_name} {self.color[0][0]}"
        while len(pretty_str) != 8:
            pretty_str += ' '
        return f"{pretty_str}"

    def legal_moves(self, board):
        avilable_moves = self.__class__.available_moves(self, board)
        # piece cannot move to it's own square
        avilable_moves = [move for move in avilable_moves if move != (self.x, self.y)]
        # restrict avilable_moves to inside the playing board
        avilable_moves = [move for move in avilable_moves if 0 <= move[0] <= 7 and 0 <= move[1] <= 7]
        
        # make sure it does not pass through any other pieces


        # ensure it does not put the king in check
        
        
        return avilable_moves

    def taken(self):
        pass

    def move(self, target_square):
        self.x = target_square[0]
        self.y = target_square[1]
        


