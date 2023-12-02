n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

ans = []
for i in range(q-p+1):
    ans_i = ""
    for j in range(s-r+1):
        x = p+i
        y = r+j
        if x+y == a+b or x-y == a-b:
            ans_i += "#"
        else:
            ans_i += "."
    ans.append(ans_i)

for ai in ans:
    print(ai)

