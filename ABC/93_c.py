class Equal:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def solve(self):
        num = [self.a, self.b, self.c]
        odd = 0
        even = 0
        for i in range(3):
            if num[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        
        ans = 0
        if odd == 1:
            ans += 1
            for i in range(3):
                if num[i] % 2 == 0:
                    num[i] += 1
        elif odd == 2:
            ans += 1
            for i in range(3):
                if num[i] % 2 == 1:
                    num[i] += 1
        
        for i in range(3):
            ans += (max(num)-num[i]) // 2

        return ans

a, b, c = map(int, input().split())
print(Equal(a, b, c).solve())
