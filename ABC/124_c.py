class tile:
    def __init__(self, S):
        self.S = list(S)
        self.ans = 0
    
    def paint(self):
        ans = self.ans
        for i in range(1, len(self.S)):
            if self.S[i-1] == self.S[i]:
                if self.S[i] == "0":
                    self.S[i] = "1"
                else:
                    self.S[i] = "0"
                ans += 1
        
        return ans

S = input()
t = tile(S)
print(t.paint())