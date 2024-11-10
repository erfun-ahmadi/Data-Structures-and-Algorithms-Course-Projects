import heapq

inputs = list(map(int,input().split()))
little_sisters = list(map(int,input().split()))
get_up_order = list()
len_get_up_order = inputs[0]
waiting_line = list()
len_waiting_line = 0
adam_queue = list()
len_adam_queue = 0
answer = list()
num_of_vaccinated = 0
for i in range(inputs[0]):
    heapq.heappush(get_up_order, [little_sisters[i], i])
    answer.append(None)
time_to_make_adam = 0
while num_of_vaccinated != inputs[0]:
    if len_adam_queue == 0:
        time_to_make_adam = get_up_order[0][0]
        adam_queue.append(heapq.heappop(get_up_order))
        len_adam_queue += 1
        len_get_up_order -= 1
    if len_get_up_order == 0:
        answer[adam_queue[0][1]] = time_to_make_adam + inputs[1]
        adam_queue.pop(0)
        len_adam_queue -= 1
        time_to_make_adam += inputs[1]
        num_of_vaccinated += 1
    elif get_up_order[0][0] > time_to_make_adam + inputs[1]:
        answer[adam_queue[0][1]] = time_to_make_adam + inputs[1]
        adam_queue.pop(0)
        len_adam_queue -= 1
        time_to_make_adam += inputs[1]
        num_of_vaccinated += 1
    else:
        if get_up_order[0][1] < adam_queue[len_adam_queue-1][1]:
            adam_queue.append(heapq.heappop(get_up_order))
            len_adam_queue += 1
            len_get_up_order -= 1
        else:
            change_priority = heapq.heappop(get_up_order)
            change_priority[0], change_priority[1] = change_priority[1], change_priority[0]
            heapq.heappush(waiting_line, change_priority)
            len_get_up_order -= 1
            len_waiting_line += 1
    if len_adam_queue == 0 and len_waiting_line != 0:
        change_priority = heapq.heappop(waiting_line)
        change_priority[0], change_priority[1] = change_priority[1], change_priority[0]
        heapq.heappush(adam_queue, change_priority)
        len_adam_queue += 1
        len_waiting_line -= 1
            
print(*answer)       