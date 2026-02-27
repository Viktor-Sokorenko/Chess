from movements import BoardMovements

print(BoardMovements.forward_left("d4", "BLACK", 1))
print(BoardMovements.forward_right("d4", "BLACK", 1))
print(BoardMovements.backward_left("d4", "BLACK", 1))
print(BoardMovements.backward_right("d4", "BLACK", 1))

print(BoardMovements.forward_left("a8", "BLACK", 1))
print(BoardMovements.backward_right("h1", "BLACK", 1))