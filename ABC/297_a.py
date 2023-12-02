# n, d = map(int, input().split())
# T = list(map(int, input().split()))

# for i in range(n-1):
#     if T[i+1]-T[i] <= d:
#         print(T[i+1])
#         exit()

# print(-1)


# import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(A, B):
    if A == B:
        return 0
    elif A < B:
        A, B = B, A
    
    gcd_value = gcd(A, B)
    if gcd_value != 1:
        return -1
    
    cnt = 0
    while B > 0:
        cnt += A // B
        A, B = B, A % B
    if A != 1:
        return -1
    return cnt

def main():
    a, b = map(int, input().split())
    if a == b:
        print(0)
        exit()
    else:
        ans = solve(a, b)
        print(ans-1)
if __name__ == '__main__':
    main()


