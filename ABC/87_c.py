class Candies:
    def __init__(self, n):
        self.n = n
    
    def solve(self, A1, A2):
        ans = 0
        for i in range(self.n):
            c = 0
            j = n-i
            for k in range(i+1):
                c += A1[k]
            for l in range(j):
                c += A2[i+l]
            ans = max(ans, c)
        
        return ans

n = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

print(Candies(n).solve(A1, A2))




                

