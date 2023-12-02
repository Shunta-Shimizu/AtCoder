N,M=map(int,input().split())

Pair=[[0]*(N+1) for i in range(N+1)]
#print(Pair)
for i in range(M):
    kx=list(map(int,input().split()))
    k=kx[0]
    x=kx[1:]
    for a in range(k):
        for b in range(a+1,k):
            Pair[x[a]][x[b]]=1
#print(Pair)
for a in range(1,N+1):
    for b in range(a+1,N+1):
        if Pair[a][b]==0:
            print("No")
            exit()

print("Yes")
