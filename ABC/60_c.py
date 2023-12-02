class Sentou:
    def __init__(self, n, t):
        self.n = n
        self.t = t
    
    def solve(self, T):
        ans = 0
        for i in range(self.n):
            if i == n-1:
                ans += t
            else:
                if T[i+1]-T[i] > t:
                    ans += t
                else:
                    ans += T[i+1]-T[i]
        return ans


n, t = map(int, input().split())
T = list(map(int, input().split()))
print(Sentou(n, t).solve(T))