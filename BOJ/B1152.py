word_list = list(map(str, input().split(' ')))

while '' in word_list:
    word_list.remove('')

print(len(word_list))