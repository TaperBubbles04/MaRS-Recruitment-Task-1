from collections import deque

#creating a grid
grid=[]
for i in range(11):
    row=[]
    for j in range(11):
        row.append(1)
    grid.append(row)

#reading the file to see where the obstacles are
try:
    with open('sample.txt', 'r') as f:
        for line in f:
            if ' ' in line:
                pos= line.split()
            else:
                pos= list(line.strip())    #removing the white spaces
                
            if len(pos) >= 4:
                n=int(pos[0])
                e=int(pos[1])
                s=int(pos[2])
                w=int(pos[3])
                
                x= e-w
                y= n-s
                
                if 0<=x<11 and 0<=y<11:
                    grid[x][y]=0
except FileNotFoundError:
    pass

for i in range(10, -1, -1):
    for j in range(11):
        print(grid[j][i], end=' ')
    print('\n')

#using breadth-first search method
queue= deque()                          #using deque in order to get the oldest instruction first
queue.append(((0, 0), [(0, 0)]))        #initialising current position and path
v={(0, 0)}
fp=[]

#for each direction accounting for the change in x and y
dir= [(-1, 0), (1, 0), (0, 1), (0, -1)]

#applying the breadth-first search method
while len(queue) > 0:
    cur=queue.popleft()
    curpos= cur[0]
    path= cur[1]
    
    cx=curpos[0]
    cy=curpos[1]
    
    #checking if final destination is reached
    if cx==10 and cy==10:
        fp= path
        break
        
    #trying all 4 directions step-by-step
    for d in dir:
        dx= d[0]
        dy= d[1]
        
        nx= cx+dx
        ny= cy+dy
        
        #Verifying if the new position is obstacle or not
        if 0<=nx<11:
            if 0<=ny<11:
                if grid[nx][ny]==1:
                    if (nx, ny) not in v:
                        v.add((nx, ny))
                        
                        #adding the new step taken
                        npath = list(path)
                        npath.append((nx, ny))
                        
                        #adding the new path to the queue
                        queue.append(((nx, ny), npath))

#displaying the result for shortest path taken
if len(fp)>0:
    print(fp)
else:
    print("No path found.")