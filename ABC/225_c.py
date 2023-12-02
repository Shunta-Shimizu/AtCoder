n, m = map(int, input().split())

B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

for i in range(m-1):
    # if B[0][i+1] -  B[0][i] != 1:
    #     print("No")
    #     exit() 
    if  (B[0][i] - 1) % 7 > (B[0][i+1] - 1) % 7:
        print("No")
        exit()

# for i in range(n-1):
#     B_add = list(map(lambda x: x+7, B[i]))
#     if B_add == B[i+1]:
#         continue
#     else:
#         print("No")
#         exit()

# print("Yes")


A = []
row = (B[0][0] - 1) // 7 
col = (B[0][0] - 1) % 7

for i in range(row, row+n):
    A.append([i * 7 + (j + 1) for j in range(col, col+m)])        

# print(A)
if A == B:
    print("Yes")
else:
    print("No")