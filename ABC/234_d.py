import heapq
n, k = map(int, input().split())
P = list(map(int, input().split()))

que = P[:k]
print(min(que))
heapq.heapify(que)
for i in range(k, n):
    min_que = heapq.heappop(que)
    min_que = max(min_que, P[i])
    heapq.heappush(que, min_que)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)
