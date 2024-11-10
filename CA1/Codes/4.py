inputs = list(map(int,input().split()))
num_of_players = inputs[0]
num_of_rounds = inputs[1]
wanted = inputs[2]
players = list()
swaps = [2, 3]
for i in range(1, num_of_players+1):
    players.append(i)

j = 4
while len(swaps) < num_of_rounds:
    for i in range(len(swaps)):
        if j % 6 != 1 and j % 6 != 5:
            break
        if j % swaps[i] == 0:
            break
        elif j % swaps[i] != 0 and swaps[i] >= j**0.5:
            swaps.append(j)
            break
    j += 1

# print(swaps)
wanted_index = players.index(wanted)
for i in range(num_of_rounds):
    if wanted_index == 0:
        wanted_index = swaps[i] % num_of_players
    else:
        wanted_index -= (swaps[i]//(num_of_players-1))
        while wanted_index < 0:
            wanted_index += num_of_players
        if wanted_index <= swaps[i] % (num_of_players-1):
            wanted_index -= 1
        while wanted_index < 0:
            wanted_index += num_of_players

swaps.reverse()
wanted_index1 = wanted_index + 1
wanted_index2 = wanted_index - 1
if wanted_index1 > num_of_players-1:
    wanted_index1 -= num_of_players
if wanted_index2 < 0:
    wanted_index2 += num_of_players
for i in range(num_of_rounds):
    if wanted_index1 - (swaps[i] % num_of_players) == 0:
        wanted_index1 = 0
    else:
        if (wanted_index1 + 1) % num_of_players <= swaps[i] % num_of_players:
            wanted_index1 += 1        
        while wanted_index1 > num_of_players-1:
            wanted_index1 -= num_of_players
        wanted_index1 += (swaps[i]//num_of_players)
        while wanted_index1 > num_of_players-1:
            wanted_index1 -= num_of_players
    
    if wanted_index2 - (swaps[i] % num_of_players) == 0:
        wanted_index2 = 0
    else:
        if (wanted_index2 + 1) % num_of_players <= swaps[i] % num_of_players:
            wanted_index2 += 1
        while wanted_index2 > num_of_players-1:
            wanted_index2 -= num_of_players
        wanted_index2 += (swaps[i]//num_of_players)
        while wanted_index2 > num_of_players-1:
            wanted_index2 -= num_of_players
        
    
print(players[wanted_index1], players[wanted_index2])        

# wanted_index = players.index(wanted)
# if wanted_index != 0 and wanted_index != len(players)-1:
#     print(players[wanted_index+1], players[wanted_index-1])
# elif wanted_index == 0:
#     print(players[wanted_index+1], players[len(players)-1])
# elif wanted_index == len(players)-1:
#     print(players[0], players[wanted_index-1])
