n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
l = int(input())
C = list(map(int, input().split()))
q = int(input())
X = list(map(int, input().split()))

p = min(min(n, m), l)
abc = set()
for a in A:
    for b in B:
        for c in C:
            abc.add(a+b+c)

for x in X:
    if x in abc:
        print("Yes")
    else:
        print("No")