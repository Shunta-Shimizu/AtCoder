class min_price:
    def __init__(self, n, m, AB):
        self.n = n
        self.m = m
        self.AB = AB
    
    def calc_price(self):
        ans = 0
        AB_sort = sorted(self.AB, key=lambda x:x[0])
        for i in range(self.n):
            if AB_sort[i][1] < self.m:
                ans += AB_sort[i][0] * AB_sort[i][1]
                self.m -= AB_sort[i][1]
            elif AB_sort[i][1] >= self.m:
                ans += AB_sort[i][0] * self.m
                break
            # print(self.m)
        return ans


n, m = map(int, input().split())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])

price = min_price(n, m, AB)
print(price.calc_price())
