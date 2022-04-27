class Node:
    def __init__(self,data,level,fvalue):                           # Initialize node with data, level of node and fvalue
        self.data = data
        self.level = level
        self.fvalue = fvalue

    def generate_child(self):                                               # Generate child nodes from the given node by moving  
                                                                            # blank space either in the four directions up,down,left,right
        x,y = self.find(self.data, '_')                                     # get index of blank space in current matrix

        directions_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]                 # contains index values for moving blank space in either of the 4 directions
        children = []                                                       # 
        for i in directions_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])               # shuffle data from x,y index to each direction's index
            if child is not None:
                child_node = Node(child, self.level+1, 0)                   # create a node by providing data , level and fvalue
                children.append(child_node)                                 # add node to children list 
        return children
        
    def shuffle(self, puzzle, x1, y1, x2, y2):                              # Move the blank space in the given direction  
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puzzle = []                                                # if indexes are in limits interchange the data from original index    
            temp_puzzle = self.copy(puzzle)                                 # to said direction
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:                                                               # if  index value are out of limits then return None
            return None
            

    def copy(self,root):                                                    # Copy function to create a similar matrix of the given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):                                                   # method to find the position of the blank space
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):                                                #Initialize the puzzle size by the specifying
        self.n = size                                                       # size of matrix 
        self.open = []                                                      # open list
        self.closed = []                                                    # closed list

    def accept(self):
        puz = []    
        for i in range(0,self.n):                                   
            temp = input().split(" ")                                       # accept puzzle matrix
            puz.append(temp)
        return puz

    def f(self,start, goal):
        return self.h(start.data, goal) + start.level                       # Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) 

    def h(self, start, goal):                                                # Calculate the difference between start / current state and goal state
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':        # if state not equal to goal state and state not equal to empty
                    temp += 1                                               # increment counter by 1    
        return temp
        

    def astar(self):
        print("Enter the start state matrix ")                            
        start = self.accept()                                               # accept start state matrix
        
        print("Enter the goal state matrix ")                         
        goal = self.accept()                                                # accept goal state matrix

        start = Node(start,0,0)                                             # create a node by providing data of start state martrix, level = 0 and fvalue = 0
        start.fvalue = self.f(start, goal)                                  # calcualte f value for start state and set to start node             
        
        self.open.append(start)                                             # add the start node in the open list
        print("\n\n")   
        while True:
            current_node = self.open[0]                                     # take first node from open list
            print("\n  || \n \\\'\'/ \n")
    
            for i in current_node.data:                                     # print puzzle
                for j in i:
                    print(j,end=" ")
                print("")
           
            if(self.h(current_node.data,goal) == 0):                        # If difference between current and goal node is 0, we have reached the goal node then break
                break
            
            for i in current_node.generate_child():
                i.fvalue = self.f(i,goal)                                   # calcualte f value for node from child generated nodes of current node       
                self.open.append(i)                                         # add new generate node to open list
            self.closed.append(current_node)                                # add current node to closed list
            del self.open[0]                                                # remove node from the open list

            self.open.sort(key = lambda x:x.fvalue, reverse=False)           # sort the open list based on f value, so that first node will have min fvalue
    
npuzzle = Puzzle(3)
npuzzle.astar()

"""
Output 

Enter the start state matrix 
_ 1 3
4 2 5
7 8 6
Enter the goal state matrix 
1 2 3
4 5 6
7 8 _



  || 
 \''/ 

_ 1 3 
4 2 5 
7 8 6 

  || 
 \''/ 

1 _ 3
4 2 5
7 8 6

  ||
 \''/

1 2 3
4 _ 5
7 8 6

  ||
 \''/

1 2 3
4 5 _
7 8 6 

  ||
 \''/

1 2 3
4 5 6
7 8 _

"""