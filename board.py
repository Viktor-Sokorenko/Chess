from pieces import Rook, Knight, Bishop, Queen, King, Pawn


class Board:
    def __init__(self):
        self.squares = {}

        for col in range(ord("a"), ord("i")):
            for row in range(1, 9):
                square = f"{chr(col)}{row}"
                self.squares[square] = None

        self.setup_board()

        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        for row in range(1, 9):
            line = []
            for col in range(ord("a"), ord("i")):
                square = f"{chr(col)}{row}"
                line.append(self.squares[square])
            print(line)
    
    def get_piece(self, square):
        """Returns the piece that is on a specific square"""
        return self.squares[square]

    def is_square_empty(self, square):
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def find_piece(self, symbol: str, identifier: int, color: str):
        result = []

        for square, piece in self.squares.items():
            if piece is not None:
                if piece.symbol == symbol and piece.identifier == identifier and piece.color == color:
                    result.append((square, piece))

        return result

    def kill_piece(self, square):
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None
    
    def setup_board(self):
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

        identifier = 1
        for col in range(ord("a"), ord("i")):
            square = f"{chr(col)}2"
            self.squares[square] = Pawn("BLACK", identifier)
            identifier += 1

        identifier = 1
        for col in range(ord("a"), ord("i")):
            square = f"{chr(col)}7"
            self.squares[square] = Pawn("WHITE", identifier)
            identifier += 1