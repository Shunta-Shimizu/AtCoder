class Gift:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def solve(self):
        ans = 1
        num = self.x
        while num*2 <= self.y:
            num *= 2
            ans += 1

        return ans

x, y = map(int, input().split()) 
print(Gift(x, y).solve())