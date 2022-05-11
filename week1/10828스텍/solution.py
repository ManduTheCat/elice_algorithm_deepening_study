import sys
import time
b_time = time.time()
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else: print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack: print(0)
        else: print(1)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else: # push X
        push_cmd, num = cmd.split()
        stack.append(int(num))
a_time = time.time()
print(a_time - b_time)