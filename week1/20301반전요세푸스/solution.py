from collections import deque

n, k, m = map(int, input().split())
q = deque(list(range(1, n+1)))
killed = []
flag = 'right'

while q:
    if(flag=='right'):
        for _ in range(k - 1):
            q.append(q.popleft())
    else:
        for _ in range(k):
            q.insert(0, q.pop())
    killed.append(q.leftpop())

    if (len(killed)%m==0):
        flag='left' if flag=='right' else 'right'

print(*killed, sep='\n')