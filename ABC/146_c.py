a, b, x = map(int, input().split())

# left: ok, right: over NG
left = 0
right = 10**9+1
p = 0
while right-left > 1:
    mid = (left+right)//2
    p =  a*mid+b*len(str(mid))
    if p <= x:
        left = mid
    elif p > x:
        right = mid

print(left)
# if p > x:
#     right = mid
#     mid = (left+right)//2
#     print(mid)
# else:
#     print(mid)