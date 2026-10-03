def loadBoard(filename):
    # loads the baord from the file. It is returned as a list of lists
    board = []
    file = open(filename, "r")
    for line in file:
        row = line.strip().split()
        if row:
            board.append(row)
    file.close()
    return board

def printBoard(board):
    # prints the board to the console
    for row in board:
        print(" ".join(row))
        

def possibleMoves(position, board):
    # calculates and returns the positions from a given position 
    x, y = position
    moves = []
    n = len(board)

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            newx, newy = x + dx, y + dy
            if 0 <= newx < n and 0 <= newy < n:
                moves.append((newx, newy))
    return moves

myBoard = loadBoard("board.txt")
printBoard(myBoard)
possibleMoves((0,0),myBoard)
possibleMoves((2,2),myBoard)





