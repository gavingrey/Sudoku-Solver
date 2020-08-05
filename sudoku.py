class Board:
    #Our Sudoku board is implemented as a 9x9 list
    #Each row of the list is a row of the board, starting from the top
    #We represent empty spaces with a 0

    #We initialize a Sudoku board as empty, with an optional parameter to fill
    def __init__(self, rows=None):
        empty_board = [[0 for i in range(9)] for i in range(9)]

    #Fills the board with a given 9x9 list
    def fill(self, rows):
        
    #Inserts a number onto the grid
    def insert(num, x, y):
        
    #Empties the board
    def empty(self):

#Checks if a given set of rows is a valid Sudoku board
def check(rows):