class Square:

    def __init__(self, x, y, piece) -> None:
        self.x = x
        self.y = y
        self.position = self.readable_position()
        self.piece = piece

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.position}, piece={self.piece})"

    def readable_position(self):
        x_map = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'
        }
        return f"{x_map.get(self.x)}{self.y + 1}"


    

