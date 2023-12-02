from collections import defaultdict
class Diverse:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    
    def solve(self, A):
        count = defaultdict(int)
        for i in range(self.n):
            count[A[i]] += 1
        
        count = dict(sorted(count.items(), key=lambda x:x[1]))
        kind = len(count)
        ans = 0
        for key, v in count.items():
            if kind > self.k:
                ans += v
                kind -= 1

        return ans

n, k = map(int, input().split())
A = list(map(int, input().split()))
print(Diverse(n, k).solve(A))
