from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

tmp = A[0]
total = abs(A[0])
for i in range(1, n):
    total += abs(A[i]-tmp)
    tmp = A[i]
# print(total)
time = defaultdict(int)
for i in range(n):
    time[i] = total
    if i == 0:
        time[i] -= abs(A[0])
        time[i] -= abs(A[i+1]-A[0])
        time[i] += abs(A[i+1])
        time[i] += abs(A[-1])
    elif i == n-1:
        if A[i] == A[i-1]:
            time[i] = time[i-1]
            continue
        time[i] -= abs(A[i]-A[i-1])
        time[i] += abs(A[-2])
    else:
        if A[i] == A[i-1]:
            time[i] = time[i-1]
            continue      
        time[i] -= abs(A[i]-A[i-1])
        time[i] -= abs(A[i+1]-A[i])
        time[i] += abs(A[i+1]-A[i-1])
        time[i] += abs(A[-1])

for ans in time.values():
    print(ans)