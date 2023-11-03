n =int(input())
S = set()
tmp = 0
for i in range(n):
    s = input()
    S.add(s)
    if len(S) > tmp:
        print(i+1)
    tmp = len(S)