n = int(input())
D = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    ans = set()
    if len(str(i)) >= 2:
        for j in str(i):
            ans.add(int(j))
    else:
        ans.add(int(i))
    for j in range(1, D[i-1]+1):
        count_set = ans.copy()
        if len(str(j)) >= 2:
            for dj in str(j):
                count_set.add(int(dj))
        else:
            count_set.add(int(j))

        if len(count_set) == 1:
            count += 1
            
print(count)
    