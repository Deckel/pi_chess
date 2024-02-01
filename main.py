
from Square import Square


def create_squares():
    squares = []
    for x in range(0,8):
        for y in range(0,8):
            squares.append(Square(x, y, piece=''))
    return squares


if __name__ == '__main__':
    squares = create_squares()