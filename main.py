from board import Board

board = Board()
board.print_board()

print(board.find_piece("R", 1, "BLACK"))
print(board.is_square_empty("a3"))
board.kill_piece("a1")
board.print_board()