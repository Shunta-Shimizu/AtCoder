import math
n, a, b = map(int, input().split())

ans = n*(n+1)//2
fizz = (n//a)*(n//a+1)//2
buzz = (n//b)*(n//b+1)//2

lcm_ab = math.lcm(a, b)
fizzbuzz = (n//lcm_ab)*(n//lcm_ab+1)//2

ans -= (a*fizz+b*buzz)-lcm_ab*fizzbuzz
print(ans)
# 嘘解法
# ans = (n+1)*n//2
# diff = 0

# if a == 1 or b == 1:
#     print(0)
#     exit()

# if a > n:
#     m = 0
# else:
#     i = 0
#     m = 0
#     while a*i <= n:
#         m += a*i
#         i += 1

# if b > n:
#     m2 = 0
# else:
#     m2 = 0
#     j = 0
#     while b*j <= n:
#         m2 += b*j
#         j += 1

# c = math.lcm(a, b)
# if c > n:
#     m3 = 0
# else:
#     m3 = 0
#     k = 0
#     while c*k <= n:
#         m3 += c*k
#         k += 1

# # print(m, m2, m3)
# diff = m+m2-m3
# ans -= diff
# print(ans)

