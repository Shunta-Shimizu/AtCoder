from collections import deque, defaultdict
n, q = map(int, input().split())

not_called = deque(i for i in range(1, n+1))
done = set()
called = deque()
for i in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        x = not_called.popleft()
        called.append(x)
    elif event[0] == 2:
        done.add(event[1])
    else:
        tf = False
        while not tf:
            y = called.popleft()
            if y not in done:
                print(y)
                tf = True
        called.appendleft(y)

# Heapqの実装
import heapq

class Heapq:
    def __init__(self, lst=[], reverse=False):
        if reverse:
            self.pm = -1
            self.hq = [-l for l in lst]
        else:
            self.pm = 1
            self.hq = lst[:]
        heapq.heapify(self.hq)
        self.tot = sum(lst)
        self.cnt = {}
        for l in lst:
            self.cnt[l * self.pm] = self.cnt.get(l * self.pm, 0) + 1
        self.length = len(lst)

    def __bool__(self):
        return self.length > 0

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        if i == 0:
            return self.top()
        else:
            assert False

    def push(self, x):
        self.length += 1
        self.cnt[x * self.pm] = self.cnt.get(x * self.pm, 0) + 1
        heapq.heappush(self.hq, x * self.pm)
        self.tot += x

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        ret = heapq.heappop(self.hq)
        self.tot -= self.pm * ret
        self.cnt[ret] -= 1
        self.delete()
        return self.pm * ret

    def top(self):
        if self.hq:
            return self.pm * self.hq[0]
        else:
            return None

    def remove(self, x):
        if self.cnt.get(x * self.pm, 0) == 0:
            return False
        self.cnt[x * self.pm] -= 1
        self.length -= 1
        self.tot -= x
        self.delete()
        return True

    def delete(self):
        while self.hq and self.cnt.get(self.hq[0], 0) == 0:
            heapq.heappop(self.hq)

# n, q = map(int, input().split())

# not_called = Heapq([i for i in range(1, n+1)])
# called = Heapq()
# for i in range(q):
#     event = list(map(int, input().split()))
#     if event[0] == 1:
#         x = not_called.pop()
#         called.push(x)
#     elif event[0] == 2:
#         x = event[1]
#         called.remove(x)
#     else:
#         print(called[0])

