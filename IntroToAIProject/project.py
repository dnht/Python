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
#This function will receive input data :R,C, matrix
def input() :
    pass
R = int(input("Row size = ")) #rowsize
C = int(input("Column size = ")) #columnsize

#thiet lap so do 
matrix = []
for i in range(R+1):
    rowth = []
    for j in range(C+1):
        rowth.append([i,j])
    matrix.append(rowth)
for i in matrix:
    print(str(i))

sum = 0

#them vi tri cay song
para_1 = int(input("Number of live-trees = ")) #so cay song
sum += para_1
while sum > (R+1)*(C+1) - 1:
    print("Wrong input! Try again!")
    sum -= para_1
    para_1 = int(input("Number of live-trees = "))
    sum += para_1
live_tree = []
for i in range(1, para_1 + 1):
    axis = input() #example: 1,2
    r, c = axis.split(",")
    while [int(r),int(c)] == [0,0] or int(r) > R or int(c) > C or [int(r),int(c)] in live_tree:
        print("Wrong input! Try again!")
        axis = input() #example: 1,2
        r, c = axis.split(",")
    live_tree.append([int(r),int(c)])
    
print("Live-tree positions:", live_tree)

#them vi tri cay chet
para_2 = int(input("Number of dead-trees = ")) #so cay chet
sum += para_2
while sum > (R+1)*(C+1) - 1:
    print("Wrong input! Try again!")
    sum -= para_2
    para_2 = int(input("Number of dead-trees = "))
    sum += para_2
dead_tree = []
for i in range(1, para_2 + 1):
    axis = input() #example: 1,2
    r, c = axis.split(",")
    while [int(r),int(c)] == [0,0] or int(r) > R or int(c) > C or [int(r),int(c)] in live_tree or [int(r),int(c)] in dead_tree:
        print("Wrong input! Try again!")
        axis = input() #example: 1,2
        r, c = axis.split(",")
    dead_tree.append([int(r),int(c)])
    
print("Dead-tree positions:",dead_tree)

#them vi tri hat giong
para_3 = int(input("Number of seeds = ")) #so hat giong
sum += para_3
while sum > (R+1)*(C+1) - 1:
    print("Wrong input! Try again!")
    sum -= para_3
    para_3 = int(input("Number of seeds = "))
    sum += para_3
seed = []
for i in range(1, para_3 + 1):
    axis = input() #example: 1,2
    r, c = axis.split(",")
    while [int(r),int(c)] == [0,0] or int(r) > R or int(c) > C or [int(r),int(c)] in live_tree or [int(r),int(c)] in dead_tree or [int(r),int(c)] in seed:
        print("Wrong input! Try again!")
        axis = input() #example: 1,2
        r, c = axis.split(",")
    seed.append([int(r),int(c)])
print("Seed positions:",seed)

#them vi tri bu nhin 
para_4 = int(input("Number of scarecrows = ")) #so bu nhin 
sum += para_4
while sum > (R+1)*(C+1) - 1:
    print("Wrong input! Try again!")
    sum -= para_4
    para_1 = int(input("Number of scarecrows = "))
    sum += para_4
scarecrow = []
for i in range(1, para_4 + 1):
    axis = input() #example: 1,2
    r, c = axis.split(",")
    while [int(r),int(c)] == [0,0] or int(r) > R or int(c) > C or [int(r),int(c)] in live_tree or [int(r),int(c)] in dead_tree or [int(r),int(c)] in seed or [int(r),int(c)] in scarecrow:
        print("Wrong input! Try again!")
        axis = input() #example: 1,2
        r, c = axis.split(",")
    scarecrow.append([int(r),int(c)])
print("Scarecrow positions:",scarecrow)

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
