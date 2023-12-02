n, q = map(int, input().split())
C = list(map(int, input().split()))

queries = []
for _ in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))

box_colors = {i + 1: {C[i]} for i in range(n)}

for query in queries:
    a, b = query

    if len(box_colors[a]) > len(box_colors[b]):

        box_colors[a] |= box_colors[b]
        box_colors[b].clear()

        print(len(box_colors[a]))

        tmp = box_colors[a]
        box_colors[a] = box_colors[b]
        box_colors[b] = tmp

    else:
        box_colors[b] |= box_colors[a]
        box_colors[a].clear()
        
        print(len(box_colors[b]))
