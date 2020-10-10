import numpy as np
import os
import time

#Code Olympics 2020 Team Tom Hanks - Stuart Mclaughlin, Alex Paterson, Sam Walker

def main():
    #define clear for later use in clearing the terminal
    clear = lambda: os.system('cls')

    #read input and generate initial board
    filename = input("Please enter the file name of your desired input: ")
    board = readInput(filename)
    
    iterations = input("How many generations do you want to see?\n")
    clear()

    startBoard = board
    #display each generation
    for i in range(0, int(iterations)):
        for a in board:
            print (' '.join(a))
        print("\n")

        newBoard = nextGen(board, 4, 8)
        board = newBoard

        print("Generation " + str(i+1))
        
        #show current gen for 0.1 seconds and clear terminal
        time.sleep(0.1)
        clear()

    #prints first and final generation board
    for a in startBoard:
            print (' '.join(a))
    print("\nFirst Generation\n")

    for a in board:
            print (' '.join(a))
    print("\nFinal Generation")

#function that reads input and returns board
def readInput(filename):
    f = open(filename, "r")
    boardDetails = f.read().split()

    #generate board of correct size
    board = np.full((int(boardDetails[0]),int(boardDetails[1])),".")

    numberOflines = int(boardDetails[0])

    #insert alive cells into board
    for indexLine in map(lambda x:x+2, range(numberOflines)):
        for char in enumerate(boardDetails[indexLine]):
            board[indexLine-2][char[0]] = char[1]
    
    return board
    

#function that generates board for the next generation
def nextGen(board, x, y):
    newBoard = np.copy(board)

    #iterate through each cell
    for i in range(0, x):
        for j in range(0, y):
            
            aliveNeighbours = 0

            #check all neighbours (diagonal, horizontal and vertical) to see if they are alive 
            for m in range(-1, 2):
                for n in range(-1,2):
                    if (i+m) >= x or (j+n) >= y:        #prevents index error
                        pass
                    elif board[i+m][j+n] == "*":
                        if (m != 0) or (n != 0):        #prevents cell counting itself as neighbour
                            aliveNeighbours += 1
            

            
            #rules
            if (board[i][j] == "*"):        #if cell is alive
                if (aliveNeighbours < 2 or aliveNeighbours > 3):
                    newBoard[i][j] = "."

            else:                           #else cell is dead
                if (aliveNeighbours == 3):
                    newBoard[i][j] = "*"
                

    return newBoard

main()