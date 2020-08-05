from copy import deepcopy
import sudoku

#The solver class for solving our sudoku board
#This uses the backtracking algorithm
class Solver:
    #Initialize the solver
    def __init__(self, board):
        self.board = board
    
    #Solves the board using backtracking
    #Returns True if board found
    #Returns False otherwise
    def solve(self):
        firstrow, firstcol = self.board.getFirstOpen()
        if firstrow == -1:
            return True
        curboard = deepcopy(self.board._board)
        possible = self.board.possible(firstrow, firstcol)
        if len(possible) == 0:
            return False
        for i in possible:
            curboard[firstrow][firstcol] = i
            self.board.fill(curboard)
            if self.solve():
                return True
        return False

