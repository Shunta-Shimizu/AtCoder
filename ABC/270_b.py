X, Y, Z = map(int, input().split())

if X<Y<Z:
    if Z<0:
        print(abs(X))
    elif X<0 and Y<0 and Z>0:
        print(abs(X)+abs(Z)*2)
    elif X<0 and Y>0:
        print(abs(X))
    elif X>0:
        print(X)
elif X<Z<Y:
    if Y<0:
        print(-1)
    elif Y>0:
        print(abs(X))
    elif X>0:
        print(X)
elif Y<X<Z:
    if Y<0:
        print(abs(X))
    else:
        print(-1)
elif Y<Z<X:
    if Y<0:
        print(abs(X))
    else:
        print(-1)
elif Z<X<Y:
    if Z<0 and X<0 and Y<0:
        print(-1)
    elif Z<0 and X<0 and Y>0:
        print(abs(X))
    elif Z<0 and X>0:
        print(abs(X))
    else:
        print(abs(X))
elif Z<Y<X:
    if Z<0 and Y<0 and X<0:
        print(abs(X))
    elif Z<0 and Y<0 and X>0:
        print(abs(X))
    elif Z<0 and Y>0:
        print(abs(X)+abs(Z)*2)
    else:
        print(abs(X))
