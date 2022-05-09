from collections import deque
N, k = map(int, input().split())
queue = deque(list(range(1, N+1)))

killed = []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    killed.append(queue.popleft())

print('<', end='')
print(*killed, sep=', ', end='')
print('>')