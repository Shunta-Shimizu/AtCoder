n = int(input())
T = input()

xy = [0, 0]
r_count = 0
for i in range(n):
    if T[i] == "S":
        if r_count % 4 == 0:
            xy[0] += 1 
            xy[0] += 0
        elif r_count % 4 == 1:
            xy[0] += 0
            xy[1] += (-1)
        elif r_count % 4 == 2:
            xy[0] += (-1)
            xy[1] += 0
        else:
            xy[0] += 0
            xy[1] += 1
    else:
        r_count += 1

print(*xy)