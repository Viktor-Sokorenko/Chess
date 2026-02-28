from board import Board

board = Board()

pawn = board.get_piece("a2")
pawn.move()

pawn = board.get_piece("b2")
pawn.move()