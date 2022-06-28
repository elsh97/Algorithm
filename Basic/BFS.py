from collections import deque

#Breadth First Search
def BFS(graph, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for n in graph[v]:
            if not visited[n]:
                queue.append(n)
                visited[n]=True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
BFS(graph, 1, visited)