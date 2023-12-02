from collections import defaultdict

n = int(input())

vote = defaultdict(int)
for _ in range(n):
    s = input()
    vote[s] += 1

vote_sort = sorted(vote.items(), key=lambda x:x[1])
print(vote_sort[-1][0])