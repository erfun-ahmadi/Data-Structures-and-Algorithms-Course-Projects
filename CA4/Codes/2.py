first = input()
second = input()
letters = list(set(first+second))
letters_flag = [i for i in range(len(letters))]
count = 0
for i in range(len(first)):
    if letters_flag[letters.index(first[i])] != letters_flag[letters.index(second[i])]:
        count += 1
        tmp = letters_flag[letters.index(first[i])]
        for j in range(len(letters)):
            if letters_flag[j] == tmp:
                letters_flag[j] = letters_flag[letters.index(second[i])]
print(count)