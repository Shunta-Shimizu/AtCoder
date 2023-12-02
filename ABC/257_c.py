from collections import defaultdict
n = int(input())
S = input()
W = list(map(int, input().split()))

data = defaultdict(list)
for i in range(n):
    data[W[i]].append(i) 

data = dict(sorted(data.items()))
bound = 0
correct_count = S.count("1")
ans = correct_count
# print(data)
for key in data.keys():
    for i in data[key]:
        if S[i] == "1":
            correct_count -= 1
        else:
            correct_count += 1
    ans = max(ans, correct_count)

print(ans)