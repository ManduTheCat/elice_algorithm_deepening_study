import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
queue = deque([i + 1 for i in range(n)])
# 1 2 3 4 5 6 7
josephus = []
i = 1
cnt = 0
reverse_rotate = False
while queue:
    if reverse_rotate:
        x = queue.pop()
        if i == k:
            josephus.append(x)
            cnt += 1
            i = 1
        else:
            queue.appendleft(x)
            i += 1
    else:
        x = queue.popleft()
        if i == k:
            josephus.append(x)
            cnt += 1
            i = 1
        else:
            queue.append(x)
            i += 1
    if cnt == m:
        cnt = 0
        if reverse_rotate:
            reverse_rotate = False
        else:
            reverse_rotate = True

for i in josephus:
    print(i)


# 1 2 3 4 5
# 2