from abc import ABC, abstractmethod
from Square import Square

class ChessPiece(Square):
    def __init__(self, color) -> None:
        self.color = color,
        self.legal_moves = self.calculate_legal_moves()

    def __repr__(self):
        class_name = type(self).__name__

        # max string length is 8 letters,
        # so we standardise this by adding spaces 
        pretty_str = f"{class_name} {self.color[0][0]}"
        while len(pretty_str) != 8:
            pretty_str += ' '
        return pretty_str

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

    

    

