import sys
sys.setrecursionlimit(15000)

def build_graph(x, y):
    graph[x-1].append(y)
    graph[y-1].append(x)
    

def find_cycle(x, parent):
    visited[x-1] = True
    for j in graph[x-1]: 
        if visited[j-1] == False:    
            if find_cycle(j, x) == True and x not in cycle:
                cycle.add(x)
                return True
            elif x in cycle: 
                return False
        elif j != parent:
            cycle.add(j)
            cycle.add(x)
            return True
    return False
            
def bfs(x):
    my_queue = [x]
    visited[x-1] = True
    distance[x-1] = 0
    len_queue = 1
    dist = 0
    while len_queue != 0:
        my_queue.pop(0)
        len_queue -= 1
        for i in graph[x-1]:
            dist = distance[x-1] + 1
            if distance[x-1] == 0:
                if i in cycle:
                    continue 
            if visited[i-1] == False:
                my_queue.append(i)
                visited[i-1] = True
                len_queue += 1
                distance[i-1] = dist
        if len_queue != 0:
            x = my_queue[0]
    
graph_inf = int(input())
graph = list()
distance = list()
for i in range(graph_inf):
    graph.append([])
distance = [None]*graph_inf
visited = [False]*graph_inf
cycle = set()
for i in range(graph_inf):
    edge = list(map(int,input().split()))
    build_graph(edge[0], edge[1])
find_cycle(1, -1)
for i in cycle:
    visited = [False]*graph_inf
    bfs(i)
print(*distance)