def max_pyramid_size(N, A):
    result = 1  # 初期値として1を設定（最小のピラミッドサイズ）

    # Aの先頭から末尾まで順に見ていく
    for k in range(1, N):
        if A[k] <= A[k-1]:
            # A[k]がA[k-1]以下の場合、A[k]を1減少させても良い
            result = max(result, k + 1)
        else:
            # A[k]がA[k-1]より大きい場合、A[k]を1減少させずに進む
            result = max(result, k)

    # Aの末尾から先頭まで逆に見ていく
    for k in range(N-2, -1, -1):
        if A[k] <= A[k+1]:
            # A[k]がA[k+1]以下の場合、A[k]を1減少させても良い
            result = max(result, N - k)
        else:
            # A[k]がA[k+1]より大きい場合、A[k]を1減少させずに進む
            result = max(result, N - k - 1)

    return result

# 入力例
# N = 5
# A = [1, 3, 1, 2, 1]
N = int(input())
A = list(map(int, input().split()))
# 結果を求める
result = max_pyramid_size(N, A)
print(result)
