def find_max(number, n):
    len_number = len(number)
    maximum = list()
    if n == 0:
        return maximum
    maximum.append(number[0])
    len_maximum = 1
    for i in range(1, len_number):
        if number[i] <= maximum[-1] and len_maximum < n:
            maximum.append(number[i])
            len_maximum += 1
        elif number[i] > maximum[-1]:
            while number[i] > maximum[-1] and (len_number-i)+(len_maximum-1) >= n:
                maximum.pop()
                len_maximum -= 1
                if len_maximum == 0:
                    break
            maximum.append(number[i])
            len_maximum += 1
    return maximum
           
def merge_max(first, second):
    return [max(first, second).pop(0) for i in first+second]

size = int(input())
first_number = list(map(int,input().split()))
second_number = list(map(int,input().split()))
len_first = len(first_number)
len_second = len(second_number)
merged = [[-1]]
max_first = list()
max_second = list()
for i in range(max(0,size-len_first), min(size, len_second)+1):  
    max_first = find_max(first_number, size-i)
    max_second = find_max(second_number, i)
    mrg = merge_max(max_first, max_second)
    if mrg > merged[0]:
        merged.pop()
        merged.append(mrg)

print(*merged[0])
    

