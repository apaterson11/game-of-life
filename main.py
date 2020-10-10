import numpy as np

def main():
    
    board = readInput(filename = r"C:\Users\apate\Workspace\game-of-life\input.txt")
    nextGen(board, 4, 8)

def readInput(filename):
    f = open(filename, "r")
    boardDetails = f.read().split()
    board = np.full((int(boardDetails[0]),int(boardDetails[1])),".")

    numberOflines = int(boardDetails[0])

    for indexLine in map(lambda x:x+2, range(numberOflines)):
        for char in enumerate(boardDetails[indexLine]):
            board[indexLine-2][char[0]] = char[1]
    
    print(board)
    
    return board
    

def nextGen(board, x, y):
    #iterate through each cell
    for i in range(0, x):
        for j in range(0, y):
            
            aliveNeighbours = 0
            for m in range(-1, 2):
                for n in range(-1,2):
                    if (i+m) >= x or (j+n) >= y:
                        pass
                    elif board[i+m][j+n] == "*":
                        if (m != 0) or (n != 0):
                            aliveNeighbours += 1
            


            print(board[i][j], aliveNeighbours)

main()