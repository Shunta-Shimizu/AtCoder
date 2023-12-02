from collections import defaultdict

h1, w1 = map(int, input().split())
A_list = []
for _ in range(h1):
    A = list(map(int, input().split()))
    A_list.append(A)

h2, w2 = map(int, input().split())
B_list = []
for _ in range(h2):
    B = list(map(int, input().split()))
    B_list.append(B)

# ans = [[] for _ in range(h2)] 
m = 0
# del_row = set()
# del_col = set()
del_row_col = defaultdict(list)
for i in range(h2):
    for j in range(w2):
        # print(B_list[i][j])
        for k in range(h1):
            for l in range(w1):
                # print(A_list[k][l])
                if B_list[i][j] == A_list[k][l]:  #and len(ans[i]) <= w2:
                    # print(A_list[k][l], B_list[i][j])
                    del_row_col[k].append(l)
                    # del_row.add(k)
                    # del_col.add(l)
                    
print(del_row_col)
del_col = list()
for key in del_row_col.keys():
    if del_row_col[key] not in del_col:
        del_col.append(del_row_col[key])

# print(del_col)
if len(del_col) == 1:
    print("Yes")
else:
    print("No")








