h, w = map(int, input().split())
c = [input() for _ in range(h)]

count_list = [0 for _ in range(w)]

for row in c:
    for i in range(len(row)):
        if row[i] == "#":
            count_list[i] += 1

for count in count_list:
    print(count, end=" ")
