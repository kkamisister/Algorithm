import sys
sys.stdin = open('input.txt')

def real_dwarfs(
dwarfs = []
for dwarf in range(9):
    dwarfs.append(int(input()))

height_gap = sum(dwarfs) - 100

for a in dwarfs:
    for b in dwarfs:
        if a != b and a + b == height_gap:
            dwarfs.remove(b)
            dwarfs.remove(a)
    if len(dwarfs) == 7:
        break
dwarfs.sort()
for i in dwarfs:
    print(i)