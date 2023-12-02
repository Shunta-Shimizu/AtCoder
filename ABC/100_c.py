class Three_Two:
    def __init__(self, n, A):
        self.n = n
        self.A = A
    
    def solve(self):
        ans = 0
        for i in range(self.n):
            num = self.A[i] 
            if num % 2 == 0:
                while num % 2 == 0:
                    num //= 2
                    ans += 1

        return ans

n = int(input())
A = list(map(int, input().split()))

ans = Three_Two(n, A)
print(ans.solve())