import itertools

# 順列
A = [1, 2, 3, 4, 5]
A = list(itertools.permutations(A, 4))
print("順列の結果を出力　長さ:{}".format(len(A)))
print(A)

# 組み合わせ
A = [1, 2, 3, 4, 5]
A = list(itertools.combinations(A, 3))
print("組合せの結果を出力　長さ:{}".format(len(A)))
print(A)

# 直積（2つの集合から要素を1つずつとって組を作成）
A = [1, 2, 3, 4]
B = ["a", "b"]
C =["C", "D", "E"]
p = list(itertools.product(A, B, C))
print("直積の結果を出力　長さ:{}".format(len(p)))
print(p)

# 重複順列
A = ["a", "b", "c"]
A = list(itertools.product(A, repeat=3))
print("重複順列の結果を出力 長さ:{}".format(len(A)))
print(A)

# 重複組合せ
A = ["a", "b", "c"]
A = list(itertools.combinations_with_replacement(A, 3))
print("重複組合せの結果を出力　長さ:{}".format(len(A)))
print(A)