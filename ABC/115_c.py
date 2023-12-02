class tree:
    def __init__(self, n, k, H):
        self.n = n
        self.k = k
        self.H = H
        self.H_sort = sorted(self.H)
    
    def search(self):
        ans = 10**10
        for i in range(self.n-self.k+1):
            ans = min(ans, self.H_sort[i+k-1]-self.H_sort[i])

        return ans

n, k = map(int, input().split())
H = []
for _ in range(n):
    h = int(input())
    H.append(h)

ans = tree(n, k, H)
print(ans.search())