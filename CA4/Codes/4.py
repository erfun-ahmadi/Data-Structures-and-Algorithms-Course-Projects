def build_graph(x, y):
    graph[x-1].append(y)
    graph[y-1].append(x)
    visited_from[x-1].append(False)
    visited_from[y-1].append(False)
    
def bfs_2D(x, parent):
    dist = [0]
    my_queue = [[x, parent]]
    len_queue = 1
    while len_queue != 0:
        my_queue.pop(0)
        len_queue -= 1
        for i in graph[x-1]:   
            if visited_from[i-1][graph[i-1].index(x)] == False and (parent, x, i) not in forbidden:
                my_queue.append([i, x])
                dist.append(dist[0]+1)
                len_queue += 1
                visited_from[i-1][graph[i-1].index(x)] = True
        dist.pop(0)
        if len_queue != 0:    
            parent = my_queue[0][1]
            x = my_queue[0][0]
        if x == org_des[1]:
            return dist[0]
    return -1

graph_inf = list(map(int, input().split()))
graph = list()
visited_from = list()
for i in range(graph_inf[0]):
    graph.append([])
    visited_from.append([])
for i in range(graph_inf[1]):
    edge = list(map(int,input().split()))
    build_graph(edge[0], edge[1])
org_des = list(map(int, input().split()))
num_forbidden = int(input())
forbidden = set()
for i in range(num_forbidden):
    path = list(map(int, input().split()))
    forbidden.add(tuple(path))
answer = list()
print(bfs_2D(org_des[0], -1))