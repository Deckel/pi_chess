class Square:

    def __init__(self, x, y, piece) -> None:
        self.x = x
        self.y = y
        self.piece = piece
        promotion = self.promotion()

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(x={self.x}, y={self.self.y}, piece={self.piece})"

    def promotion(self):
        if (self.y == 7 and self.piece.color == 'white') or (self.y == 0 and self.piece.color == 'black'):
            return True
        else:
            return False

    

