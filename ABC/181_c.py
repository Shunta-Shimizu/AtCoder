n = int(input())
XY = []
for _ in range(n):
    x, y = map(int, input().split())
    XY.append([x, y])

XY = sorted(XY)
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if XY[i][0] == XY[j][0]:
#                 if XY[j][0] == XY[k][0]:
#                     print("Yes")
#                     exit()
#             elif XY[j][0] == XY[k][0]:
#                 if XY[k][0] == XY[i][0]:
#                     print("Yes")
#                     exit()
#             elif XY[k][0] == XY[i][0]:
#                 if XY[i][0] == XY[j][0]:
#                     print("Yes")
#                     exit()
            
#             elif (XY[j][1]-XY[i][1]) / (XY[j][0]-XY[i][0]) == (XY[k][1]-XY[j][1]) / (XY[k][0]-XY[j][0]):
#                 print("Yes")
#                 exit()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (XY[j][1]-XY[i][1])*(XY[k][0]-XY[j][0]) == (XY[k][1]-XY[j][1])*(XY[j][0]-XY[i][0]):
                print("Yes")
                exit()
print("No")