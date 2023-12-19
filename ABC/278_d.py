from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
q = int(input())

tf = False
add = defaultdict(int)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        tf = True
        all_num = query[1]
        add = defaultdict(int)
    elif query[0] == 2:
        add[query[1]-1] += query[2]
    else:
        if not tf:
            ans = A[query[1]-1]+add[query[1]-1]
        else:
            ans = all_num+add[query[1]-1]
        
        print(ans)
