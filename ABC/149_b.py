a, b, k = map(int, input().split())

ans_a = max(0, a-k)
if ans_a > 0:
    ans_b = b
else:
    ans_b = max(0, b-(k-a))

print(ans_a, ans_b)