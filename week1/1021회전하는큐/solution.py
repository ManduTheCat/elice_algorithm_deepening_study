import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  
to_pop_list = list(map(int, sys.stdin.readline().split()))  
rotating_queue = deque([i + 1 for i in range(n)])
cnt = 0
for i in to_pop_list:
    while True:
        if rotating_queue.index(i) == 0:
            rotating_queue.popleft()
            break
        elif rotating_queue.index(i) <= len(rotating_queue) - rotating_queue.index(i):
            rotating_queue.append(rotating_queue.popleft())
            cnt += 1
        else:
            rotating_queue.appendleft(rotating_queue.pop())
            cnt += 1

print(cnt)