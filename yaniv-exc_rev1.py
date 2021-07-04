# import numpy
import numpy as np
import random
import concurrent.futures

class Maze_builder:
    def __init__(self,inputboard):
        self.inputboard = inputboard
        self.outputBoard  = np.chararray(self.inputboard.shape) 
        self.outputBoard[:] = " "
 
    def wall_decision(self,neighbors):
        """ return decision for each wall """
        if sum(neighbors)>2:
            return "+"
        
        if sum(neighbors[:2])==2:
            return "|"
        
        if sum(neighbors[2:])==2:
            return "-"
        
        if sum(neighbors)<=1:
            return "o"
        
        return "+"

    def wall_detector(self,i,j,neighbors,):
        """ 
            wall detector - a recursion function that follow the walls for each side .
            i,j index for matrix data.
            neighbors is array of the neighbor - [down, top ,right ,left] 
        """
        # recursion stop condition 1/2
        if self.inputboard[i,j]==0:
            #stop
            return 0

        # recursion stop condition 2/2
        if self.outputBoard[i,j] == b't':
            return 1
        else:
            # Leave a trail
            self.outputBoard[i,j] = 't'


        # check down
        if i+1 < self.inputboard.shape[0]:
            if neighbors[0]==0:
                neighbors[0] = self.wall_detector(i+1,j,[0,1,0,0])

        
        # check top
        if i-1 >= 0:
            if neighbors[1]==0:
                neighbors[1] = self.wall_detector(i-1,j,[1,0,0,0])


        # check Right
        if j+1 < self.inputboard.shape[1]:
            if neighbors[2]==0:
                neighbors[2] = self.wall_detector(i,j+1,[0,0,0,1])

        # check Left
        if j-1 >= 0:
            if neighbors[3]==0:
                neighbors[3] = self.wall_detector(i,j-1,[0,0,1,0])

        # take decision for each wall using next function
        self.outputBoard[i,j]= self.wall_decision(neighbors)
        return 1

    def build(self):
        for i in range(len(self.inputboard)):
            for j in range(len(self.inputboard[i])):
                if self.inputboard[i,j]==1 and self.outputBoard[i,j]=="":
                    # go left/right/top/bottom this section will be recursive
                    self.wall_detector(i,j,[0,0,0,0])
        return self.outputBoard

if __name__=="__main__":
    #exmple data
    npdata = np.array([
                    [1, 1, 1, 0, 1], 
                    [1, 0, 0, 0, 1], 
                    [1, 0, 1, 0, 1], 
                    [0, 0, 0, 0, 1], 
                    [1, 1, 1, 1, 1], 
                ])
    
    board_size = 8
    npdata = np.random.randint(2, size=(board_size, board_size))

    # testBoard  = np.chararray(npdata.shape) 
    # testBoard[:] = " "

    # for i in range(len(npdata)):
    #         for j in range(len(npdata[i])):
                

    print(npdata)
    
    maze= Maze_builder(npdata)
    print(maze.build())
