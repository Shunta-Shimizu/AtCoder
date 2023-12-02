from collections import defaultdict
n = int(input())
S = input()

ans = S[0]
count_ans = defaultdict(set)
count_ans[ans].add(1)
count = 1
for i in range(1, n):
    if ans == S[i]:
        count += 1
        count_ans[S[i]].add(count)
    else:
        count_ans[ans[-1]].add(count)
        count = 1
        count_ans[S[i]].add(count)
        ans = S[i]

# print(count_ans)
a = 0
for k, v in count_ans.items():
    a += len(v)

print(a)