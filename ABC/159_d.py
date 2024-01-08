from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
for i in range(n):
    count[A[i]] += 1

total = 0
for k, v in count.items():
    total += v*(v-1)//2

for i in range(n):
    if count[A[i]] == 1:
        ans = total
    else:
        ans = total-count[A[i]]*(count[A[i]]-1)//2+(count[A[i]]-1)*(count[A[i]]-2)//2 
    
    print(ans)