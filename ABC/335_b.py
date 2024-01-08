n = int(input())

for i in range(22):
    for j in range(22):
        for k in range(22):
            if i+j+k <= n:
                print(i,j,k)