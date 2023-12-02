class Nine_Nine:
    def __init__(self, n):
        self.n = n
    
    def solve(self):
        total = 0
        for i in range(1, 10):
            for j in range(1, 10):
                total += i*j
        
        diff = total - self.n
        for k in range(1, 10):
            if diff % k == 0 and diff // k < 10:
                print(str(k) +  " x " + str(diff//k))

n = int(input())
Nine_Nine(n).solve()
