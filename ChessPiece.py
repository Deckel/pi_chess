from abc import ABC, abstractmethod
from Square import Square

class ChessPiece(Square):
    def __init__(self, color) -> None:
        # self.x = x
        # self.y = y
        self.color = color,
        self.legal_moves = self.calculate_legal_moves()

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(color={self.color})"

    def calculate_legal_moves(self):
        pass

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def taken():
        pass

    def promote(self):
        print("Choose piece to promote too@")
        pass

    

    

