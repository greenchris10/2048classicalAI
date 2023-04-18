#Steps:
#1. Set up board class
#2. Create functions that will merge left, right, up, or down
#3. Implement MiniMax
#4. Use pygame to add graphics (didn't have enough time to do this)

import random
import numpy as np
import copy

class Board:
    
    def __init__(self, board_size = 4):
        self.board_size = board_size
        self.board = [[0]*board_size for num in range(board_size)]
        self.score = 0

        self.addTile()
        self.addTile()

    def __str__(self):
        outStr = ''
        for i in self.board:
            outStr += '\t'.join(map(str,i))
            outStr += '\n'
        return outStr

    # function that checks board for available tiles
    def available_tiles(self):

        available = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == 0:
                    available.append((row,col))
        
        return available
    
    # function to add tile to board (either 2 or 4)
    def addTile(self):
            num_to_add = 0
            free_spaces = self.available_tiles()
            if len(free_spaces) == 0:
                 raise Exception("board is currently full")
            
            position = free_spaces[0]
            
            num_to_add = 4

            self.board[position[0]][position[1]] = num_to_add

    #function to move 
    def move_row_left(self, row):
        
        #move all numbers to the left of row
        for i in range(self.board_size - 1):
             for j in range(self.board_size - 1, 0, -1 ):
                  if row[j-1] == 0:
                    row[j-1] = row[j]
                    row[j] = 0

        #merge numbers in row that are the same
        for i in range(self.board_size - 1):
             if row[i] == row[i+1]:
                  row[i] *= 2
                  self.score += row[i]
                  row[i+1] = 0

        # move numbers to the left again
        for i in range(self.board_size - 1, 0, -1):
             if row[i-1] == 0:
                  row[i-1] = row[i]
                  row[i] = 0

        return row
    
    # applies the  'move_row_left' funtion on the entire board
    def merge_left(self):
        
        for row in range(self.board_size):
             self.board[row] = self.move_row_left(self.board[row])
    
    #reverses the order of one row
    def reverse(self, row):
         #return row in reverse order
         return row[::-1]
    
    #merges the whole board right
    def merge_right(self):
         #reverse row, move row left, reverse back
         for row in range(self.board_size):
              self.board[row] = self.reverse(self.board[row])
              self.board[row] = self.move_row_left(self.board[row])
              self.board[row] = self.reverse(self.board[row])
    
    #transposes the board
    def transpose(self):
         self.board = np.array(self.board).T.tolist()
            
    #merges the board up
    def merge_up(self):
         self.transpose()
         self.merge_left()
         self.transpose()

    #merges the board down
    def merge_down(self):
         self.transpose()
         self.merge_right()
         self.transpose()
    
    def getHeuristic(self, A = 1000, B = 50, C = 30):

        inCorner = False

        E = len(self.available_tiles())
        D = []

        corner_locations = [(0,0), (0,self.board_size-1),
                            (self.board_size-1, 0), (self.board_size-1, self.board_size-1)]
        max_num = 0
        max_location = (0,0)

        for i in range(self.board_size):
            for j in range(self.board_size):
                D.append(self.board[i][j])
                if self.board[i][j] > max_num:
                    max_num = self.board[i][j]
                    max_location = (i,j)

        D = len(np.unique(np.array(D)).tolist())-1

        for i in corner_locations:
            if i == max_location:
                inCorner = True

        if inCorner:
            P = 0
        else:
            P = 1
    
        h_n = A*E - B*D - C*P

        return h_n


    #returns true if board can move up
    def canMoveUp(self):
        for j in range(self.board_size):
            k = -1
            for i in range(self.board_size-1, -1, -1):
                if self.board[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, 0, -1):
                    if self.board[i-1][j] == 0 or self.board[i][j] == self.board[i-1][j]:
                        return True
        return False
    
    #returns true if board can move down
    def canMoveDown(self):
        for j in range(self.board_size):
            k = -1
            for i in range(self.board_size):
                 if self.board[i][j] > 0:
                    k = i
                    break
            if k > -1:
                for i in range(k, self.board_size-1):
                    if self.board[i+1][j] == 0 or self.board[i][j] == self.board[i+1][j]:
                        return True
        return False

    #returns true if board can move left
    def canMoveLeft(self):
        for i in range(self.board_size):
            k = -1
            for j in range(self.board_size-1, -1, -1):
                if self.board[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, 0, -1):
                    if self.board[i][j-1] == 0 or self.board[i][j] == self.board[i][j-1]:
                        return True
        return False
    
    #returns true if board can move right
    def canMoveRight(self):
        for i in range(4):
            k = -1
            for j in range(self.board_size):
                if self.board[i][j] > 0:
                    k = j
                    break
            if k > -1:
                for j in range(k, self.board_size-1):
                    if self.board[i][j+1] == 0 or self.board[i][j] == self.board[i][j+1]:
                        return True
        return False
    
    #returns true if no moves can be made (games over)
    def isTerminal(self):
        if self.canMoveUp():
            return False
        if self.canMoveDown():
            return False
        if self.canMoveLeft():
            return False
        if self.canMoveRight():
            return False
        return True
    
    #creates a list of all moves that can be made in state
    def getAvailableMoves(self):
        moves = []

        if self.canMoveUp():
            moves.append('up')
        if self.canMoveDown():
            moves.append('down')
        if self.canMoveLeft():
            moves.append('left')
        if self.canMoveRight():
            moves.append('right')
        
        return moves
    
    #gets list of available moves
    def getChildren(self):
        return self.getAvailableMoves()
    
    #move the board given a direction string
    def move(self, direction):

        if direction == "up":
            self.merge_up()
        elif direction == "down":
            self.merge_down()
        elif direction == "left":
            self.merge_left()
        elif direction == "right":
            self.merge_right()

    #gets the direction given an initial board and a board after a direction was applied
    def getMoveTo(self, initial, target):
        if initial.canMoveUp():
            temp = copy.deepcopy(initial)
            temp.merge_up()
            temp.addTile()
            if temp.board == target.board:
                return "up"
        if initial.canMoveDown():
            temp = copy.deepcopy(initial)
            temp.merge_down()
            temp.addTile()
            if temp.board == target.board:
                return "down"
        if initial.canMoveLeft():
            temp = copy.deepcopy(initial)
            temp.merge_left()
            temp.addTile()
            if temp.board == target.board:
                return "left"
        if initial.canMoveRight():
            temp = copy.deepcopy(initial)
            temp.merge_right()
            temp.addTile()
            if temp.board == target.board:
                return "right"