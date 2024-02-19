import sys
sys.stdin = open('input.txt')

dwarfs = []
for dwarf in range(9):
    dwarfs.append(int(input()))

height_gap = sum(dwarfs) - 100

flag = False
for a in dwarfs:
    for b in dwarfs:
        if a != b and a + b == height_gap:
            dwarfs.remove(b)
            dwarfs.remove(a)
            flag = True
            break
    if flag:
        break
dwarfs.sort()
for i in dwarfs:
    print(i)