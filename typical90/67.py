n, k = map(int, input().split())

# m進法をn進法に変換
def MtoN(m,a,n):
    s=0
    i=0
    while a>0:
        r=a%n
        s=s+r*m**i
        a=a//n
        i=i+1
    return s

ans = n
for i in range(k):
    ans = MtoN(8, int(ans), 10)
    ans = MtoN(10, ans, 9)
    
    ans = str(ans).replace("8", "5")

print(ans)
