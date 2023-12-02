A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 三角形の内部に点を持つかを判定
# 外積 (Outer Product)
def vec(P, Q):
    return (Q[0]-P[0], Q[1]-P[1])

def InTriangle(A, B, C, D):
    vec_ab = vec(A, B)
    vec_bc = vec(B, C)
    vec_ca = vec(C, A)

    vec_ad = vec(A, D)
    vec_bd = vec(B, D)
    vec_cd = vec(C, D)

    OP_ab_ad = vec_ab[0] * vec_ad[1] - vec_ab[1] * vec_ad[0]
    OP_bc_bd = vec_bc[0] * vec_bd[1] - vec_bc[1] * vec_bd[0]
    OP_ca_cd = vec_ca[0] * vec_cd[1] - vec_ca[1] * vec_cd[0]

    if OP_ab_ad > 0 and OP_bc_bd > 0 and OP_ca_cd > 0: #or (OP_ab_ad < 0 and OP_bc_bd < 0 and OP_ca_cd < 0) 
        return True
    else:
        return False

if InTriangle(A, B, C, D) or InTriangle(B, C, D, A) or InTriangle(C, D, A, B) or InTriangle(D, A, B, C):
    print("No")
else:
    print("Yes")

