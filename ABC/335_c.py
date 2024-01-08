from collections import deque
n, q = map(int, input().split())

queries = []
nodes = [[i+1, 0] for i in range(n, -1, -1)]

for _ in range(q):
    q1, q2 = map(str, input().split())
    q1 = int(q1)

    if q1 == 1:
        x = nodes[-1][0]
        y = nodes[-1][1]
        if q2 == "R":
            add_node = [x+1, y]
        elif q2 == "L":
            add_node = [x-1, y]  
        elif q2 == "U":
            add_node = [x, y+1]
        else:
            add_node = [x, y-1]
        nodes.append(add_node)
    else:
        print(*nodes[-(int(q2))])