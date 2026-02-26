from abc import ABC, abstractmethod


class BaseChessPiece(ABC):
    def __init__(self, color, name, symbol, identifier):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = "None"
        self.is_alive = True

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

    @abstractmethod
    def move(self):
        pass

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"


class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        print("Pawn moves forward 1 position")