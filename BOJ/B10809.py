S = str(input())
only_string = []

for string in S:
    if string not in only_string:
        only_string.append(string)
    else:
        only_string.append(0)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for alph in alphabet:
    if alph not in only_string:
        print(-1, end=' ')
    else:
        a = -1
        for string in only_string:
            if alph == string:
                print(a+1, end=' ')
            else:
                a += 1