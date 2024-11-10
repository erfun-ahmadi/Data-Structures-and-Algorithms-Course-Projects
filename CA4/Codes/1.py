def build_graph(x, y):
    graph[x-1].append(y)
    graph[y-1].append(x)
   
def bfs(x, my_queue):
    my_queue.append(x)
    my_visited2[x-1] = True
    len_queue = len(my_queue)
    len_traversed1 = 1
    while len_queue != 0:
        my_queue.pop(0)
        len_queue -= 1
        for i in graph[x-1]:
            if my_visited2[i-1] == False:
                my_queue.append(i)
                my_visited2[i-1] = True
                len_queue += 1
                traversed.append(i)
                len_traversed1 += 1
        if len_queue != 0:
            x = my_queue[0]
    return len_traversed1

        
def dfs(x, my_stack):
    my_stack.append(x)
    my_visited1[x-1] = True
    for i in graph[x-1]:
        if my_visited1[i-1] == False:
            dfs(i, my_stack)
    
graph_inf = list(map(int,input().split()))
graph = list()
traversed = list()
visited = list()
for i in range(graph_inf[0]):
    graph.append([])
    visited.append(False)
for i in graph:
    i.sort()
for i in range(graph_inf[1]):
    edge = list(map(int,input().split()))
    build_graph(edge[0], edge[1])
num_of_req = int(input())
for i in range(num_of_req):
    req = list(map(str, input().split()))
    if int(req[0]) == 1 and req[1] == "BFS":
        my_queue = list()
        my_visited2 = visited[:]
        traversed = [int(req[2])]
        len_traversed = 1
        print(bfs(int(req[2]), my_queue))
    elif int(req[0]) == 1 and req[1] == "DFS":
        my_stack = list()
        my_visited1 = visited[:]
        dfs(int(req[2]), my_stack)
        print(len(my_stack))
        traversed = my_stack[:]
    elif int(req[0]) == 2:
        if len(traversed) == 0 or int(req[1]) > len(traversed):
            print(-1)
        else:
            print(traversed[int(req[1])-1])