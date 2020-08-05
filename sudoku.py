#Checks if a given set of rows is a valid Sudoku board
def check(rows):
    #Only return true if no exceptions and it passes all tests
    try:
        if len(rows) != 9:
            return False
        for row in rows:
            if len(row) != 9:
                return False
            for col in row:
                if not isinstance(col, int):
                    return False
                if col < 0 or col > 9:
                    return False
    except:
        return False
    else:
        return True

class Board:
    #Our Sudoku board is implemented as a 9x9 list
    #Each row of the list is a row of the board, starting from the top
    #We represent empty spaces with a 0

    #We initialize a Sudoku board as empty, with an optional parameter to fill
    def __init__(self, rows=None):
        #Attempt to fill with given rows, else fill with empty
        if(not self.fill(rows)):
            self.empty()

    #Attempts to fill the board with a given 9x9 list
    #Returns True if success, False if fail
    def fill(self, rows):
        if(check(rows)):
            self._board = rows
            return True
        else:
            return False

    #Empties the board
    def empty(self):
        self.fill([[0 for _ in range(9)] for _ in range(9)])

    #Attempts to insert a number onto the grid
    #Returns True if success, False if fail
    def insert(self, num, row, col):
        if isinstance(num, int):
            if num >= 0 and num <= 9:
                self._board[row, col] = num
                return True
        return False

    #Attempts to return a given row
    #Returns False if fail
    def getrow(self, row):
        try:
            return self._board[row]
        except:
            return False

    #Attempts to return a given column
    #Returns False if fail
    def getcol(self, col):
        try:
            return [row[col] for row in self._board]
        except:
            return False

    #Attempts to return a given square
    #Returns square in the form of a single list of ints
    #Returns False if fail
    def getsquare(self, row, col):
        square = []
        try:
            rowSection = row // 3
            colSection = col // 3
            firstRow = 3 * rowSection
            firstCol = 3 * colSection
            for row in self._board[firstRow:firstRow + 3]:
                square.extend(row[firstCol:firstCol + 3])
            return square
        except:
            return False

    #Attempts to return a list of possible integers for a space
    #Returns False if fail
    def possible(self, row, col):
        intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        currow = self.getrow(row)
        curcol = self.getcol(col)
        cursquare = self.getsquare(row, col)
        if currow and currow and cursquare:
            return [i for i in intlist if i not in currow + curcol + cursquare ]
        else:
            return False