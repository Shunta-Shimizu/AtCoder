A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 2つの対角線が交点を持つか
# 線分ABと線分CDの交点存在判定関数
# False：交点なし　True：交点あり
# ACの直線式 (Xa - Xc) * (Y - Ya) - (Ya - Yc) * (X - Xa) = 0
# y = ax + b に　A(Xa, Ya)を代入 → Ya = a * Xa + b → b = Ya - a * Xa → 先頭に代入
# s, t > 0の時，直線の上側に点が存在
# s, t < 0の時，直線の下側に点が存在
# s, tの符号が異なるとき(s*t < 0)2点は直線を挟んで反対の位置
def cross_point(A, B, C, D):
    s = (A[0] - C[0]) * (B[1] - A[1]) - (A[1] - C[1]) * (B[0] - A[0])
    t =  (A[0] - C[0]) * (D[1] - A[1]) - (A[1] - C[1]) * (D[0] - A[0])
    if s*t > 0:
        return False

    s = (B[0] - D[0]) * (A[1] -  B[1]) - (B[1] - D[1]) * (A[0] - B[0])
    t = (B[0] - D[0]) * (C[1] - B[1]) - (B[1] - D[1]) * (C[0] - B[0])
    if s*t > 0:
        return False
    
    return True

if not cross_point(A, B, C, D):
    print("No")
else:
    print("Yes")