n = int(input())
word = ""
for i in range(0, n):
    answer = list()
    inputs = list(map(str, input().split()))
    if inputs[0] == "push":
        word = word + inputs[1]
    else:
        word = word[1:]
    for a in range(0,len(word)):
        for b in range(a+1, len(word)+1):
            part = word[a:b]
            part2 = part[::-1]
            if part == part[::-1]:
                answer.append(part)
    answer = set(answer)
    print(len(answer))
                
                
    
    