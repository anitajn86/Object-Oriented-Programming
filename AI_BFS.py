#Implementing the BFS in python
graph={
    'A':['C','B','E'],
    'B':['E','D'],
    'C':['F','G'],
    'D':['H','L'],
    'E':['I','J'],
    'F':['K'],
    'G':['K'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[]
}

visited=[]   #list for visited nodes
queue=[]     #initialize a queue

def bfs(visited,graph,node):  #function for bfs
    visited.append(node)
    queue.append(node)

    while queue:    #as long as queue is not empty, we create this loop to visit each node
        m=queue.pop(0)
        print(m, end=" ")

        for neighbour in graph [m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print('Following the breadth-first search,')
bfs(visited,graph,'A')
