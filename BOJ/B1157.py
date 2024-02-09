word = str(input())

upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = word.upper()

count_list = [0 for i in range(len(upper_list))]

for i in range(len(word)):
    for j in range(len(upper_list)):
        if word[i] != upper_list[j]:
            pass
        else:
            count_list[j] += 1

max_count = max(count_list)
for i in 