size = input()
inputs = list(map(int,input().split()))
inputs.insert(0, 0)
inputs.append(0)
periods = list()
period_beggining = list()
for i in range(1, len(inputs)):
    if inputs[i] > inputs[i-1]:
        for j in range(0, (inputs[i]-inputs[i-1])):
            period_beggining.append(i)
    elif inputs[i] < inputs[i-1]:
        for j in range(0, (inputs[i-1]-inputs[i])):
            periods.append([period_beggining[-1], i-1])
            period_beggining.pop()
periods.sort()
for i in range(0, len(periods)):
    print(*periods[i])
            