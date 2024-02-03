class Square:
    def __init__(self, x, y, piece) -> None:
        self.x = x
        self.y = y
        self.piece = piece
        self.position = self.readable_position()

    def __repr__(self):
        class_name = type(self).__name__
        return f"({self.position}, {self.piece})"

    def readable_position(self):
        x_map = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'
        }
        return f"{x_map.get(self.x)}{self.y + 1}"
