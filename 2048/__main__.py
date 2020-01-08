from game import Game
from board import Board

game = Game()
game.start()

# board = Board(4, 4)

# testRows = []

# testRows.append([0, 2, 2, 0])
# testRows.append([0, 2, 0, 0])
# testRows.append([0, 4, 2, 2])
# testRows.append([4, 4, 0, 0])
# testRows.append([8, 2, 2, 0])

# for row in testRows:
#     print("Initial State: " + str(row))
#     board.slideRaw(row)
#     print("Final State: " + str(row) + "\n")

# available = game.board.availableTiles()
# for p in available:
#     print(str(p))

# from grid import Grid

# grid = Grid(4, 4)

# row = [0, 0, 0, 0]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")

# row = [0, 1, 0, 0]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")

# row = [1, 0, 1, 0]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")

# row = [1, 0, 1, 1]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")

# row = [2, 0, 1, 1]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")

# row = [2, 1, 0, 1]
# print(str(row))
# grid.slideRow(row)
# print(str(row) + "\n")