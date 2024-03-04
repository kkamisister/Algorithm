# BOJ 2869 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())
days = (V-B-1)//(A-B) + 1

print(days)1