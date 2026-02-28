from abc import ABC, abstractmethod
from movements import BoardMovements


class BaseChessPiece(ABC):
    def __init__(self, color, name, symbol, identifier):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = "None"
        self.is_alive = True
        self.board = None

    # ********** property color - (setter/getter) ***********
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value) -> None:
        if value in ["BLACK", "WHITE"]:
            self.__color = value
        else:
            raise ValueError("Color must be 'BLACK' or 'WHITE'")

    # ********** property name - (setter/getter) ***********
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if isinstance(value, str) and value.strip() != "":
            self.__name = value
        else:
            raise ValueError("Name have to be a non empty string")

    # ********** property symbol - (setter/getter) ***********
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value) -> None:
        if isinstance(value, str) and len(value) == 1:
            self.__symbol = value
        else:
            raise ValueError("Symbol have to be a single character")

    # ********** property identifier - (setter/getter) ***********
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, value) -> None:
        if isinstance(value, int) and value > 0:
            self.__identifier = value
        else:
            raise ValueError("Identifier have to be an int greater than 0")

    # ********** property position - (setter/getter) ***********
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value) -> None:
        if isinstance(value, str):
            self.__position = value
        else:
            raise ValueError("Position have to be a string")

    # ********** property is_alive - (setter/getter) ***********
    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value) -> None:
        if isinstance(value, bool):
            self.__is_alive = value
        else:
            raise ValueError("is_alive have to be a bool")
        
    # ********** property board - (setter/getter) ***********
    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, value) -> None:
        self.__board = value

    @abstractmethod
    def move(self, movement):
        print(movement)

    def die(self):
        self.is_alive = False
    
    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"


class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        movement = BoardMovements.forward(self.position, self.color, 1)
        super().move(movement)

class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Rook", "R", identifier)

    def move(self, direction, squares):
        if direction == "Left":
            movement = BoardMovements.left(self.position, self.color, squares)

        elif direction == "Right":
            movement = BoardMovements.right(self.position, self.color, squares)

        elif direction == "Forward":
            movement = BoardMovements.forward(self.position, self.color, squares)

        elif direction == "Backward":
            movement = BoardMovements.backward(self.position, self.color, squares)

        else:
            return

        super().move(movement)


class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self, direction, squares):
        if direction == "ForwardLeft":
            movement = BoardMovements.forward_left(self.position, self.color, squares)

        elif direction == "ForwardRight":
            movement = BoardMovements.forward_right(self.position, self.color, squares)

        elif direction == "BackwardLeft":
            movement = BoardMovements.backward_left(self.position, self.color, squares)

        elif direction == "BackwardRight":
            movement = BoardMovements.backward_right(self.position, self.color, squares)

        else:
            return

        super().move(movement)

class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self, direction, squares):
        if direction == "Left":
            movement = BoardMovements.left(self.position, self.color, squares)

        elif direction == "Right":
            movement = BoardMovements.right(self.position, self.color, squares)

        elif direction == "Forward":
            movement = BoardMovements.forward(self.position, self.color, squares)

        elif direction == "Backward":
            movement = BoardMovements.backward(self.position, self.color, squares)

        elif direction == "ForwardLeft":
            movement = BoardMovements.forward_left(self.position, self.color, squares)

        elif direction == "ForwardRight":
            movement = BoardMovements.forward_right(self.position, self.color, squares)

        elif direction == "BackwardLeft":
            movement = BoardMovements.backward_left(self.position, self.color, squares)

        elif direction == "BackwardRight":
            movement = BoardMovements.backward_right(self.position, self.color, squares)

        else:
            return

        super().move(movement)

class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "King", "K", identifier)

    def move(self, direction):
        if direction == "Left":
            movement = BoardMovements.left(self.position, self.color, 1)

        elif direction == "Right":
            movement = BoardMovements.right(self.position, self.color, 1)

        elif direction == "Forward":
            movement = BoardMovements.forward(self.position, self.color, 1)

        elif direction == "Backward":
            movement = BoardMovements.backward(self.position, self.color, 1)

        elif direction == "ForwardLeft":
            movement = BoardMovements.forward_left(self.position, self.color, 1)

        elif direction == "ForwardRight":
            movement = BoardMovements.forward_right(self.position, self.color, 1)

        elif direction == "BackwardLeft":
            movement = BoardMovements.backward_left(self.position, self.color, 1)

        elif direction == "BackwardRight":
            movement = BoardMovements.backward_right(self.position, self.color, 1)

        else:
            return

        super().move(movement)


class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Knight", "N", identifier)

    def move(self):
        movement = "Knight moves in an L shape"
        super().move(movement)