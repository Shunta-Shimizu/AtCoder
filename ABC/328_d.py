S = input()

ans = []
for s in S:
    ans.append(s)
    if ans[-3:] == ["A", "B", "C"]:
        ans.pop()
        ans.pop()
        ans.pop()

print(*ans, sep="")