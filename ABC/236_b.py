from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
for a in A:
    count[a] += 1

for key in count.keys():
    if count[key] != 4:
        print(key)
        break