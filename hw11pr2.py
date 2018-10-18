#amamdna owens



def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it
    
    def addMove(self, col, ox):
        """adds X or O into board from bottom"""
        for i in range(self.height):
            if self.data[i][col] != " ":
               self.data[i-1][col]=ox
               return 
        self.data[self.height-1][col]=ox 

    def clear(self):
        """clears board of all pieces"""
        self.data =[[' ']*self.width for row in range(self.height)]

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'   


    def allowsMove(self, c):
        """"checks if a piece can fit in a row c, returns false if row doesnt exist on board 
        or is full"""
        if c<0 or c>=self.width:
            return False
        if self.data[0][c]!=" ":
            return False
        return True


    def isFull(self):
        for x in range(self.width):
            if self.allowsMove(x)==True:
                return False
        return True

    def delMove(self,c):
        """deletes top checker from column c"""
        for i in range(self.height):
            if self.data[i][c] != ' ':
                self.data[i][c] = ' '
                break
            
    def winsFor(self, ox):
        for i in range(self.height):
            for j in range(self.width):
                if inarow_Neast(ox,i,j,self.data,4) or inarow_Nnortheast(ox,i,j,self.data,4) or inarow_Nsouth(ox,i,j,self.data,4) or inarow_Nsoutheast(ox,i,j,self.data,4):
                    return True

        return False

    def hostGame(self):
        print(self)
        while 1==1:
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = int(input("X turn: "))
            
            
            
            self.addMove(users_col, "X")
            print(self)

            if self.winsFor("X"):
                print("Player X Wins!")
                return
            if self.isFull():
                print("tie")
                return

            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = int(input("O turn: "))
            self.addMove(users_col,"O")

            print(self)
            if self.winsFor("O"):
                print("Player O Wins!")
                return

            if self.isFull():
                print("tie :/")
                return





