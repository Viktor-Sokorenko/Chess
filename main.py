from movements import BoardMovements

print(BoardMovements.forward("a2", "BLACK", 1))
print(BoardMovements.forward("a2", "WHITE", 1))

print(BoardMovements.backward("a2", "BLACK", 1))
print(BoardMovements.backward("a2", "WHITE", 1))

print(BoardMovements.left("b2", "BLACK", 1))
print(BoardMovements.right("b2", "BLACK", 1))

print(BoardMovements.left("a2", "BLACK", 1))
print(BoardMovements.right("h2", "BLACK", 1))