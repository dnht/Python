N=1000#define N
R=0 #initiate the row size
C=0 #initiate the column size
matrix=[] #state of each cell [i][j] in the garden
move=[[0,1],[1,0],[-1,0],[0,-1]] #move we can conduct
#x,y  x move[i][0] y move[i][1]  for i in range(0,4)
step=[[0]*(N+1)for i in range(N+1)]#the smallest step it takes to get to (i,j) from (0,0)
visited=[[False] * (N+1) for i in range(N+1)] #define that the cell is visited or not(initiate all to false at first)
#visite[x][y] kiem tra xem toa do [x][y] da duoc di den hay chua
percept_sequence= []
action=[]
stack=[]
total_steps=0

#------------------------------------------------------------------------------------------------------------------
#This function will receive input data :R,C, matrix (Trang)
def input() :
    pass

#This function  will calculate the execution time and return it(Tuyen)
def executionTimeCount():
    pass

#This function will find the shortest path, percept sequence , action needed to take
# from (0,0) to (i,j) using IDA*(Chien)(Tuyen)
def shortestPath(i,j):
    pass

#This function will find the shortest path, percept sequence , action needed to take
# from (0,0) to (i,j) using BFS(Minh)
def BFS():
    pass
def shortestPathBFS(i,j) :
    pass

#This function will visit every cell in the matrix, percept sequence, action needed
# for the AI to finish work(Minh)
def DFS():
    pass


#Main
