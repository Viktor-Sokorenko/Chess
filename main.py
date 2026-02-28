from board import Board

board = Board()
board.print_board()

pawn = board.get_piece("a2")
pawn.move()

board.print_board()