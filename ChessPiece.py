class ChessPiece():
    def __init__(self, color, x, y) -> None:
        self.color = color
        self.x = x
        self.y= y
        self.legal_moves = self.calculate_legal_moves()

    def __repr__(self):
        class_name = type(self).__name__
        # max string length is 8 letters,
        # so we standardise this by adding spaces 
        pretty_str = f"{class_name} {self.color[0][0]}"
        while len(pretty_str) != 8:
            pretty_str += ' '
        return f"{pretty_str}"

    def calculate_legal_moves(self):
        pass

    def taken(self):
        pass


