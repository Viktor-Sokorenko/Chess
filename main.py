from board import Board

board = Board()

bishop = board.get_piece("c1")
bishop.move("ForwardRight", 2)

queen = board.get_piece("d1")
queen.move("Forward", 2)

king = board.get_piece("e1")
king.move("Forward")