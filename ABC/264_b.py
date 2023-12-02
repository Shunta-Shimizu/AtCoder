r, c = map(int, input().split())
# リストの初期化は内包表記で行う
# grid = [["white"] * 15] * 15 とすると二次元配列の要素（リスト）が全て同じものとして扱われる
grid = [["white"] * 15 for _ in range(15)]
# print(*grid, "\n")

for i in range(15):
    if i % 2 == 0:
        for j in range(i, 15-i):
            grid[i][j] = "black"
            grid[j][i] = "black"
            grid[-i-1][j] = "black"
            grid[j][-i-1] = "black"

# grid全体を表示
# for k in range(15):
#     print(*grid[k])

print(grid[r-1][c-1])

