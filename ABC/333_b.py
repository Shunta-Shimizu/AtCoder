S = list(input())
T = list(input())

S = [s for s in S]
T = [t for t in T]

same1 = [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["A", "E"]]
same2 = [["A", "C"], ["A", "D"], ["C", "E"], ["B", "D"], ["B", "E"]]
S.sort()
T.sort()

tf = False
if S in same1 and T in same1:
    tf = True

if S in same2 and T in same2:
    tf = True

if tf:
    print("Yes")
else:
    print("No")