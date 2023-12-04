n, m, l = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = set()
for _ in range(l):
    c, d = map(int, input().split())
    CD.add((c, d))

# def max_dish_price(N, M, a, b, bad_combinations):
#     # 各主菜に対する最適な副菜の価格を計算
#     best_b = [float('inf')] * N
#     for c, d in bad_combinations:
#         best_b[c - 1] = min(best_b[c - 1], b[d - 1])

#     # 最も高い価格の定食を求める
#     # max_price = max(max(a[i] for i in range(N) if best_b[i] == float('inf'))), max(a[i] + best_b[i] for i in range(N) if best_b[i] != float('inf'))
#     max_without_bad_combinations = max((a[i] for i in range(N) if best_b[i] == float('inf')), default=0)
#     max_with_bad_combinations = max((a[i] + best_b[i] for i in range(N)), default=0)
#     max_price = max(max_without_bad_combinations, max_with_bad_combinations)
#     # 最も高い価格の定食を求める
#     return max_price

def max_dish_price(N, M, a, b, bad_combinations_set):
    # bad_combinations_set = set((c, d) for c, d in bad_combinations)

    max_price = 0
    for i in range(N):
        if (i + 1, 0) not in bad_combinations_set:
            max_price = max(max_price, a[i] + b[0])

    for j in range(M):
        if (0, j + 1) not in bad_combinations_set:
            max_price = max(max_price, a[0] + b[j])

    for i in range(1, N):
        for j in range(1, M):
            if (i + 1, j + 1) not in bad_combinations_set:
                max_price = max(max_price, a[i] + b[j])

    return max_price


result = max_dish_price(n, m, A, B, CD)
print(result)