class BoardMovements:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])

        if color == "WHITE":
            new_row = row - squares
        else:
            new_row = row + squares

        if new_row == 0 or new_row == 9:
            return position

        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        column = position[0]
        row = int(position[1])

        if color == "WHITE":
            new_row = row + squares
        else:
            new_row = row - squares

        if new_row == 0 or new_row == 9:
            return position

        return f"{column}{new_row}"

    @staticmethod
    def left(position: str, color: str, squares: int = 1):
        column = position[0]
        row = position[1]

        new_column = chr(ord(column) - squares)

        if new_column == "`" or new_column == "i":
            return position

        return f"{new_column}{row}"

    @staticmethod
    def right(position: str, color: str, squares: int = 1):
        column = position[0]
        row = position[1]

        new_column = chr(ord(column) + squares)

        if new_column == "`" or new_column == "i":
            return position

        return f"{new_column}{row}"