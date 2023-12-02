from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

nums = defaultdict(int)
for a in A:
    if a % 4 == 0:
        nums[4] += 1
    elif a % 4 != 0 and a % 2 == 0:
        nums[2] += 1
    else:
        nums[1] += 1

if nums[4]+(nums[2]//2) >= n//2:
    print("Yes")
else:
    print("No")
