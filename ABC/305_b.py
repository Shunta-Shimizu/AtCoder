from collections import defaultdict
p, q = map(str, input().split())

point = ["A", "B", "C", "D", "E", "F", "G"]
dst = [0, 3, 4, 8, 9, 14, 23]

ans = abs(dst[point.index(p)] - dst[point.index(q)])

print(ans)
