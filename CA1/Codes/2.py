num_of_words = int(input())
first_letters = dict()
repeated_letters = list()
for i in range(num_of_words):
    word = input()
    if word[0] in first_letters.keys():
        first_letters[word[0]] += 1
    else:
        first_letters[word[0]] = 1
for letter in first_letters.keys():
    if first_letters[letter] >= 5:
        repeated_letters.append(letter)
repeated_letters.sort()
if len(repeated_letters) != 0:
    print(*repeated_letters, sep='')
else:
    print("How long must I suffer")