class cube:
    def __init__(self, S):
        self.S = list(S)
        self.zero_c = 0
        self.one_c = 0

    def forward(self):
        zero_c = self.zero_c
        one_c = self.one_c
        for i in range(len(self.S)):
            if self.S[i] == "0":
                zero_c += 1
            else:
                one_c += 1
        
        ans = min(zero_c, one_c) * 2

        return ans
    
S = input()
ans = cube(S)
print(ans.forward())




