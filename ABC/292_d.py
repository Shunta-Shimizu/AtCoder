class UnionFind:
    def __init__(self, n):
        # 親ノードを管理する配列
        self.parent = [i for i in range(n)]
        # 木の高さを管理する配列
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        # parent[x-1] = x のとき、xは根
        if self.parent[x] == x:
            return x
        else:
            # 根を探索する過程で親を更新（根を調べる計算量を減らすため）
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def unite(self, x, y):
        # 根を探索
        x = self.find(x)
        y = self.find(y)

        # 木の高さを比較し、低い方を高い方に結合
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

# n, m = map(int, input().split())
# uf = UnionFind(n)
# for _ in range(m):
#     u, v = map(int, input().split())
#     uf.unite(u, v)
import string
n = int(input())
S = input()

alphabet = string.ascii_uppercase
ans = ""
for i in range(len(S)):
    ans += alphabet[(alphabet.index(S[i])+n)%26]

print(ans)