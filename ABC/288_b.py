n , k = map(int, input().split())

name = []
for _ in range(n):
    name.append(input())

name = sorted(name[:k])

print(*name, sep="\n")