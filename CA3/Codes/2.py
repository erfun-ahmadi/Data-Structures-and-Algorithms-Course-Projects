import heapq

first_line = list(map(int,input().split()))
array = list(map(int,input().split()))
heapq.heapify(array)
array_nsmallest = list()
if first_line[0] >= first_line[2]:
    for i in range(first_line[2]):   
        heapq.heappush(array_nsmallest, -1*heapq.heappop(array))
array_size = first_line[0]
for i in range(first_line[1]):
    command = list(map(str,input().split()))
    if command[0] == '+':
        if array_size < first_line[2]-1:
            heapq.heappush(array, int(command[1]))
        elif array_size == first_line[2]-1:
            heapq.heappush(array, int(command[1]))
            for i in range(array_size+1):
                heapq.heappush(array_nsmallest, -1*heapq.heappop(array))
        elif int(command[1]) < array_nsmallest[0]*(-1):
            heapq.heappush(array, -1*heapq.heapreplace(array_nsmallest, -1*int(command[1])))
        else:
            heapq.heappush(array, int(command[1]))
        array_size += 1
    elif command[0] == '-' and array_size >= first_line[2]:
        if array_size > first_line[2]:
            heapq.heapreplace(array_nsmallest, -1*heapq.heappop(array))
        elif array_size == first_line[2]:
            heapq.heappop(array_nsmallest)
            for i in array_nsmallest:
                heapq.heappush(array, -1*i)
            array_nsmallest.clear()
        array_size -= 1        
    elif command[0] == 'print':
        if array_size < first_line[2]:
            print(-1)
        else:
            print(-1*array_nsmallest[0])