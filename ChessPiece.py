from abc import ABC, abstractmethod

class ChessPiece:
    def __init__(self, x, y, color, type) -> None:
        self.x = x
        self.y = y
        self.piece = type,
        self.color = color,
        self.legal_moves = self.calculate_legal_moves()

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(pos_x={self.x}, po_y={self.self.y}, piece={self.type})"

    def calculate_legal_moves(self):
        return None

    @abstractmethod
    def move():
        pass

    @abstractmethod
    @staticmethod
    def taken():
        pass

    def promote(self):
        print("Choose piece to promote too@")
        return None

    

    

